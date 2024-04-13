import asyncio
import asyncpg
import json
import enum

connections = {}

maxlen = 524288
db_host = '127.0.0.1'
db_port = 5432
db_user = 'price_user'
db_name = 'price_control'
db_password = 'test'


async def write(message,writer):
    writer.write(message)
    await writer.drain()
    print(message)

async def get_user(reader):
    received = await reader.read(maxlen)
    try:
        return json.loads(received.decode())
    except json.decoder.JSONDecodeError:
        return 

async def db_connect():
    db = await asyncpg.connect(
            host=db_host,
            port=5432,
            user=db_user,
            database=db_name,
            password=db_password)
    return db

async def login(user_data, writer):
    db = await db_connect()
    db_request = await db.fetch(
        'select email, password from users'
    )
    await db.close()
    users_list = list(map(tuple, db_request))
        
    for users in users_list:
        print(users)
        username, password = users[0], users[1]
        if user_data['email'] == username and user_data['password'] == password:
            data_to_send = {'correct': True, 'event': 'login'}
            break
            
        data_to_send = {'correct': False, 'event': 'login'}
    await write(json.dumps(data_to_send).encode(),writer)

async def register(user_data, writer):
    print(user_data)
    email, password, phone = user_data['email'], user_data['password'], user_data['phone']
        #email = email[:email.find('@')] + '\\' + email[email.find('@'):]
    print(email)
    print(email,password,phone)
    db = await db_connect()
    await db.execute(
        '''insert into users(email, phone, password) values ($1,$2,$3)''', email, phone, password
    )
    await db.close()
    data_to_send = {'correct': True, 'event': 'register'}
    await write(json.dumps(data_to_send).encode(),writer)

async def handler(reader, writer):
    global connections

    user_data = await get_user(reader)
    print(user_data)
    
    if user_data['event'] == 'login':
       await login(user_data, writer)

    elif user_data['event'] == 'register':
       await register(user_data, writer)
                
    #writer.close()
    #await writer.wait_closed()
    while True:
        data = await get_user(reader)
        if data:
           if data['event'] == 'close':
               writer.close()
               await writer.wait_closed()
               break
           if data['event'] == 'login':
            await login(user_data, writer)

           elif data['event'] == 'register':
                await register(user_data, writer)


async def main():
    server = await asyncio.start_server(handler, '127.0.0.1', 5310, limit=2097152)
    async with server:
        await server.serve_forever()
    

asyncio.run(main())