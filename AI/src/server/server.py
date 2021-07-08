import socket
import threading
import json
import cmds.match as match

class server:
    
    def __init__(self):
        self.HEADER = 2048
        self.PORT = 5050
        self.SERVER = '127.0.0.1'
        self.ADDR = (self.SERVER, self.PORT)
        self.clients = []


        self.FMT = 'utf-8'
        self.DISCONNECT_MSG = "[DISCONNECED]"


        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.run = self.start()
        
    def get_clients(self):
        return self.clients

    def handle_client(self, conn, addr):
        print(f'[NEW CONNECTION] {addr} connected')

        connected = True
        while connected:
            try:
                msg_length = conn.recv(self.HEADER).decode(self.FMT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(self.FMT)

                    if msg == self.DISCONNECT_MSG:
                        connected = False

                    print(f'[{addr}]: {msg}')

                    send = match.receive_data(json.loads(msg))
                    conn.send(json.dumps(send).encode(self.FMT))
            except:
                connected = False

        conn.close()



    def start(self):
        print("[STARTING] Server is starting...")
        server.listen()
        print(f'[LISTENING] Server is listening on {self.SERVER}')
        while True:
            conn, addr = server.accept()
            self.clients.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONENCTIONS] {threading.active_count() - 1}')
            

