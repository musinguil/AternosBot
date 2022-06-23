import discord
from AternosServer import AternosServer

class DiscordBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        aternos_server = AternosServer()
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.lower() == 'hello' or message.content.lower() == 'bonjour':
            await message.channel.send('Hello {0}'.format(message.author))
        elif message.content == "<@988392549695754240>":
            await message.channel.send('Ask me everything that figure in the command !help')
        elif message.content == "!help":
            await message.channel.send('''!enable_server\tenable server\n
            !status_server\tgetting status of the server''')
        elif message.content == "!enable_server":
            aternos_server.cmd(start)
        elif message.content == "!status_server":
            aternos_server.cmd(status)