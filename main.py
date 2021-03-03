import os
import discord
import config
from gilgabot import Gilgabot

def __main__():
    props = config.get_properties()
    gilgabot = Gilgabot()
    gilgabot.run(props.get('DISCORD', 'DISCORD.TOKEN'))
    

if __name__ == "__main__":
    __main__()