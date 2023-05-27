import discord

async def UpdateMessage(client, beforeMessage, afterMessage): 
  channel = client.get_channel(822837640872067082)
  try:
        member = beforeMessage.author

        if member == client.user:
            return

        if beforeMessage.content == afterMessage.content and beforeMessage.embeds == afterMessage.embeds:
            return

        updateEmbed = discord.Embed(title="Someone Updated their message!!", color=0x8000ff)
        updateEmbed.add_field(name="Orginal Message", value=beforeMessage.content, inline=True)
        updateEmbed.add_field(name="Updated Message", value=afterMessage.content, inline=True)
        updateEmbed.add_field(name="Link to message", value=f"{beforeMessage.jump_url}", inline=False)
        updateEmbed.set_author(name=f"{beforeMessage.author.display_name}", icon_url=member.avatar)

        await channel.send(embed=updateEmbed)
  except Exception as e:
        # Handle the exception
        await channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
        await channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error: **{e}**")  