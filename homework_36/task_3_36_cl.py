import asyncio

HOST = '127.0.0.1'
PORT = 8000

async def client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    print('Client connected.')
    while True:
        mess = input('enter message: ')
        writer.write(mess.encode())
        await writer.drain()
        received = await reader.read(1024)
        print(f'Received {received.decode()}')
        if mess == 'exit':
            break

        writer.close()
        await writer.wait_closed()
        print('server close')

