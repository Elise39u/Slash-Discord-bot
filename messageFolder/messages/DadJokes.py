import requests
import discord

async def onJoke(interaction, client):
  response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json", "User-Agent": "https://github.com/Elise39u/Slash-Discord-bot"})
  jokeData = response.json();
  if(jokeData['status'] == 200):
    jokeEmbed = discord.Embed(color=6331378)
    jokeEmbed.add_field(name="Dad Joke", value=jokeData['joke'], inline=False)
    await interaction.response.send_message(embed=jokeEmbed)
  else:
    await ErrorHandeling(interaction, jokeData['status'], client)


async def ErrorHandeling(interaction, reason, client):
  logging_channel = client.get_channel(822837640872067082)

  await logging_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
  await logging_channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error status while trying to get a joke: **{reason}**")  
  await interaction.response.send_message(f"Oopise i found status code {reason}. I notified Mommy Elise but for now try later to gain a new joke. {interaction.user}")