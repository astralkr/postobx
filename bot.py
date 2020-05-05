import discord
import os

client = discord.Client()



@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('----')
    game = discord.Game("우체국 시험중!")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.abc.PrivateChannel) and message.author.id != 70708503995914651:
        channel = client.get_channel(707089326781104179)
        await channel.send(str(message.author.name) + "(" + str(message.author.id) + ") : " + str(message.content))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
