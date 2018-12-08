import discord, configparser, time
from date import getCurrentICDate, getTimezone

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('Settings', 'token')
global prefix

prefix = config.get('Settings', 'prefix')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Using ' + prefix + ' as prefix for commands')
    print('------')

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix + 'hi'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith(prefix + 'date'):
        icDate = getCurrentICDate()
        msg = 'Keep in mind that this time is based on the following timezone: ' + getTimezone() + '\n' + icDate
        await client.delete_message(message)
        sentMessage = await client.send_message(message.channel, msg)
        time.sleep(5)
        await client.delete_message(sentMessage)

    if message.content.startswith(prefix + 'setprefix'):
        newprefix = str(message.content).split(" ")[1]
        config.set('Settings', 'prefix', newprefix)
        global prefix
        prefix = str(newprefix)
        await client.delete_message(message)
        sentMessage = await client.send_message(message.channel, 'The prefix has been changed to `' + newprefix + '`.')
        time.sleep(5)
        await client.delete_message(sentMessage)

client.run(TOKEN)