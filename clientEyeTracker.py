import socket

#komande za eye-tracker
CALIBRATE_SHOW = b'<SET ID=\"CALIBRATE_SHOW\" STATE=\"1\" />\r\n'
ENABLE_SEND_DATA = b'<SET ID=\"ENABLE_SEND_DATA\" STATE=\"1\" />\r\n'
ENABLE_SEND_BEST_POG = b'<SET ID=\"ENABLE_SEND_POG_BEST\" STATE=\"1\" />\r\n'
ENABLE_SEND_TIME = b'<SET ID=\"ENABLE_SEND_TIME\" STATE=\"1\" />\r\n'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4242))
    s.sendall(ENABLE_SEND_DATA)
    s.sendall(ENABLE_SEND_BEST_POG)
    s.sendall(ENABLE_SEND_TIME)
    while True:
        data = s.recv(1024)
        print(repr(data))