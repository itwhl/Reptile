import asyncio


async def say_hello(name):
    await asyncio.sleep(1)
    print(f'Hello, {name}!')


co1 = say_hello('Hao')
print(co1)
co2 = say_hello('Dachui')
print(co2)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([co1, co2]))
loop.close()
