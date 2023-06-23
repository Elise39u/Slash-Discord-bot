import random
import discord
EliseId = 203095887264743424

async def EightBallResponse(interaction, question, client):
  project_diva_responses = [
     "🎤 Hatsune Miku says yes!",
    "🎵 The rhythm is certain.",
    "🎶 Absolutely like Project DIVA!",
    "🎧 Yes, like a VOCALOID melody!",
    "🎹 It's as reliable as KAITO's voice.",
    "🎵 As I see it, yes, like Megurine Luka's charm.",
    "🎶 Most likely, just like MEIKO's popularity.",
    "🎧 Outlook good, like a captivating concert!",
    "🎹 Yes, like the beat of a VOCALOID song!",
    "🎤 Signs point to yes, just like Rin and Len's duet.",
    "🎵 Reply hazy, try again while playing Project DIVA.",
    "🎶 Ask again later, after listening to some VOCALOID tunes.",
    "🎧 Better not tell you now, enjoy the suspense like in a music video.",
    "🎹 Cannot predict now, like the unpredictable charm of Project DIVA.",
    "🎤 Concentrate and ask again while humming a VOCALOID melody.",
    "🎵 Don't count on it, like trying to hit extreme difficulty in Project DIVA.",
    "🎶 My reply is no, just like the absence of a certain VOCALOID.",
    "🎧 My sources say no, like a silent virtual singer.",
    "🎹 Outlook not so good, like a missed note in Project DIVA.",
    "🎤 Very doubtful, like the chance of seeing a live VOCALOID concert.",
  ]
  
  pregnant_girl_responses = [
    "👍 It is certain, mama-to-be! 🤰",
    "🎱 It is decidedly so, a beautiful journey awaits! 🌈",
    "🔮 Without a doubt, you're glowing with joy! ✨",
    "🌟 Yes, definitely! Your journey is unique and amazing! 🌈",
    "✨ You may rely on it, mama! Trust your instincts! 🌸",
    "💫 As I see it, yes! Embrace this magical chapter! 🌙",
    "👌 Most likely, darling! You've got this! 🌺",
    "🔍 Outlook good, mama! The future looks bright! 🌞",
    "🌈 Yes, absolutely! Your baby is a precious gift! 🌷",
    "🤞 Signs point to yes, mama! Exciting times lie ahead! 🌼",
    "🙌 Reply hazy, try again later, but trust your journey! 🌈",
    "⏳ Ask again later, as this is a time of change and growth! 🌸",
    "🤔 Better not tell you now, but trust your heart! ❤️",
    "🙃 Cannot predict now, but enjoy the surprises along the way! 🌟",
    "❌ Concentrate and ask again, trust your intuition! 💫",
    "😕 Don't count on it, but stay positive and hopeful! 🌈",
    "🚫 My reply is no, but don't lose hope, miracles happen! 🌺",
    "🔒 My sources say no, but remember, love conquers all! ❤️",
    "🙅‍♀️ Outlook not so good, but your strength will carry you through! 🌟",
    "❗ Very doubtful, but believe in your resilience, mama! 🌸"
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