import random 
from ..helpers import EmbedBuilder

randomPun = ["*Len and Miku talking on the phone*\nMiku: Could you do me a favour? I could really use your help.\nLen: Sure, I'll do it tomorrow.\nMiku: But Len, wouldn't you want to be....... Freely Tomorrow?\nLen: *facepalm*", "*Elise and Miku are Talking in the Arcades*\nMiku: Elise you know what is so speical about Suki Kirai?\n Elise: Ehhhee Len and Rin sing it?\nMiku: Almost Elise\nElise: Miku i wouldnt have a clue about Suki Kirai or Love hate.\nMiku: Well its appears they have a case of **Two-faced-lovers**\nElise: -.-", "Miku: Elise i wanna show you something about this arcade machine!\nElise: I swear to god miku if its anthor pun\nMiku: Why would it be? Otherwise it only would bring me down like a **deep sea girl**\nElise: That is it im *popi popio* out of here", "*Summer is rolling around and Elise, Miku, Rin and Luka are talking near the Pool of the arcade*\n Miku: Elise when your turning into a *summer idol*.\n Miku: Elise? Eliseeee? Where did she go\nElise: Not that song again. Not the spam", "*Luka and Miku and Elise are walking through the Arcade gardens*\nMiku:Luka what ever happend to your relationship with that girl\nLuka: Oh just dindt work out. But hey it brought out the song *just be friends*\nMiku: Dont you say it killed the **Love song**\nElise and Luka: MIKUUUUUUUUUUUUU"]

async def generatePun(interaction):
  await EmbedBuilder.BuildEmbed(interaction, "", random.choice(randomPun), "", 6331378, "", None, None)