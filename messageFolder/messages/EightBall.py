import random
import discord
EliseId = 203095887264743424

async def EightBallResponse(interaction, question, client):
  project_diva_responses = [
    "The rhythm of Project DIVA is uncertain, just like this question.",
    "Will the song play in harmony with your heart? 🎶",
    "<:MikuBlush:757984284052029500> The virtual divas smile upon you.",
    "As I see it, the future holds a dazzling encore for you. 🎵",
    "The Project DIVA of life is full of surprises. Can't predict what's coming next!",
    "The 8ball spins like a vocaloid twirling in anticipation... 🌀",
    "Is your dream stage waiting for you in the next song?",
    "The Project DIVA songs will guide you through the challenges of life.",
    "🎱 The answer is as unpredictable as a vocaloid concert.",
    "Your future is in harmony with the rhythm of the stars.",
    "The Project DIVA of your life will bring joy and challenges alike.",
    "Is your heart singing the melody of happiness?",
    "The Project DIVA songs will be your loyal companions on this journey.",
    "<:MikuStare:1048727307612868640> The answer is hidden within the melody of Project DIVA.",
    "Your playlist is expanding with new rhythm and beats.",
    "Just like a rhythm game, the path ahead may require precise timing and coordination.",
    "Will the songs you sing become anthems that touch people's hearts?",
    "The 8ball says, 'Congratulations! The Project DIVA of your dreams awaits.' 🎉",
    "Your playlist is now synchronized with the rhythm of life itself."
  ]
  
  pregnant_girl_responses = [
      "🎱 The future holds a precious gift within you.",
      "Will the baby's laughter bring melodies to your life? 🍼🎶",
      "<:MikuBlush:757984284052029500> You are carrying a little miracle within you.",
      "As I see it, the journey of motherhood awaits with open arms. 🤰💕",
      "The 8ball spins with anticipation for the new life you nurture... 🌀",
      "Is the baby going to dance to lullabies you sing with love?",
      "The moments of pregnancy are the most beautiful and magical ones.",
      "🎱 The answer is as mysterious as the bond between a mother and child.",
      "The baby's future is intertwined with your love and care.",
      "The Project DIVA of motherhood will bring you immense joy and challenges.",
      "Will the baby's first word be music to your ears?",
      "The journey of pregnancy is filled with melodies of hope and anticipation.",
      "<:MikuStare:1048727307612868640> The answer lies within the gentle kicks of life inside you.",
      "Your playlist now includes the sweetest lullabies for your little one.",
      "Just like a symphony, the journey of motherhood requires strength and harmony.",
      "Will the baby's arrival be the grand finale of love and happiness?",
      "The 8ball says, 'Congratulations! The Project DIVA of motherhood awaits.' 🎉",
      "Your heart beats in sync with the miracle growing inside you."
  ]
  try:
      if interaction.user.id == EliseId:
        EightBallEmebed = discord.Embed(color=6331378)
        EightBallEmebed.add_field(name="Your Question Elise", value=question, inline=False)
        EightBallEmebed.add_field(name="Elise 8ball Responses", value=random.choice(pregnant_girl_responses), inline=False)
        await interaction.response.send_message(embed=EightBallEmebed)
      else: 
          EightBallEmebed = discord.Embed(color=6331378)
          EightBallEmebed.add_field(name="Your Question", value=question, inline=False)
          EightBallEmebed.add_field(name="Eight ball responses", value=random.choice(project_diva_responses), inline=False)
          await interaction.response.send_message(embed=EightBallEmebed)
  except Exception as e:
      await ErrorHandeling(interaction, e, client)


async def ErrorHandeling(interaction, reason, client):
  logging_channel = client.get_channel(822837640872067082)

  await logging_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
  await logging_channel.send(f"<@203095887264743424><@203095887264743424> Halp Mommy Elise. I got an error while trying to make the 8ball to work: **{reason}**")  
  await interaction.response.send_message(f"Oopise the 8ball got an error try again later. {interaction.user}")