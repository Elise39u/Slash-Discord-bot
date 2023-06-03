import discord

async def BuildEmbed(message, embedTitle, embedDescription, imageUrl, colour,
                     footer, channel, url):
    newEmbed = discord.Embed(title=embedTitle, description=embedDescription)
    if not colour:
        newEmbed.colour = 0xfe3ee4
    else:
        newEmbed.colour = colour
    if len(imageUrl) > 0:
        newEmbed.set_image(url=imageUrl)
    newEmbed.set_footer(text=footer)
    if url:
      newEmbed.url = url;
    if message is None:
      await channel.send(embed=newEmbed)
    else: 
      await message.response.send_message(embed=newEmbed)


async def EmbedWithAuthorBuilder(message, embedTitle, embedDescription, imageUrl, colour,
                     footer, channel, url, authorName, authorImage):
    newEmbed = discord.Embed(title=embedTitle, description=embedDescription)
    newEmbed.set_author(name=authorName, icon_url=authorImage)
    if not colour:
        newEmbed.colour = 0xfe3ee4
    else:
        newEmbed.colour = colour
    if len(imageUrl) > 0:
        newEmbed.set_image(url=imageUrl)
    newEmbed.set_footer(text=footer)
    if url:
      newEmbed.url = url;
    if message is None:
      await channel.send(embed=newEmbed)
    else: 
      await message.response.send_message(embed=newEmbed)
