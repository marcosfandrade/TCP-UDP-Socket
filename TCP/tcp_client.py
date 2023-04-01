import socket

# cria um socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
server_address = ('localhost', 10000)
sock.connect(server_address)

# envia dados para o servidor
message = 'Hello, server!'
sock.sendall(message.encode())

# espera a resposta do servidor
data = sock.recv(4096)

print('Dados recebidos: %s' % data.decode())

# fecha o socket
sock.close()