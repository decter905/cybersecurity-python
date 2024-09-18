from scapy.all import *
from scapy.layers.inet import IP, ICMP

request = IP(dst='10.16.0.1') / ICMP()
ans, unans = sr1(request, timeout=2, retry=1, verbose=1)

request_time = request.sent_time - request.time

print(f'Request time: {request_time}s')
