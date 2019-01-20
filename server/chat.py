import socket
import threading
import sys
import time

class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    connections = []
    
    def __init__(self):

        self.sock.bind(('0.0.0.0', 10000))

        self.sock.listen(1)


    def handler(self, c, a):
        while True:
            data = c.recv(1024)

            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break
    
    def run(self):
        while True:
            c, a = self.sock.accept()
            c_thread = threading.Thread(target=self.handler, args=(c,a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(c)

            print(str(a[0]) + ':' + str(a[1]), "connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, address):
        self.sock.connect((address, 10000))        

        iThread = threading.Thread(target=self.send_message)
        iThread.daemon = True
        iThread.start()
   
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
    
    def send_message(self):
        while True:
            self.sock.send(bytes(input(), 'utf-8'))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        client = Client(sys.argv[1])
    else:
        server = Server()  
        server.run()