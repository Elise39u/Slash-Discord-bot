logging_channel_id = 822837640872067082

async def clapClapClap(interaction, sentence, client):
    try:
        if sentence is None:
            raise Exception("Dindt find a message")
        
        # Remove the !clapify command and get the remaining text
        clapSentence = ' '.join(sentence.split()[1:])
    
        # Split the sentence into words and join them with clap emojis
        clapified_sentence = ' 👏 '.join(clapSentence.split())
    
        # Send the clapified sentence as a reply
        await interaction.response.send_message(clapified_sentence)
    except Exception as e:
      channel = client.get_channel(logging_channel_id)
      await channel.send(f"<@203095887264743424> Mommy MOMMY HALP. I had an error with the clap command: {e}")