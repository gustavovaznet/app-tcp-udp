import socket

#CLIENT
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#CONNECT
try:
    while True:
        message = input("Message: ") + "\n"
        client.sendto(message.encode(), ("192.168.1.3", 8000))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "quit\n" or message == "quit\n":
            break

    client.close()    

#ERRORS
except Exception as error:
    print("Error...")
    print(error)
    client.close()
