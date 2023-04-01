import socket

# cria um socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa o socket ao endereço e porta
server_address = ('localhost', 10000)
sock.bind(server_address)

# aguarda conexões
sock.listen(1)

print('Servidor TCP em %s porta %s' % server_address)

while True:
    # aguarda a chegada de uma conexão
    print('Aguardando conexão...')
    connection, client_address = sock.accept()
    print('Conexão estabelecida com', client_address)

    try:
        # recebe dados da conexão
        data = connection.recv(4096)
        print('Dados recebidos: %s' % data.decode())

        # envia uma resposta
        message = 'Resposta do servidor: ' + data.decode()
        connection.sendall(message.encode())

    finally:
        # fecha a conexão
        connection.close()