import socket

#CLIENT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

#CONNECT
try:
    client.connect(("127.0.0.1", 8000))
    client.send(b"Hello, how are you?\n")
    packets_received = client.recv(1024).decode()
    print(packets_received)

#ERRORS
except Exception as error:
    print("Error...")
    print(error)
