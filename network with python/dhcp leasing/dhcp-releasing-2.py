from scapy.all import *

from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP


def mac_to_bytes(mac_addr: str) -> bytes:
    return int(mac_addr.replace(":", ""), 16).to_bytes(6, "big")


conf.checkIPaddr = False
conf.iface = "Ethernet 5"

localiface = 'Ethernet 5'
releaseMAC = 'f2:77:c3:1d:04:03'
releaseIP = '10.16.1.95'
serverIP = '10.16.0.1'
releaseMACraw = mac_to_bytes(releaseMAC)
transactionid = int(0x7579dc58)

dhcp_release = (IP(dst=serverIP) /
                UDP(sport=68, dport=67) /
                BOOTP(chaddr=releaseMACraw, ciaddr=releaseIP, xid=transactionid) /
                DHCP(options=[('message-type', 'release'), 'end']))
send(dhcp_release)
