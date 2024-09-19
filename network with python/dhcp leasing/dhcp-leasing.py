import random

from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether, ARP

conf.iface = "Ethernet 5"
conf.checkIPaddr = False

client_mac = "F2:77:C3:1D:04:03"

dhcp_server_ip = "10.16.0.1"
dhcp_server_mac = "d8:58:d7:01:10:cf"
iface = "Ethernet 4"


def mac_to_bytes(mac_addr: str) -> bytes:
    return int(mac_addr.replace(":", ""), 16).to_bytes(6, "big")


packet = (
    Ether(dst="ff:ff:ff:ff:ff:ff") /
    IP(src="0.0.0.0", dst="255.255.255.255") /
    UDP(sport=68, dport=67) /
    BOOTP(
        chaddr=client_mac,
        xid=random.randint(1, 2**32-1),
        flags=0x8000
    ) /
    DHCP(options=[("message-type", "discover"), "end"])
)

ans = srp1(packet, timeout=5, verbose=False)

if ans:
    dhcp_request_packet = (
        Ether(dst="ff:ff:ff:ff:ff:ff", src=client_mac) /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(
            chaddr=client_mac,
            ciaddr="0.0.0.0",
            xid=ans[BOOTP].xid,
            flags=0x8000
        ) /
        DHCP(options=[
            ("message-type", "request"),
            ("server_id", ans[IP].src),
            ("requested_addr", ans[BOOTP].yiaddr),
            "end"
            ]
        )
    )

    ans = srp1(dhcp_request_packet, timeout=5, verbose=True)

    if ans:
        print("Received DHCP ACK:")
        print(ans.show())
        print("Leased IP address:", ans[BOOTP].yiaddr)
    else:
        print("No DHCP ACK received.")
else:
    print("No DHCP offer received.")





