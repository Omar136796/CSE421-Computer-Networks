import socket


DISCONNECT = "End"
FORMAT = "utf-8"
HEADER_LENGTH = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

print(f"Server is running on {SERVER}:{PORT}")

server.listen()

print(f"Server is listening on {SERVER}:{PORT}")

while True:
    conn, addr = server.accept()        # conn --> client er socket obj store korbe, addr --> socket add store krobe
    print(f"Connection from {addr} has been established")
    connected = True
    while connected:
        msg_lenghth = conn.recv(HEADER_LENGTH).decode(FORMAT)
        if msg_lenghth:
            msg_lenghth=int(msg_lenghth)
            message = conn.recv(msg_lenghth).decode(FORMAT)
            if message==DISCONNECT:
                connected=False
                conn.send("Connection closed".encode(FORMAT))
            else:
                print(message)
                conn.send("Message Received".encode(FORMAT))
    
    conn.close()       #client side e r lagbe na

