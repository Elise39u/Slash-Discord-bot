import os
import discord

Admin_RoleID = 699558391894507620
Booster_RoleID = 790938505823518751
Elise_RoleID = 875058552006393947
Sub_Roles = 882546255446822932
EmbedImage = "https://cdn.discordapp.com/attachments/709057115159003156/1093643303519526952/2022_08_22_15_19_12.gif"

#Embed colors/generator https://leovoel.github.io/embed-visualizer/ also fix response thing 
script_dir = os.path.dirname(os.path.abspath(__file__))
commands_dir = os.path.join(script_dir, 'commands')

def load_Commands(file_path):
    with open(file_path, 'r') as file:
        commands = [line.strip() for line in file]
    formatted_text = "\n".join(commands)
    return formatted_text

admin_commands = load_Commands(os.path.join(commands_dir, 'adminCommands.txt'))
utility_commands = load_Commands(os.path.join(commands_dir, 'utilityCommands.txt'))
fun_commands = load_Commands(os.path.join(commands_dir, 'funCommands.txt'))
arcade_commands = load_Commands(os.path.join(commands_dir, 'arcadeLoreCommands.txt'))
booster_commands = load_Commands(os.path.join(commands_dir, 'boosterCommands.txt'))
sub_commands = load_Commands(os.path.join(commands_dir, 'subCommands.txt'))

async def helpCommand(user, interaction):
  user_roles = [role.id for role in user.roles]
  added_roles = set()  # Set to keep track of added roles
  
  helpEmbed = discord.Embed(title="Commands in the Girly Gamer Arcade", description="You have access to the following commands. If you have any suggestions make sure to contact @Hatsune Elise#0071", color=6331378)
  helpEmbed.set_author(name="Command List", icon_url="https://cdn.discordapp.com/attachments/491904770236481549/1093854438566924509/hatsune-miku-sleeping-sitting-twintails-wallpaper-preview.jpg")
  helpEmbed.set_footer(text="🎀 Im gonna hit Elise :-} 🎀")
  helpEmbed.set_image(url=EmbedImage)
  helpEmbed.add_field(name="Utility Commands", value=utility_commands, inline=False)
  helpEmbed.add_field(name="Fun Commands", value=fun_commands, inline=False)
  helpEmbed.add_field(name="Arcade Lore Commands", value=arcade_commands, inline=False)

  if Elise_RoleID in user_roles and "Elise" not in added_roles: 
    helpEmbed.add_field(name="Admin commands", value=admin_commands, inline=False)
    helpEmbed.add_field(name="Booster Commands", value=booster_commands, inline=False)
    helpEmbed.add_field(name="Sub Commands", value=sub_commands, inline=False)
    added_roles.update(["Admin", "Booster", "Sub", "Elise"])
  
  if Admin_RoleID in user_roles and "Admin" not in added_roles: 
    helpEmbed.add_field(name="Admin commands", value=admin_commands, inline=False)
    added_roles.add("Admin")
  
  if Booster_RoleID in user_roles and "Booster" not in added_roles:
    helpEmbed.add_field(name="Booster Commands", value=booster_commands, inline=False)
    added_roles.add("Booster")
    
  if Sub_Roles in user_roles and "Sub" not in added_roles: 
    helpEmbed.add_field(name="Sub Commands", value=sub_commands, inline=False)
    added_roles.add("Sub")
    
  await interaction.response.send_message(embed=helpEmbed)