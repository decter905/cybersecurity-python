import pandas as pd
import re
from datetime import timedelta

log_file_path = "gitlab_access.log"


def get_failed_attempts():
    failed_connections = []

    pattern = re.compile(r'HTTP/\d\.\d"\s(4\d{2}|5\d{2})\b')

    with open(log_file_path, 'rt') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                failed_connections.append(line.strip())

    df = pd.DataFrame(failed_connections, columns=['Log Entry'])

    df.to_csv("failed_connections.csv", index=False)

    return df


def get_suspicious_ips(log_file):
    ip_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    timestamp_pattern = r'\[(?P<timestamp>[^\]]+)\]'

    log_file['IP'] = log_file['Log Entry'].apply(lambda x: re.search(ip_pattern, x).group('ip') if re.search(ip_pattern, x) else None)
    log_file['Timestamp'] = log_file['Log Entry'].apply(lambda x: re.search(timestamp_pattern, x).group('timestamp') if re.search(timestamp_pattern, x) else None)

    log_file['Timestamp'] = pd.to_datetime(log_file['Timestamp'], format='%d/%b/%Y:%H:%M:%S %z')

    log_file = log_file.sort_values(by=['IP', 'Timestamp'])

    time_window = timedelta(minutes=1)

    log_file['Prev_Timestamp'] = log_file.groupby('IP')['Timestamp'].shift(1)

    log_file['Time_Diff'] = log_file['Timestamp'] - log_file['Prev_Timestamp']

    suspicious_requests = log_file[log_file['Time_Diff'] <= time_window]

    suspicious_ips = suspicious_requests['IP'].value_counts().reset_index()
    suspicious_ips.columns = ['IP', 'Count']
    suspicious_ips = suspicious_ips[suspicious_ips['Count'] > 20]  # Adjust threshold as needed

    suspicious_ips.to_csv('suspicious_ips_short_timespan.csv', index=False)


# Run the functions
failed_connections_log_file = get_failed_attempts()
get_suspicious_ips(failed_connections_log_file)
