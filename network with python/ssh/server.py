import paramiko
import socket
import threading

class MockSSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.username = 'testuser'
        self.password = 'testpassword'

    def check_auth_password(self, username, password):
        if username == self.username and password == self.password:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 2222))
    sock.listen(1)

    print('Mock SSH server started on localhost:2222')

    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        t = paramiko.Transport(client)
        t.start_server(server=MockSSHServer())
        t.start_server()

if __name__ == '__main__':
    start_server()