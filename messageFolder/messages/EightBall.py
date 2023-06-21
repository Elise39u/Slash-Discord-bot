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
        "🌟 It is certain that your journey as a pregnant trans girl will bring joy and fulfillment. ✨",
        "🌈 Without a doubt, being a pregnant trans girl will open up new avenues of self-discovery. 🌱",
        "🎨 Reply hazy, but your creativity in content creation during this phase will shine through. 🖌️",
        "🎵 Cannot predict now, but your project diva skills will continue to captivate your audience. 🎶",
        "🌺 Don't count on it, focus on self-care during your pregnancy as a trans girl. 🌿",
        "💔 My sources say no, take some time off from content creation to prioritize your well-being. 🛀",
        "💫 Signs point to yes, your unique perspective as a pregnant trans girl will resonate with many. 💖",
        "⏳ Ask again later, for now, enjoy playing Project Diva and nurturing yourself. 🎮",
        "💡 Outlook good, use this time as a pregnant trans girl to explore new content creation ideas. 🌟",
        "🌙 Better not tell you now, but your passion for Project Diva will continue to inspire you. 🎵",
        "🌟 Most likely, your experiences as a pregnant trans girl will lead to personal growth and success. 💪",
        "🌈 It is decidedly so, embrace your journey and let it influence your creative projects. 🌟",
        "🌸 Yes, definitely! Let your identity as a pregnant trans girl shine in your content creation. 🌈",
        "❌ My reply is no, take a break from Project Diva and focus on self-reflection. 🧘",
        "🌟 You may rely on it, your path as a pregnant trans girl will be filled with opportunities. 🌟",
        "⏰ Ask again later, but don't forget to express yourself authentically in your projects. 📝",
        "❗ Outlook not so good, take some time off from content creation to rest and recharge. 🌙",
        "💖 Signs point to a fruitful journey as a pregnant trans girl, incorporating Project Diva along the way. 🌸",
        "🎯 Concentrate and ask again, find balance between your pregnancy and content creation endeavors. ✨",
        "🌈 Yes, definitely! Your passion for Project Diva will fuel your creative output during this phase. 🎶"
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