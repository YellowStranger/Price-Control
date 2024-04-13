import asyncio
import json

maxlen = 524288
server = '127.0.0.1'


class Socket:
    async def send(self,message):
        self.writer.write(json.dumps(message).encode())
        await self.writer.drain()
        received = await self.reader.read(maxlen)
        received_data = json.loads(received.decode())
        print(received_data)
        return received_data

    async def login(self,email, password):
        data_to_send = {'event': 'login', 'email': email, 'password': password}
        print(data_to_send)
        received_data = await self.send(data_to_send)
        print(received_data)
        if received_data['correct']:
            self.event = 'login'
            self.correct = True
        else:
            self.event = 'login'
            self.correct = False

    async def register(self,email, password, phone):
        data_to_send = {'event': 'register', 'email': email, 'password': password, 'phone': phone}
        received_data = await self.send(data_to_send)
        if received_data['correct']:
            self.event = 'register'
            self.correct = True
        else:
            self.event = 'register'
            self.correct = False
            

    async def start(self):
        
        self.reader, self.writer = await asyncio.open_connection(server, port=5310)
    
        
    async def close(self):
        msg = {'event': 'close'}
        await self.send(msg)
        