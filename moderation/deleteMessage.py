import discord

async def DeleteMessage(message, client):
  member = message.author
  channel = client.get_channel(822837640872067082)

  try:
    if member == client.user:
          return
      
    deletedEmbed = discord.Embed(title=f"A message has been deleted in {message.channel.name}", description=f"Message content: **{message.content}**", color=0xbb0000) 
    deletedEmbed.add_field(name="**Link to channel**", value=f"{message.jump_url}", inline=False)
    deletedEmbed.add_field(name="Author", value=f"{message.author}", inline=True)
    deletedEmbed.add_field(name="MessageID", value=f"{message.id}", inline=True)
    deletedEmbed.set_author(name=f"{member.display_name}", icon_url=member.avatar)
  
    if message.attachments:
          attachments_text = "\n".join([attachment.url for attachment in message.attachments])
          deletedEmbed.add_field(name="**Attachments**", value=attachments_text, inline=False)
    
    await channel.send(embed=deletedEmbed)
  except Exception as e:
        # Handle the exception
        await channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
        await channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error: **{e}**")  