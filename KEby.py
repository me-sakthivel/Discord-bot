import discord

client = discord.Client()
#----------------------------BOTS------------------------------------------------------
@client.event
async def on_ready():
    bot_chat = client.get_channel(854073971959922718)
    await bot_chat.send("Hello everybody I'm back")


@client.event
async def on_message(message):
    if message.content == "$hi" :
        bot_chat = client.get_channel(854073971959922718)
        await bot_chat.send("Hello")


@client.event
async def on_message(message):
    if message.content == "$version" :
        bot_chat = client.get_channel(854073971959922718)
        await bot_chat.send("1.0")

#------------------------------GENERAL CHATS-----------------------------------------------


@client.event
async def on_message(message):
    if message.content == "$version" :
        bot_chat = client.get_channel(854063949338771506)
        await bot_chat.send("1.0v")

@client.event
async def on_message(message):
    if message.content == "$hi" :
        bot_chat = client.get_channel(854063949338771506)
        await bot_chat.send("Hello")

@client.event
async def on_message(message):
    if message.content == "$how are you " :
        bot_chat = client.get_channel(854063949338771506)
        await bot_chat.send("I'm just doing good.")

#Paste your token here

TOKEN = 

client.run("TOKEN")                   