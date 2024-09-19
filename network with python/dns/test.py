import dns.resolver

result = dns.resolver.resolve('google.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())
