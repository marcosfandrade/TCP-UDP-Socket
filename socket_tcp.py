import socket

class SocketTCP:
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta = porta
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        self.socket.connect((self.ip, self.porta))

    def enviar(self, mensagem):
        self.socket.sendall(mensagem.encode())

    def receber(self, tamanho):
        return self.socket.recv(tamanho)

    def fechar(self):
        self.socket.close()

# exemplo de uso
socket_tcp = SocketTCP('127.0.0.1', 8080)
socket_tcp.conectar()
mensagem = "Olá, mundo!"
socket_tcp.enviar(mensagem)
resposta = socket_tcp.receber(1024)
print("Resposta do servidor: ", resposta.decode())
socket_tcp.fechar()
