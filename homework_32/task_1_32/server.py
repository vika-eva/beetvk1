import socket


def start_server(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        while True:
            data, client_address = server_socket.recvfrom(2048)
            print(data)
            server_socket.sendto(f"message {data.decode()}".encode(), client_address)


if __name__ == "__main__":
    start_server()
