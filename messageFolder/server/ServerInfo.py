import discord
logging_channel_id = 822837640872067082

async def GetServerInfo(interaction, client):
    try:
        server = client.get_guild(699557641818734634)

        # Retrieving server information
        server_icon = server.icon
        server_owner = server.owner
        date_created = server.created_at.strftime("%Y-%m-%d %H:%M:%S")
        member_count = server.member_count
        server_roles = len(server.roles)
        channel_count = len(server.channels)
      
        serverInfoEmbed = discord.Embed(title="Arcade Sekai Information", color=6331378)
        #serverInfoEmbed.set_image(url=server_icon)
        serverInfoEmbed.set_thumbnail(url=server_icon)
        serverInfoEmbed.add_field(name="Owner", value=server_owner)
        serverInfoEmbed.add_field(name="Date Created", value=date_created)
        serverInfoEmbed.add_field(name="Member Count", value=member_count)
        serverInfoEmbed.add_field(name="Channel Count", value=channel_count)
        serverInfoEmbed.add_field(name="Roles Count", value=server_roles)

        await interaction.response.send_message(embed=serverInfoEmbed)
    
    except Exception as e:
        await onServerInfoError(client, e)
        await interaction.response.send_message(f"sorry {interaction.user.mention} i got an error while trying to find the records for the Arcade sekai. I notified Mommy Elise of the issue :) ")  

async def onServerInfoError(client, error):
  channel = client.get_channel(logging_channel_id)
  # Error logging
  await channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
  await channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error trying to find our records: **{error}**")  