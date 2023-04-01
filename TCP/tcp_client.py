import socket

class TCPClient:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.address, self.port))
        
        print(f"Conectando ao servidor {self.address} na porta {self.port}")
        
    def send_receive(self, message):
        try:
            self.client_socket.sendall(message.encode())
            
            data = self.client_socket.recv(1024)
            print(f"Recebido do servidor: {data.decode()}")
            
        finally:
            print("Fechando conexão com o servidor")
            self.client_socket.close()