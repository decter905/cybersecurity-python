from scapy.all import *
import codecs


def mac_to_bytes(mac_addr: str) -> bytes:
    return int(mac_addr.replace(":", ""), 16).to_bytes(6, "big")


conf.checkIPaddr=False

localiface = 'Ethernet 4'
releaseMAC = 'f3:77:c3:1d:04:03'
releaseIP='10.16.1.94'
serverIP='10.16.0.1'
releaseMACraw = mac_to_bytes(releaseMAC)


dhcp_release = IP(dst=serverIP)/UDP(sport=68,dport=67)/BOOTP(chaddr=releaseMACraw, ciaddr=releaseIP, xid=RandInt())/DHCP(options=[('message-type','release'), 'end'])
send(dhcp_release)
