#import random
import uwuify

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

async def text_to_owo(text, interaction):
  
    flags = uwuify.SMILEY | uwuify.YU | uwuify.STUTTER
    #""" Converts your text to OwO """
    #smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    #text = text.replace('L', 'W').replace('l', 'w')
    #text = text.replace('R', 'W').replace('r', 'w')

    #text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    #text = last_replace(text, '?', '? owo')
    #text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    #for v in vowels:
        #if 'n{}'.format(v) in text:
            #text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        #if 'N{}'.format(v) in text:
            #text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    await interaction.response.send_message(uwuify.uwu(text, flags=flags))