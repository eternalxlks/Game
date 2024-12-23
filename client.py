import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Disconnected from server.")
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

threading.Thread(target=receive_messages, args=(client,)).start()

print("Connected to server. Type your messages below.")
while True:
    message = input()
    client.send(message.encode("utf-8"))
