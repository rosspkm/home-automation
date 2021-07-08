import socket
class connect:

    # intial connection to server
    def __init__(self):
        self.HEADER = 2048
        self.PORT = 5050
        self.FMT = 'utf-8'
        self.DISCONNECT_MSG = "[DISCONNECED]"

        self.SERVER = '127.0.0.1'
        self.ADDR = (self.SERVER, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    # send to server
    def process(self, msg):
        message = msg.encode(self.FMT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FMT)
        send_length += b' '* (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        while True:
            if self.client.recv(2048):
                return self.client.recv(2048).decode(self.FMT)