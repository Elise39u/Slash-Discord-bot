import json
import requests 
import re
import urllib
import urllib.request
from messageFolder.helpers.EmbedBuilder import BuildEmbed
import discord
import logging
from discord.ext import tasks
  
# Configure logging
logging.basicConfig(level=logging.ERROR)  # Set the logging level to ERROR

# Discord channel ID to send error messages
error_channel_id = 822837640872067082  # Replace with the actual channel ID

@tasks.loop(seconds=60)
async def checkforVideos(client):
  try:
    with open("youtube/youtubeJson.json", "r") as ytData:
      data=json.load(ytData)

      for youtube_channel in data:
        channel = f"https://www.youtube.com/channel/{youtube_channel}"
      
        #getting html of the /videos page
        html = requests.get(channel+"/videos").text
  
        #try to get the latetes video url
        #anwsers used from stackoverflow 
        #https://stackoverflow.com/questions/59627108/retrieve-youtube-video-title-using-api-python
        #https://github.com/AdvicSaha443/Discord.py-Youtube-Notification-Bot/blob/main/main.py
        #https://www.youtube.com/watch?v=qZ6kcQJxbzQ          #https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html
        #discord.ext.tasks.Loop.start
        
        try:
          latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
        except:
          continue
  
        if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
          
          #chaning the last video url
          data[str(youtube_channel)]["latest_video_url"] = latest_video_url
  
          #Dumping the new youtube lateste url into the json file
          with open("youtube/youtubeJson.json", "w") as ytJson:
            json.dump(data, ytJson)
  
          discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
          discord_channel = client.get_channel(int(discord_channel_id))
          
          vidId = re.search('(?<="videoId":").*?(?=")', html).group()
          parmas = {"format": "json", "url": latest_video_url}
          url = "https://www.youtube.com/oembed"
          query_string = urllib.parse.urlencode(parmas)
          url = url + "?" + query_string
          
          with urllib.request.urlopen(url) as response:
            response_text = response.read()
            youtubeVidData = json.loads(response_text.decode())
            vidTitle = get_vid_title(youtubeVidData)
            embedTitle, embedDescription = get_embed_details(youtubeVidData)
            await discord_channel.send(vidTitle)
            await BuildEmbed(None, embedTitle, embedDescription, "http://img.youtube.com/vi/" + vidId + "/0.jpg", None, "🎀 New Vid Upload 🎀", discord_channel, latest_video_url)
  except requests.RequestException as e:
        # Log HTTP request errors
        logging.error(f"Error during HTTP request: {e}")

        # Get the error channel
        error_channel = client.get_channel(error_channel_id)
        if error_channel:
            # Send the error message to the error channel  
            await error_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
            await error_channel.send(f"<@203095887264743424> Halp Mommy Elise. I found an error during the HTTP request: **{e}**")

  except discord.HTTPException as e:
        # Log Discord API errors
        logging.error(f"Error during Discord API usage: {e}")

        # Get the error channel
        error_channel = client.get_channel(error_channel_id)
        if error_channel:
            # Send the error message to the error channel  
            await error_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
            await error_channel.send(f"<@203095887264743424> Halp Mommy Elise. I found an error during Discord API usage: **{e}**")

  except json.JSONDecodeError as e:
        # Log JSON parsing errors
        logging.error(f"Error during JSON parsing: {e}")

        # Get the error channel
        error_channel = client.get_channel(error_channel_id)
        if error_channel:
            # Send the error message to the error channel  
            await error_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
            await error_channel.send(f"<@203095887264743424> Halp Mommy Elise. I found an error during JSON parsing: **{e}**")

  except Exception as e:
        # Log other general exceptions
        logging.error(f"Error during video checking: {e}")

        # Get the error channel
        error_channel = client.get_channel(error_channel_id)
        if error_channel:
            # Send the error message to the error channel  
            await error_channel.send("https://cdn.discordapp.com/attachments/709057115159003156/1109789108722741389/909558100162379877.gif")
            await error_channel.send(f"<@203095887264743424> Halp Mommy Elise. I found an error during video checking: **{e}**")

def get_vid_title(youtube_vid_data):
    title = youtube_vid_data["title"]
    if "Cover" in title:
        return " 🎀 <@&934500064364216390> <@203095887264743424> Uploaded a new English cover to her Channel 💜🎀"
    elif "EGS" in title:
        return " 🎀 <@&934500064364216390> <@203095887264743424> has uploaded a Gender story in the form of a project diva video 💜🎀"
    elif "Perfect" in title or "Divaroadmap" in title:
        return "<@&934500064364216390> <@203095887264743424> has uploaded a Project diva video, go check it out 💜"
    elif "Megamix" in title or "AFT" in title or "Diva" in title or "Future tone" in title:
        return " 🎀 <@&934500064364216390> <@203095887264743424> has uploaded a recent project diva stream to her vods channel 🎀"
    elif "Stream" in title:
        return " 🎀 <@&934500064364216390> <@203095887264743424> has uploaded a recent stream to her vods channel 🎀"
    else:
        return "<@&934500064364216390> <@203095887264743424> has uploaded a lets play video. Go check it out 💜"

def get_embed_details(youtube_vid_data):
    title = youtube_vid_data["title"]
    if "Cover" in title:
        return title, "🎀 You know that Miku tries to teach Elise to sing from time to time. How do we test if Elise can sing well a v-singer career? My sources tell me they practiced a Vocaloid song and gave it an English jacket. Care what Elise sung this time? Click the title of the embed and check it out 🎀"
    elif "EGS" in title:
        return title, "🎀 Elise would love to have an open community where you can discuss gender thoughts and preferences. She hopes to give courage to someone else by stepping up as the first to talk. See how Elise dealt with some stuff in her transgender life. Check it out by clicking on the title above 🎀"
    elif "Perfect" in title or "Divaroadmap" in title:
        return title, "🎀 Elise has uploaded a new project diva video. Care to see if she got a perfect or got a new divaroadmap? See what happens by checking the title of the embed 🎀"
    elif "Megamix" in title or "AFT" in title or "Diva" in title or "Future tone" in title:
        return title, "🎀 Elise recently streamed a project diva game on her Twitch. After downloading and maybe a little bit of editing, it's finally uploaded to her vods channel. Interested to see what happens in the stream? Click the title of the embed 🎀"
    elif "Stream" in title:
        return title, "🎀 Elise recently streamed something, but it's hard to tell what. Well, here's an upload, so after downloading and maybe a little bit of editing, it's finally uploaded to her vods channel. Interested to see what happens in the stream? Click the title of the embed 🎀"
    else:
        return title, "🎀 Elise has uploaded a new lets play video. Is it horror or a fun lets play video? Well, it's hard to tell, but there's a new upload. Care to check it out? Click on the title to watch the video. 🎀"