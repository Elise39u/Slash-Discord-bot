from ..helpers import EmbedBuilder

async def onHelp(user, interaction):
  #await interaction.response.send_message(f"Hello {user.display_name}! <:MikuStare:1048727307612868640>. You wanted to know what i can do for you in the arcade. Here you go")

  #Embed colors/generator https://leovoel.github.io/embed-visualizer/ also fix response thing 
  await EmbedBuilder.EmbedWithAuthorBuilder(interaction, "Found the following arcade commands", f"Hi {user.display_name} i have found the following Arcade commands for you. If you have any suggestions please contact @Hatsune Elise#0071 \n\n **Uttilty Commands** \n🎀 \Help --> Show this message\n **Fun commands** \n*Coming soon* \n **Admin commands**\n *Coming soon*",     "https://cdn.discordapp.com/attachments/709057115159003156/1093643303519526952/2022_08_22_15_19_12.gif", 65463, "🎀 Someone asked for help? 🎀", None, None, "Command List for the Arcade", "https://cdn.discordapp.com/attachments/709057115159003156/1093642977550807171/ezgif-3-f1b581708e09.gif")