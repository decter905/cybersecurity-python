import pandas as pd
import csv
import ipaddress

logs = 'log_tool.csv'


def create_csv(log_file_path, temp_log_file_path):
    df = pd.read_csv(log_file_path, on_bad_lines='skip')
    print(df.head())
    df.to_csv(temp_log_file_path, index=False)


def analyze(log_file_path):

    log_file = pd.read_csv(log_file_path)

    print("Data Summary:")
    print(log_file.info())
    print(log_file.describe())

    print("\nUnique App Names:")
    print(log_file['event_app_name'].unique())

    print("\nEvent Count by App Name:")
    print(log_file.groupby('event_app_name')['event_id'].count())

    app_center_events = log_file[log_file['event_app_name'] == 'App Center']
    print("\nApp Center Events:")
    print(app_center_events.head())


analyze(logs)


def get_ip_addresses(log_file_path):
    ip_addresses = set()
    with open(log_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ip_address = row['event_ip']
            try:
                ipaddress.ip_address(ip_address)
                ip_addresses.add(ip_address)
            except ValueError:
                pass
    return list(ip_addresses)


ipaddresses = get_ip_addresses(logs)
print(f'found {len(ipaddresses)} ip addresses: {ipaddresses}')


def get_sus(log_file_path):
    admin_ip_addresses = set()
    with open(log_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[4] == 'admin':
                admin_ip_addresses.add(row[4])
    return admin_ip_addresses


sussy_ips = get_sus(logs)
print(f'sussy ips({len(sussy_ips)}): {sussy_ips}')
