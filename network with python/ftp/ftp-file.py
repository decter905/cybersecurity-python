import paramiko

HOSTNAME = "pi2.cyber"
USERNAME = "www-data"
PASSWORD = "www-data@pi2"

transport = paramiko.Transport((HOSTNAME, 22))
transport.connect(username=USERNAME, password=PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put("dexter.txt", "/html/dexter.txt")
sftp.remove("html/index.nginx-debian.html")

for file in sftp.listdir("/html"):
    print(file)



sftp.close()
transport.close()