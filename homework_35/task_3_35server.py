import socket
import multiprocessing
import time, sys
import concurrent.futures

HOST = 'localhost'
PORT = 8000

def handle_client(connection):
    while True:
        data = connection.recv(1024)
        print(f'message received: {data.decode()}')
        connection.sendall(data)
        if data.decode() == 'QUIT':
            print('client disconnected')
            break
    connection.close()
    return False

def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print('Server is listening')
        while True:
            print('waiting for connection')
            connection, addr = server.accept()
            with concurrent.futures.ProcessPoolExecutor() as executor:
                p1 = executor.submit(handle_client, connection)
                result = p1.result()
            if result is False:
                break
        print('connection stopped')

if __name__ == '__main__':
    echo_server()