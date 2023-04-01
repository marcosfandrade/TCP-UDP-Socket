import socket

# cria um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia dados para o servidor
server_address = ('localhost', 10000)
message = 'Hello, server!'
sock.sendto(message.encode(), server_address)

# espera a resposta do servidor
data, address = sock.recvfrom(4096)

print('Recebido %s bytes de %s' % (len(data), address))
print('Dados recebidos: %s' % data.decode())

# fecha o socket
sock.close()