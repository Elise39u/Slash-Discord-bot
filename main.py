# This code is based on the following example:
#https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
import discord
from discord import app_commands
from discord.ext import commands, tasks
import server_
import os
from moderation.updateMessage import UpdateMessage
from moderation.deleteMessage import DeleteMessage
from moderation.kickUser import OnKick
from moderation.banUser import OnBan
#from moderation.banUser import on_button_click
from messageFolder.messages.HelpCommand import helpCommand
from messageFolder.messages.EliseGenderStory import EliseGenderStory
from messageFolder.messages.Socials import Socials
from messageFolder.messages.VocaloidPuns import generatePun
from messageFolder.messages.UserAvatar import getUserAvatar
from messageFolder.messages.RoleMenu import AddRole
from messageFolder.messages.OwO import text_to_owo
from messageFolder.messages.Choices import chooseAnswer
from messageFolder.messages.OwnerTest import testGiffies
from messageFolder.server.ServerLeave import onMemberLeave
from messageFolder.server.ServerJoin import onMemberJoin
from messageFolder.messages.DadJokes import onJoke
from messageFolder.messages.Clapify import clapClapClap
from messageFolder.server.ServerInfo import GetServerInfo
from youtube.youtube import checkforVideos

activity = discord.Activity(type=discord.ActivityType.watching,
                            name="your pregnant Elise")
my_secret = os.environ['TOKEN']
intents = discord.Intents.all()
client = discord.Client(intents=intents, activity=activity)
tree = app_commands.CommandTree(client)
GUILD_ID = 699557641818734634
  
@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=699557641818734634))
  channel = client.get_channel(822837640872067082)
  checkforVideos.start(client)
  AliveEmbed = discord.Embed(description="生きてる 初音エリーゼ!! Gamer miku 1.1.1b has arrived", color=65463)
  await setup_roles()
  await channel.send(embed=AliveEmbed)

def is_authorized(user):
  if user.id == 203095887264743424:
    return True
  else:
    return False


@client.event
async def on_message_edit(beforeMessage, afterMessage):
    await UpdateMessage(client, beforeMessage, afterMessage)

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    else:
        await DeleteMessage(message, client)
      
@tree.command(name = "ping", description = "Wanna ping pong or see my ms", guild=discord.Object(id=GUILD_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
  await interaction.response.send_message('Pong! Is my ping good enough or too high UwU? **{0}ms**'.format(client.latency, 1))

@tree.command(name = "hello", description = "Say hello to your gamer miku here in this sekai", guild=discord.Object(id=GUILD_ID))
async def hello_command(interaction):
  user = interaction.user
  await interaction.response.send_message(f"Hello {user.mention}! Welcome to Elise her gamer arcade sekai. \nHow can i help you today? \nMaby you wanna use \help to see what i can")

@tree.command(name = "help", description = "Wanna see what my slash commands are? Use this one then", guild=discord.Object(id=GUILD_ID))
async def help_command(interaction):
  user = interaction.user
  await helpCommand(user, interaction)
  
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

@tree.command(name = "avatar", description = "Gain a profile picture of someone who is visting the arcades", guild=discord.Object(id=GUILD_ID))
async def avatar(interaction, user: discord.Member = None):
  user = user or interaction.user
  avatar = user.avatar 
  
  if interaction.guild:
        # If we're in a guild, try to get the guild-specific avatar
        guild_avatar = user.guild_avatar
        if guild_avatar:
            avatar = guild_avatar
          
  await getUserAvatar(interaction, avatar, user)

@tree.command(name = "sekairoles", description = "Want a fancy new Sekai role? Based on the sekais of project sekai", guild=discord.Object(id=GUILD_ID))
async def addRole(interaction, role: discord.Role): 
  if role: 
    member = interaction.user
    await AddRole(member, interaction, role)

@tree.command(name = "owo", description = "OwOfys your given text", guild=discord.Object(id=GUILD_ID))
async def owoText(interaction, message: str):
  await text_to_owo(message, interaction)

@tree.command(name = "testgifs", description = "A command for Elise to test stuff with me here in the arcade", guild=discord.Object(id=GUILD_ID))
async def gifTest(interaction):
  await testGiffies(interaction)

@tree.command(name = "choice", description = "Choose between 2 options", guild=discord.Object(id=GUILD_ID))
async def choice(interaction, choice1: str, choice2: str):
  await chooseAnswer(interaction, choice1, choice2)

@tree.command(name = "kick", description = "Kick a user from the guild", guild=discord.Object(id=GUILD_ID))
async def kickUser(interaction, user: discord.Member, reason: str):
  await OnKick(interaction, reason, client, user)

@tree.command(name = "ban", description = "Ban a user from the guild", guild=discord.Object(id=GUILD_ID))
async def banUser(interaction, user: discord.Member, reason: str):
  await OnBan(interaction, reason, client, user)
  
@tree.command(name = "dadjoke", description = "Wanna hear a joke :)", guild=discord.Object(id=GUILD_ID))
async def jokeGetter(interaction):
  await onJoke(interaction, client)

@tree.command(name = "clapify", description = "Time to clap.", guild=discord.Object(id=GUILD_ID))
async def clapify(interaction, sentence: str):
  await clapClapClap(interaction, sentence, client)

@tree.command(name = "serverinfo", description = "Wanna get some sekai information :)", guild=discord.Object(id=GUILD_ID))
async def serverinfo(interaction):
  await GetServerInfo(interaction, client)

async def setup_roles():
  role_names = ['🎵 Virtual Singer', '🎸 Leo/Need', '🎼 More More Jump', '☕ Vivid Bad Squad', '🎡 Wonderlands X Showtime', '💻 Nightcord 25:00']
  for role_item in role_names:
    if role_item not in [r.name for r in client.guilds[0].roles]:
      await client.guilds[0].create_role(
        name=role_item,
        hoist=True
      )


#Check if a member has left or joined the guild
@client.event
async def on_member_join(member):
    await onMemberJoin(member, client)


@client.event
async def on_member_remove(member):
    await onMemberLeave(member, client)


server_.keep_alive()
try:
    client.run(my_secret)
except:
    print("at except")
    os.system("kill 1")
    client.run(my_secret)