import socket

class SocketUDP:
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta = porta
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def enviar(self, mensagem):
        self.socket.sendto(mensagem.encode(), (self.ip, self.porta))

    def receber(self, tamanho):
        dados, endereco = self.socket.recvfrom(tamanho)
        return dados, endereco

    def fechar(self):
        self.socket.close()

# exemplo de uso
socket_udp = SocketUDP('127.0.0.1', 8080)
mensagem = "Olá, mundo!"
socket_udp.enviar(mensagem)
resposta, endereco = socket_udp.receber(1024)
print("Resposta do servidor: ", resposta.decode())
socket_udp.fechar()
