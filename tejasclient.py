import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 65432))

message = "Hello, Server!"
client.sendall(message.encode())
print(f"Sent: {message}")
print(f"Received: {client.recv(1024).decode()}")

client.close()
