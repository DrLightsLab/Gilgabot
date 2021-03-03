import discord

class Gilgabot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Greetings mongrel!')
            print('Message from {meesage.author}: {message.content}'.format(message))
