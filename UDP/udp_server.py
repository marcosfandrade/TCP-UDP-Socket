import socket

# cria um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associa o socket ao endereço e porta
server_address = ('localhost', 10000)
sock.bind(server_address)

print('Servidor UDP em %s porta %s' % server_address)

while True:
    # aguarda a chegada de dados
    data, address = sock.recvfrom(4096)

    print('Recebido %s bytes de %s' % (len(data), address))
    print('Dados recebidos: %s' % data.decode())

    # envia uma resposta
    message = 'Resposta do servidor: ' + data.decode()
    sock.sendto(message.encode(), address)