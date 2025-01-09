import socket, threading


def client_thread():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', 8080))
        t = threading.Thread(target=client_socket.send, args=(client_socket,), daemon=True)
        t.start()
        name = input('Enter your name: ')
        while True:
            message = input('Enter a message: ')
            send = f'{name}: {message}'
            client_socket.send(send.encode())
            received = client_socket.recv(1024)
            print(received.decode())
            if message == 'quit':
                print('Bye!')
                break