from ..helpers import EmbedBuilder

async def onHelp(user, interaction):
  #await interaction.response.send_message(f"Hello {user.display_name}! <:MikuStare:1048727307612868640>. You wanted to know what i can do for you in the arcade. Here you go")

  #Embed colors/generator https://leovoel.github.io/embed-visualizer/ also fix response thing 
  await EmbedBuilder.BuildEmbed(interaction, "Found Arcade commands", "** General Commands** \n🎀 \Help --> Show this message",     "https://cdn.discordapp.com/attachments/709057115159003156/1093643303519526952/2022_08_22_15_19_12.gif", 65463, "🎀 Someone asked for help? 🎀", None, None)