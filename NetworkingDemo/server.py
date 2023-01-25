import socket

if __name__ == '__main__':

    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1234
    addr = (host, port)
    server_socket.bind(addr)
    server_socket.listen(5)
    print('Server is ready')

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f'Got a connection from {client_addr}')
        msg = 'Hello there! Welcome to networking'
        client_socket.send(msg.encode('ascii'))
        client_resp = client_socket.recv(1024)
        print(f'The client says: {client_resp.decode()}')
