import discord

logging_channel_id = 822837640872067082
imuun_roles_guild = ["Preggo Diamond Diva Elise", "Sweetie Miku 💖", "Vocaloids", "Game guardians"] 

class BanButton(discord.ui.Button):
    def __init__(self, user, message, client, **kwargs):
      label = f"Ban {user}"
      style = discord.ButtonStyle.success
      super().__init__(style=style, label=label, **kwargs)
      self.user = user
      self.message = message  
      self.client = client
      self.id = user.id

    async def callback(self, interaction: discord.Interaction):
      #print(interaction.user.id)
      #print(self.id)
      #if interaction.user.id != self.id:
        #await interaction.response.send_message("You are not allowed to perform this action.", ephemeral=True)
        #return
      
      await interaction.message.delete()
      await banUser(interaction, self.client, self.message, self.user)
      #await interaction.response.send_message(f"Are you sure you want to ban {self.user.mention} for **{self.message}**?")

class CancelBanButton(discord.ui.Button):
    def __init__(self, user, **kwargs):
        label = f"Cancel ban on {user}"
        style = discord.ButtonStyle.danger
        super().__init__(style=style, label=label, **kwargs)
        self.user = user
        self.id = user.id

    async def callback(self, interaction: discord.Interaction):
      #print(interaction.user.id)
      #print(self.id)
      #if interaction.user.id != self.id:
        #await interaction.response.send_message("You are not allowed to perform this action.", ephemeral=True)
        #return 
        
      await interaction.response.send_message(f"Ban canceled for {self.user.mention}.")
      await interaction.message.delete()

async def OnBan(interaction, message, client, user):
    def check(confirm_ctx):
        return confirm_ctx.user.id == interaction.user.id

    user_roles = [role.name for role in user.roles]
    immune_roles = [role_name for role_name in user_roles if role_name in imuun_roles_guild]
    if immune_roles:
        role_names = '\n'.join(['- ' + role for role in immune_roles])
        await interaction.response.send_message(f"Sorry {interaction.user.mention}. Elise told me that im not allowed to ban people with the following roles:\n*{role_names}*")
        return

    if user == client.user:
        await interaction.response.send_message(f"Nice try {interaction.user.mention}. But Mommy Elise made me so that I can't ban myself :P NENENENE <:slowpoke:875806601804677240>")
        return

    ban_user_button = BanButton(user, message, client)
    cancel_ban_button = CancelBanButton(user)

    view = discord.ui.View()
    view.add_item(ban_user_button)
    view.add_item(cancel_ban_button)

    await interaction.response.send_message(f"Are you really sure you want to ban {interaction.user} for ** {message} **", view=view)

async def banUser(interaction, client, message, user):
  channel = client.get_channel(logging_channel_id)
  guild = client.get_guild(interaction.guild_id)
    
  try:
      #await interaction.followup.send(content=f'{user} has been banned for **{message}**')
      embed_banned = discord.Embed(title=f"Someone has been banned by {interaction.user}", description=f"{user.display_name} has been banned", color=0xff0000)
      embed_banned.add_field(name="Reason", value=message, inline=True)
      embed_banned.set_footer(text="🎀 Someone is banned from the arcades 🎀")
      await channel.send(embed=embed_banned)
      await guild.ban(user, reason=message)
  except discord.HTTPException as e:
    await channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
    await channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I found an error while trying to ban someone: **{e}**")  
    #await interaction.followup.send(content=f"{interaction.user} sorry i got an error while trying to ban {user} for you. I told Mommy elise about it")