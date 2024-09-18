from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import UDP, IP
import random

client_mac = "F3:77:C3:1D:04:03"

my_ip = "10.16.1.94"
dhcp_server_ip = "10.16.0.1"
dhcp_server_mac = "d8:58:d7:01:10:cf"
iface = "Ethernet 4"

fam, hw = get_if_raw_hwaddr(iface)


def mac_to_bytes(mac_addr: str) -> bytes:
    return int(mac_addr.replace(":", ""), 16).to_bytes(6, "big")


def dhcp_release():
    release_packet = (
            IP(
                src=my_ip,
                dst=dhcp_server_ip
            ) /
            UDP(
                sport=68,
                dport=67
            ) /
            BOOTP(
                chaddr=hw,
                ciaddr="0.0.0.0",
                xid=random.randint(1, 0xffffffff)
            ) /
            DHCP(options=[
                ("message-type", "release"),
                ("server_id", dhcp_server_ip),
                "end"
                ]
            )
    )

    send(release_packet, iface=iface, verbose=True)
    dhcp_release_filter = "udp and port 67 and src port 68"
    print("Sniffing...")
    acks = sniff(iface=iface, filter=dhcp_release_filter, count=1, timeout=5)

    if acks:
        print("ACK received: ")
        print(acks[0].show())
    else:
        print("No ACK received.")


dhcp_release()

