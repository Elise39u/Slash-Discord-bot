import discord

async def UpdateMessage(client, beforeMessage, afterMessage): 
    member = beforeMessage.author

    if member == client.user:
        return

    if beforeMessage.content == afterMessage.content and beforeMessage.embeds == afterMessage.embeds:
        return
    
    updateEmbed = discord.Embed(title="Someone Updated their message!!", color=0x8000ff)
    updateEmbed.add_field(name="Orginal Message", value=f"**{beforeMessage.content}**", inline=False)
    updateEmbed.add_field(name="Updated Message", value=f"**{afterMessage.content}**", inline=False)
    updateEmbed.add_field(name="Link to message", value=f"{beforeMessage.jump_url}", inline=False)
    updateEmbed.set_author(name=f"{beforeMessage.author.display_name}", icon_url=member.avatar)

    channel = client.get_channel(822837640872067082)
  
    await channel.send(embed=updateEmbed)