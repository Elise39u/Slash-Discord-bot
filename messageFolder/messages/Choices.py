import random 
async def chooseAnswer(interaction, choice1, choice2):
  choicesList = [choice1, choice2]
  await interaction.response.send_message("I choose for you >.<: **" + random.choice(choicesList) + "** Did i do well?")