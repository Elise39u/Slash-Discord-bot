# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
import discord
from discord import app_commands
from discord.ext import commands, tasks
import server_
import os
from messageFolder.messages.helpCommand import onHelp
from messageFolder.messages.EliseGenderStory import EliseGenderStory
from messageFolder.messages.Socials import Socials
from messageFolder.messages.VocaloidPuns import generatePun
from messageFolder.messages.UserAvatar import getUserAvatar



activity = discord.Activity(type=discord.ActivityType.watching,
                            name="The Arcades")
my_secret = os.environ['TOKEN']
intents = discord.Intents.all()
client = discord.Client(intents=intents, activity=activity)
tree = app_commands.CommandTree(client)
GUILD_ID = 699557641818734634
  
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=699557641818734634))
    #keep_alive.start()
    print("I have launched with {0.user}".format(client))


@tree.command(name = "ping", description = "Wanna ping pong or see my ms", guild=discord.Object(id=GUILD_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
  await interaction.response.send_message('Pong! Is my ping good enough or too high UwU? **{0}ms**'.format(round(client.latency, 1)))

@tree.command(name = "hello", description = "Say hello to your gamer miku here in this sekai", guild=discord.Object(id=GUILD_ID))
async def hello_command(interaction):
  user = interaction.user
  await interaction.response.send_message(f"Hello {user.mention}! Welcome to Elise her gamer arcade sekai. \nHow can i help you today? \nMaby you wanna use \help to see what i can")

@tree.command(name = "help", description = "Wanna see what my slash commands are? Use this one then", guild=discord.Object(id=GUILD_ID))
async def help_command(interaction):
  user = interaction.user
  await onHelp(user, interaction)
  
@tree.command(name = "egs", description = "Wanna know more about the EGS series on youtube or known as Elise Gender story?", guild=discord.Object(id=GUILD_ID))
async def EGS(interaction):
  await EliseGenderStory(interaction)

@tree.command(name = "socials", description = "Want to know what the socials of elise are? I can find them for you. at least the offical ones", guild=discord.Object(id=GUILD_ID))
async def socials(interaction):
  user = interaction.user
  await Socials(user, interaction)

@tree.command(name = "summer_idol", description = "Elise her favorite chart and see why", guild=discord.Object(id=GUILD_ID))
async def summer_idol(interaction):
  await interaction.response.send_message("https://cdn.discordapp.com/attachments/699557641818734638/1094899315580862534/7hmp4m.png")
  
@tree.command(name = "108", description = "Wanna know some secrets about your favourite project diva game. Its what i heared from Elise", guild=discord.Object(id=GUILD_ID))
async def oneoeight(interaction):
  user = interaction.user
  await interaction.response.send_message(f"Here you go {user.mention}! https://108memo.jp/en/#m")

@tree.command(name = "vocaloid_pun", description = "Il give you a random vocaloid pun from either here in the sekais or from Elise.", guild=discord.Object(id=GUILD_ID))
async def vocaloidPun(interaction):
  await generatePun(interaction)

@tree.command(name = "avatar", description = "*Coming Soon Avatar command*", guild=discord.Object(id=GUILD_ID))
async def avatar(interaction, user: discord.Member = None):
  user = user or interaction.user
  avatar = user.avatar 
  
  if interaction.guild:
        # If we're in a guild, try to get the guild-specific avatar
        guild_avatar = user.guild_avatar
        if guild_avatar:
            avatar = guild_avatar
          
  await getUserAvatar(interaction, avatar, user)
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


server_.keep_alive()
try:
    client.run(my_secret)
except:
    print("at except")
    os.system("kill 1")
    client.run(my_secret)