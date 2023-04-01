import socket

class TCPServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.address, self.port))
        self.server_socket.listen(1)
        
        print(f"Iniciando servidor no endereço {self.address} na porta {self.port}")
        
    def serve_forever(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Conexão recebida de {client_address}")
            try:
                data = client_socket.recv(1024)
                print(f"Recebido do cliente: {data.decode()}")
                
                message = "Olá, cliente!"
                client_socket.sendall(message.encode())
                
            finally:
                print(f"Fechando conexão com {client_address}")
                client_socket.close()