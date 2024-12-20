import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_client:
        message = input("Enter message: ")
        socket_client.sendto(message.encode(), (host, port))
        response, server_address = socket_client.recvfrom(2048)
        print(f"echo server {response.decode()}")



if __name__ == "__main__":
    start_client("127.0.0.1", 65432)