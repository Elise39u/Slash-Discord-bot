# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
import discord
from discord import app_commands
import server_
import os

activity = discord.Activity(type=discord.ActivityType.watching,
                            name="The Arcades")
my_secret = os.environ['TOKEN']
intents = discord.Intents.all()
client = discord.Client(intents=intents, activity=activity)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=699557641818734634))
    print("I have launched with {0.user}".format(client))


@tree.command(name = "ping", description = "Wanna ping pong or see my ms", guild=discord.Object(id=699557641818734634)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
  await interaction.response.send_message('Pong! Is my ping good enough or too high UwU? **{0}ms**'.format(round(client.latency, 1)))

@tree.command(name = "hello", description = "Say hello to your gamer miku here in this sekai", guild=discord.Object(id=699557641818734634)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def hello_command(interaction):
  user = interaction.user
  await interaction.response.send_message(f"Hello {user.mention}! Welcome to Elise her gamer arcade sekai. \nHow can i help you today? \nMaby you wanna use \help to see what i can")
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


server_.awake("https://slash-discord-bot.juju125.repl.co/", False)
try:
    client.run(my_secret)
except discord.HTTPException as e:
  if e.status == 429:
    print("The Discord servers denied the connection for making too many requests")
    print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    os.system("kill 1")
  else:
    raise e