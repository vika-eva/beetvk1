import socket

def start_server(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: # UDP
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"TCP Socket listening on {host}:{port}")

        connection, addr = server_socket.accept()
        with connection:
            print(f"Connected with Client({addr})")
            while True:
                data = connection.recv(1024)
                print(f"data received   {data.decode()}")
                if not data:
                    break
                print(f"receive {data.decode()} from {addr}")
                connection.send(data.upper())

if __name__ == "__main__":
    start_server()