import socket
import caesar

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("enter: ")
        encrypted_message = caesar.caesar_encode(message, 3)
        client_socket.sendall(encrypted_message.encode())
        response = client_socket.recv(1024).decode()
        print(f"echo from server {response}")

if __name__ == '__main__':
    start_client("127.0.0.1", 65432)