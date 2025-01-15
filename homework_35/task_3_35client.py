import socket
import time
import multiprocessing

HOST = 'localhost'
PORT = 8000

def client_main(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('connected')

        while True:
            message = input('enter message: ')
            s.sendall(message.encode())
            rec = s.recv(1024)
            print(rec.decode())
            if message == 'exit':
                break
        print('disconnected')

if __name__ == '__main__':
    client_main()