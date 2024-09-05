import pandas as pd
import re


def extract_ip_addresses(log_file):
    ip_addresses = set()

    with open(log_file, "r") as file:
        for line in file:
            fields = line.strip().split(",")

            if len(fields) > 5:
                ip_addresses.add(fields[5])

    return ip_addresses


def preprocess_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        content = file.read()

    processed_content = re.sub(r'\(([^)]+)\)', lambda x: x.group(0).replace(',', ';'), content)

    with open(log_file_path, 'w') as file:
        file.write(processed_content)


def extract_devices_and_ips_from_log(log_file_path):
    temp_file_path = 'temp_log.csv'

    preprocess_log_file(log_file_path)

    log_file = pd.read_csv(temp_file_path, skipinitialspace=True)

    ip_device_mapping = log_file.groupby('conn_ip')['conn_client_agent'].unique().apply(list).to_dict()

    results = {
        "ip_device_mapping": ip_device_mapping,
    }

    return results


logs = "connection_log.txt"
devices_ips = extract_devices_and_ips_from_log(logs)

for ip, devices in devices_ips['ip_device_mapping'].items():
    print(f"IP Address: {ip}")
    for device in devices:
        print(f"  Device: {device}")


def extract_devices_and_users(log_file_path):
    preprocess_log_file(log_file_path)

    log_file = pd.read_csv(log_file_path, skipinitialspace=True)

    device_user_mapping = log_file.groupby('conn_user')['conn_client_agent'].unique().apply(list).to_dict()

    return device_user_mapping


devices_users = extract_devices_and_users(logs)

for user, devices in devices_users.items():
    print(f'User: {user}')
    for device in devices:
        print(f'  Device: {device}')


def extract_failed_connection_attempts(log_file_path):
    preprocess_log_file(log_file_path)

    log_file = pd.read_csv(log_file_path, skipinitialspace=True)

    failed_attempts = log_file[log_file['conn_type'] == 1]

    return failed_attempts


failed_connection_attempts = extract_failed_connection_attempts(logs)

for _, attempt in failed_connection_attempts.iterrows():
    print(f"Failed attempt by {attempt['conn_user']} with connection type of {attempt['conn_type']} from IP {attempt['conn_ip']} at {attempt['conn_date']} {attempt['conn_time']}")
