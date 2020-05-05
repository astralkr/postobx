import discord

client = discord.Clinet()

@client.event
async def on_ready():
    print('login')
    print(clinet.user.name)
    print(client.user.id)
    print('--------------------')
    await client.change_presence(game=discord.Game(name='Postbox' , type=1))

@client.event
async def on_message(message):
    if client.private_channels and message.author.id != (707085039959146516):
        await client.get_channel(707089326781104179).send(message.author.name + "(" + str(message.author.id) + "): " + message.content)


    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
