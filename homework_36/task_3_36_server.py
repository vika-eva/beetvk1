import asyncio

HOST = '127.0.0.1'
PORT = 8000

run_serv = True

async def client_handler(reader, writer):
    request = None
    while request != 'exit':
        request = await reader.read(1024)
        response = str(eval(request)) + '\n'
        writer.write(response.encode())
        await writer.drain()
    writer.close()

async def serv():
    server = await asyncio.start_server(client_handler, HOST, PORT)
    async with server:
        print('server run')
        await server.serve_forever()

