import socket
import threading

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

print("Server is running...")
while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
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
