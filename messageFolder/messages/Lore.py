import discord

async def LoreExplained(interaction):
  loreEmbed = discord.Embed(title="Your pregnant girl Elise her lore explained", description="So your interesed in how i ever ended up in this first place. Maby you wanna know how i got transformed? Became pregnant? Or even how i met my boyfriend Elif? Then this the right place. Im gonna shortly explain how my lore works \n\n I also am gonna show in which order the lore is suppose to be going. So based on an evently timed based line. Think about like A started first then C then B and etc. So sit thight grab some popcorn and im gonna show you how i became the pregnant girl i am today.", color=0x249b8f)
  loreEmbed.set_image(url="https://media.discordapp.net/attachments/961512157726539847/1121769123425292379/LoreExplained.png?width=1205&height=677")
  loreEmbed.add_field(name="Lore Explained", value="It all started basically with a weird dream. But my lore can be found in <#1013382908926500894>. There you can find 5 threads. Each thread basically explains a bit of lore. \n There is the Dream lore where i got my transformations, How i met Elif, My sekai looks?, My own sekai and as last ofcourse the pregnancy? So that explains how my lore works and how i got transformed into the girl that i am today ", inline=False)
  loreEmbed.add_field(name="Thread system explained", value="Ever since i added more lore i decided to move it into a thread system. This to prevent an cognitive overload once you open elise-lore. So there are 5 threads which each their own piece of lore. As moment of typing im still in progress of writing lore for my boyfriends stroy and the pregnancy story. So keep an eye out for those. But if your interesed make sure to check any of the 5 threads in <#1013382908926500894>.", inline=False)
  loreEmbed.add_field(name="Order explained", value="Now ofcourse comes the question? Preggie girl Elise how is the order of your lore since they all stand through each other? Great question let me explain \n 1. Is the the girl with the mark *This is my dream where i got transformed* \n 2. Arcade sekai. *Not long after i got my transformation i also got my own sekai* \n 3. Is the Sekai dress *Since then i have traveld the sekais and got dresses based on the sekais know to you by project sekai* \n 4. Is meeting my boyfriend *He is such a sweetheart and has its own story* \n 5. As last ofcourse there is my own pregnanchy story", inline=False)
  loreEmbed.add_field(name="Updates", value="There is still a chance your preggie girl will give updates to her lore!. So make sure to keep an eye out on the threads. You might find a new update here and there ", inline=False)
  loreEmbed.set_footer(text="🎀 The pregnant girl her lore explained 🎀")
  await interaction.response.send_message(embed=loreEmbed)
