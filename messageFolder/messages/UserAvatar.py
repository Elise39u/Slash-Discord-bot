from ..helpers import EmbedBuilder

async def getUserAvatar(interaction, avatar, user):
  await EmbedBuilder.BuildEmbed(
        interaction, "Heres {0.display_name} their avatar".format(user),
        "I found a profile picture", avatar, 65463,
        "🎀 Profile pic 🎀", None, None)