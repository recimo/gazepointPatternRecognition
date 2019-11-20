import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4242))
    s.listen()
    clientsocket, adress = s.accept()
    with clientsocket:
        print('Connected by', adress)
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.sendall(data)
