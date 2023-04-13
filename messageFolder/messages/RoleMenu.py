import discord
from ..helpers import EmbedBuilder

role_names = ['🎵 Virtual Singer', '🎸 Leo/Need', '🎼 More More Jump', '☕ Vivid Bad Squad', '🎡 Wonderlands X Showtime', '💻 Nightcord 25:00']

async def AddRole(member, interaction, role):
  if role.name in role_names:
    if role in member.roles:
      await member.remove_roles(role)
      await EmbedBuilder.BuildEmbed(interaction, "Role Removed", f"Removed the following role for you {member.display_name} the role is: {role.name} since i saw that you already had the role.", "", 6331378, "", "", "")
    else:
      await member.add_roles(role)
      await EmbedBuilder.BuildEmbed(interaction, "Role Added", f"Added the following role to you {member.display_name} the role is: {role.name}", "", 6331378, "", "", "")
  else:
    ErrorEmbed = discord.Embed(title="An Error occuerd", description="Given Role is not one of the Sekai roles. Sekai roles are: \n\n <@&1010980678998949938> \n <@&1010980219038990387> \n <@&1010981513849995425> \n <@&1010981914104041572> \n <@&1010982791623745606> \n <@&1010983272806883399>", color=16711680)
    await interaction.response.send_message(embed=ErrorEmbed)