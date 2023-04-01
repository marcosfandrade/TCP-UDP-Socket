import socket

class UDPClient:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        print(f"Conectando ao servidor {self.address} na porta {self.port}")
        
    def send_receive(self, message):
        try:
            self.client_socket.sendto(message.encode(), (self.address, self.port))
            
            data, server_address = self.client_socket.recvfrom(1024)
            print(f"Recebido do servidor: {data.decode()}")
            
        finally:
            print("Fechando conexão com o servidor")
            self.client_socket.close()