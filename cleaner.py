import discord
import asyncio

TOKEN = ""
client = discord.Client()
blacklist = {''}


async def main():
    print('Script is initializing!')
    await asyncio.sleep(15)
    for x in client.private_channels:
        if str(x.type) == 'group':
            if not any(int(x.id) == int(d) for d in blacklist):
                await x.leave()
                print(F'Left {x.name}, Good Riddance!')


client.loop.create_task(main())
try:
    client.run(TOKEN, bot=False)
except Exception as e:
    print(e)