import socket
from scapy.all import sr1
from scapy.layers.inet import IP, TCP
from tkinter import *
from tkinter.ttk import Progressbar
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

def send_status_report():
    print({"timestamp": datetime.datetime,
           "services": {

           }
           })

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
    for serv, info in EXPECTED_SERVICES.items():
        port = info["port"]
        protocol = info["protocol"]
        expected_status = info["expected_status"]
        port_open = check_port(ip, port, protocol)
        # update_gui(serv, port_open, expected_status)
        return ip, port, protocol, expected_status

def update_gui(serv, port_open, expected_status):
    if port_open and expected_status == "Enabled":
        service_bars[serv]["progress"].set(100)
        service_bars[serv]["label"].config(fg="green", text=f"{serv}: Active")
    elif not port_open and expected_status == "Disabled":
        service_bars[serv]["progress"].set(100)
        service_bars[serv]["label"].config(fg="green", text=f"{serv}: Inactive (as expected)")
    elif port_open and expected_status == "Disabled":
        service_bars[serv]["progress"].set(0)
        service_bars[serv]["label"].config(fg="red", text=f"Warning: {serv} should be disabled!")
    elif not port_open and expected_status == "Enabled":
        service_bars[serv]["progress"].set(0)
        service_bars[serv]["label"].config(fg="red", text=f"Warning: {serv} should be active!")

def scan_periodically():
    scan_ports(TARGET_IP)
    root.after(SCAN_INTERVAL * 1000, scan_periodically)


root = Tk()
root.title("Service Monitor")

service_bars = {}
for service in EXPECTED_SERVICES:
    frame = Frame(root)
    frame.pack(pady=5)
    label = Label(frame, text=f"{service}: Checking...", width=30, anchor="w")
    label.pack(side=LEFT, padx=10)
    progress = IntVar()
    bar = Progressbar(frame, length=200, mode='determinate', maximum=100, variable=progress)
    bar.pack(side=RIGHT, padx=10)
    service_bars[service] = {"label": label, "progress": progress}

root.after(1000, scan_periodically)
root.mainloop()
