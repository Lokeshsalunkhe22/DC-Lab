import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 65432))
server.listen()
print("Server listening on port 65432...")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    if data:
        print(f"Received: {data.decode()}")
        conn.sendall(data)
    conn.close()
