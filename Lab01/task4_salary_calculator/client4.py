import socket

FORMAT = "utf-8"
HEADER_LENGTH = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)
DISCONNECT = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)       #encoded msg er length
    send_length=str(msg_length).encode(FORMAT)
    send_length+=(HEADER_LENGTH-len(send_length))* b' '

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))


while True:
    message=input("Enter hours worked: ")

    send(message)

    if message==DISCONNECT:
        break