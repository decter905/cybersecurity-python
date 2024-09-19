import dns.resolver
import socket


def get_ip_of_host(host):
    return socket.gethostbyname(host)


def get_ip_of_host2(host, dnsserver):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dnsserver]
        answer = resolver.resolve(host, 'A')
        for rdata in answer:
            return rdata.address
    except dns.resolver.NoAnswer:
        return 'No answer.'
    except dns.resolver.NXDOMAIN:
        return None


dns_server = '10.16.0.1'
hostname = 'google.com'
ip_address = get_ip_of_host2(hostname, dns_server)
print(f"IP address for {hostname}: {ip_address}")
