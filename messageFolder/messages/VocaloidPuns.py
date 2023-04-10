import random 
from ..helpers import EmbedBuilder

randomPun = ["*Len and Miku talking on the phone*\nMiku: Could you do me a favour? I could really use your help.\nLen: Sure, I'll do it tomorrow.\nMiku: But Len, wouldn't you want to be....... Freely Tomorrow?\nLen: *facepalm*", "*Elise and Miku are Talking in the Arcades*\nMiku: Elise you know what is so speical about Suki Kirai?\n Elise: Ehhhee Len and Rin sing it?\nMiku: Almost Elise\nElise: Miku i wouldnt have a clue about Suki Kirai or Love hate.\nMiku: Well its appears they have a case of **Two-faced-lovers**\nElise: -.-"]

async def generatePun(interaction):
  await EmbedBuilder.BuildEmbed(interaction, "", random.choice(randomPun), "", 16776960, "", None, None)