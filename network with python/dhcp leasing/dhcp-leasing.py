import random

from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether, ARP

client_mac = "F3:77:C3:1D:04:03"

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
        chaddr=mac_to_bytes(client_mac),
        xid=random.randint(1,2**32-1),
    ) /
    DHCP(options=[("message-type", "discover"), "end"])
)

ans = sendp(packet, iface=iface, verbose=True)

dhcp_offer_filter = "udp and port 67 and src port 67"
print('Sniffing DHCP offers...')
dhcp_offers = sniff(iface=iface, filter=dhcp_offer_filter, count=1, timeout=10)

if dhcp_offers:
    print("Received DHCP offer:")
    dhcp_offer_pkt = dhcp_offers[0]
    print(dhcp_offer_pkt.show())

    offered_ip = dhcp_offer_pkt[BOOTP].yiaddr

    arp_pkt = ARP(pdst=offered_ip)
    ans, unans = srp(arp_pkt, timeout=1, verbose=False)

    if ans:
        print(f"IP address {offered_ip} is already in use")
    else:
        print(f"IP address {offered_ip} is available")

    dhcp_request_packet = (
        Ether(dst="ff:ff:ff:ff:ff:ff", src=client_mac) /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(
            chaddr=mac_to_bytes(client_mac),
            xid=dhcp_offer_pkt[BOOTP].xid,
        ) /
        DHCP(options=[
            ("message-type", "request"),
            ("server_id", dhcp_offer_pkt[DHCP].options[1][1]),
            ("requested_addr", dhcp_offer_pkt[BOOTP].yiaddr),
            "end"
        ])
    )

    ans = sendp(dhcp_request_packet, iface=iface, verbose=True)

    dhcp_ack_filter = "udp and port 67 and src port 67"
    print('Sniffing for ACKs...')
    dhcp_acks = sniff(iface=iface, count=1, timeout=10)

    if dhcp_acks:
        print("Received DHCP ACK:")
        dhcp_ack_pkt = dhcp_acks[0]
        print(dhcp_ack_pkt.show())
        print("Leased IP address:", offered_ip)
    else:
        print("No DHCP ACK received.")
else:
    print("No DHCP offer received.")
