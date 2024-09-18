from scapy.all import *


fam, hw = get_if_raw_hwaddr('WLAN')
def dhcp_release():
    send(IP())