import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    #We do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('What can you do'):
        msg = 'Try sending me a sentence using !reverse and I will reverse it'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!reverse'):
      msg = message.content[8::]
      await client.send_message(message.channel, msg[::-1])
      
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
