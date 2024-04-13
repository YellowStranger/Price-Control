import asyncio
import json

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 5310)
    data = {'name': 'andrey', 'email':'coolandr@mail.ru'}
    writer.write(json.dumps(data).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


asyncio.run(main())