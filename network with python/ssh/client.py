import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="nuc.cyber", username="ssh", password="test" )
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("systemctl status apache2.service; ls -l; uptime")
print(ssh_stdout.read().decode())
ssh.close()
