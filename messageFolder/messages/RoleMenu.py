import discord
from ..helpers import EmbedBuilder

role_names = ['🎵 Virtual Singer', '🎸 Leo/Need', '🎼 More More Jump', '☕ Vivid Bad Squad', '🎡 Wonderlands X Showtime', '💻 Nightcord 25:00']

async def AddRole(member, interaction, role):
  if role.name in role_names:
    if role in member.roles:
      await member.remove_roles(role)
      await EmbedBuilder.BuildEmbed(interaction, "Role Removed", f"Removed the following role for you {member.display_name} the role is: {role.name} since i saw that you already had the role.", "", "", "", "", "")
    else:
      await member.add_roles(role)
      await EmbedBuilder.BuildEmbed(interaction, "Role Added", f"Added the following role to you {member.display_name} the role is: {role.name}", "", "", "", "", "")
  else:
    ErrorEmbed = discord.Embed(title="An Error occuerd", description="Given Role is not one of the Sekai roles. Sekai roles are: \n\n Virtual Singer\n Leo/Need\n More More Jump\n Vivid Bad Sqaud\nWonderlands X Showtime\nNightcord 25:00 ", color=16711680)
    await interaction.response.send_message(embed=ErrorEmbed)