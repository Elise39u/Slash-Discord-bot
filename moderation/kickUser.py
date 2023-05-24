import discord
logging_channel_id = 822837640872067082
allowed_roles = ["Diamond Diva Elise", "Sweetie Miku 💖", "Vocaloids", "Game guardians"]  # List of imuun role names

async def OnKick(interaction, message, client, user):
  try:
    
    # Check if the user being kicked has any of the allowed roles
    user_roles = [role.name for role in user.roles]
    immuun_roles = [role_name for role_name in user_roles if role_name in allowed_roles]
    if immuun_roles:
        role_names = '\n'.join(immuun_roles)
        await interaction.response.send_message(f"Sorry {interaction.user.mention}. Elise told me that im not allowed to kick people with the following roles: \n *{role_names}*")
        return
      
    # Check if the user being kicked is the bot itself
    if user == client.user:
        await interaction.response.send_message(f"Nice try {interaction.user.mention}. But Mommy Elise made me so that i cant kick my self :P NENENENE <:slowpoke:875806601804677240>")
        return

    guild = client.get_guild(interaction.guild_id)
    await guild.kick(user, reason=message)
    await interaction.response.send_message(f'{user} has been kicked for **{message}**')
    channel = client.get_channel(logging_channel_id)
    
    EmbedKicked = discord.Embed(title=f"Someone has been kicked by {interaction.user.display_name}", description=f"{user.display_name} hasbeen kicked", color=0xff0000)
    EmbedKicked.add_field(name="Reason", value=message, inline=True)
    EmbedKicked.set_footer(text="🎀 Someone is kicked out of the arcades 🎀")
    await channel.send(embed=EmbedKicked)
  except discord.Forbidden:
        await OnKick_error(client, "Mommy Elise im not allowed to Kick people :(")
  except discord.HTTPException as e:
        error_message = f"Mommy Elise i found an error while trying to kick: {user}: {e}"
        await OnKick_error(error_message)

#turn into a error handler
async def OnKick_error(client, error):
    channel = client.get_channel(logging_channel_id)
    # Error logging
    await channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
    await channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error: **{error}**")  