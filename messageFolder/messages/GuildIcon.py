from ..helpers import EmbedBuilder
import discord

async def getGuildIcon(interaction, client):
  guild = client.get_guild(699557641818734634)

  if guild.icon:
    await EmbedBuilder.BuildEmbed(interaction, "I found an server avatar {0.display_name}".format(interaction.user), "I found the server avatar", guild.icon, 6331378, "🎀 Server pic 🎀", None, None)
  else: 
    await EmbedBuilder.BuildEmbed(interaction, "", "I couldnt find the server avatar sorry :(. Ask your preggie server owner for it", "", "", "🎀 Error found 🎀", None, None)