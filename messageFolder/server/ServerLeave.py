import random
from ..helpers import EmbedBuilder

embedLeaveUrls = ["https://images.hdqwalls.com/wallpapers/sad-miku-1a.jpg", "https://data.whicdn.com/images/104730073/original.gif", "https://cdn75.picsart.com/185243629000202.gif?to=min&r=640", "https://cdn.discordapp.com/attachments/757611689003974779/861351458824781875/ezgif-6-00b29df6c68e.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861351473162223656/ezgifmaker.gif", "https://i.pinimg.com/originals/d4/19/73/d419735eb285e55e0a38093683fb3503.gif", "https://cdn.discordapp.com/attachments/757611689003974779/861351713444331550/Hibana.gif", "https://wallpapers.com/images/hd/anime-girl-sad-alone-hatsune-miku-city-view-70uef0rsbenzw78x.jpg", "https://cdn.discordapp.com/attachments/709057115159003156/1096071814901407754/DilemmaRunMiku.gif", "https://cdn.discordapp.com/attachments/709057115159003156/1096071816814010469/P7qoKy.gif"]
imageUrl = random.choice(embedLeaveUrls)


async def onMemberLeave(member, client):
  channel = client.get_channel(797789187910664193)
  await channel.send("I saw that {0.name} has left the sekai.".format(member))
  await EmbedBuilder.BuildEmbed(None, "Someone has left the arcades", "Might we hope to see you back some day here in the arcades. <:Cute:879363818982084618>", imageUrl, 6331378, "🎀 A member has left Elise her arcade hal sekai 🎀", channel, None)