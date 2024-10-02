import paramiko

HOSTNAME = "pi2.cyber"
USERNAME = "www-data"
PASSWORD = "www-data@pi2"

transport = paramiko.Transport((HOSTNAME, 22))
transport.connect(username=USERNAME, password=PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)

foldername = "/html/test_decter"

sftp.mkdir(foldername)
print(f"Ordner '{foldername}' erstellt.")
print(sftp.listdir("/html"))

sftp.rmdir(foldername)
sftp.listdir("/html")
print(f"Ordner '{foldername}' gelöscht.")
print(sftp.listdir("/html"))

sftp.close()
transport.close()