import socket


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('Vinods-MBP16.local', 1234))
    resp = s.recv(1024)
    print(f'Server says: {resp.decode()}')
    msg = input('Enter a message to the server: ')
    s.send(msg.encode('ascii'))
    s.close()