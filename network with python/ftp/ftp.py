import paramiko

def connect_to_sftp_server():
    try:
        transport = paramiko.Transport(("pi2.cyber", 22))
        transport.connect(username="www-data", password="www-data@pi2")
        sftp = paramiko.SFTPClient.from_transport(transport)

        try:
            sftp.mkdir("/html/test_dexter")
        except IOError as error:
            print(f"Error creating directory: {error}")

        print(sftp.listdir("/html"))

        try:
            sftp.rmdir("/html/test_dexter")
        except IOError as error:
            print(f"Error removing directory: {error}")

        print(sftp.listdir("/html"))
        sftp.close()
        transport.close()


    except paramiko.SSHException as error:
        print(f"Error: {error}")


connect_to_sftp_server()