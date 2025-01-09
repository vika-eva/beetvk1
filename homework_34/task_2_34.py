import socket, threading

def handle_client(client_socket, addr):
    print(f"handling connection from {addr}")
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"{addr}: {message}")
                client_socket.send(f"echo {message}".encode())
            else:
                print(f"client disconnected: {addr}")
                break
    finally:
        client_socket.close()

def start_server(host='localhost', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"client connected: {threading.active_count()-1}")



