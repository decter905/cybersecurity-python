import socket
from tkinter import Tk

from scapy.all import sr1
from scapy.layers.inet import IP, TCP
import json
import datetime

TARGET_IP = "pi2.cyber"
SCAN_INTERVAL = 60

EXPECTED_SERVICES = {
    "SSH": {"port": 22, "protocol": "tcp", "expected_status": "Enabled"},
    "HTTP": {"port": 80, "protocol": "tcp", "expected_status": "Enabled"},
    "HTTPS": {"port": 443, "protocol": "tcp", "expected_status": "Enabled"},
    "FTP": {"port": 21, "protocol": "tcp", "expected_status": "Enabled"},
    "DNS": {"port": 53, "protocol": "udp", "expected_status": "Disabled"},
    "DHCP": {"port": 67, "protocol": "udp", "expected_status": "Disabled"},
}

def check_port(ip, port, protocol):
    if protocol == "tcp":
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            return True
    elif protocol == "udp":
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b"", (ip, port))
            sock.recvfrom(1024)
            sock.close()
            return True
        except socket.error:
            return False
    return False

def scan_ports(ip):
    scan_results = {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), "services": {}}
    for serv, info in EXPECTED_SERVICES.items():
        port = info["port"]
        protocol = info["protocol"]
        expected_status = info["expected_status"]
        port_open = check_port(ip, port, protocol)
        scan_results["services"][serv.lower()] = {"expected": expected_status == "Enabled", "actual": port_open}
    return scan_results

def save_scan_results(scan_results):
    try:
        with open("scan_results.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(scan_results)
    with open("scan_results.json", "w") as f:
        json.dump(data, f, indent=4)

def scan_periodically():
    scan_results = scan_ports(TARGET_IP)
    save_scan_results(scan_results)
    root.after(SCAN_INTERVAL * 1000, scan_periodically)

root = Tk()
root.title("Service Monitor")

root.after(1000, scan_periodically)
root.mainloop()