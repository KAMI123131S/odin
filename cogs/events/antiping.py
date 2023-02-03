import os
import discord
from discord.ext import commands
import requests
import sys
from utils.Tools import getConfig, add_user_to_blacklist, getanti
import setuptools
from itertools import cycle
from collections import Counter
import threading
import datetime
import logging
from core import Astroz, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ui import View, Button
import json
from discord.ext import tasks
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antipinginv(Cog):
    def __init__(self, client: Astroz):
        self.client = client
        self.spam_control = commands.CooldownMapping.from_cooldown(10, 12.0, commands.BucketType.user)
        print("Cog Loaded: Antipinginv")

    @commands.Cog.listener()
    async def on_message(self, message):
      button = Button(label="Invite", url =  "https://discord.gg/painarmyop")
      button1 = Button(label="Support", url = "https://discord.gg/painarmyop")
      try:
       
        with open("blacklist.json", "r") as f:
          data2 = json.load(f)
          astroz = '<@1040194948496109569>'
          try:
            data = getConfig(message.guild.id)
            anti = getanti(message.guild.id)
            prefix = data["prefix"]
            wled = data["whitelisted"]
            punishment = data["punishment"]
          except Exception:
            pass
          guild = message.guild
          if message.mention_everyone:
            if str(message.author.id) in wled or anti == "off":
              pass
            else:
              if punishment == "ban":
                await message.guild.ban(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "kick":
                await message.guild.kick(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "none":
                return


          elif message.content == astroz or message.content == "<@!1040194948496109569>":
            if str(message.author.id) in data2["ids"]:
              embed = discord.Embed(title="<:wrong:1040661608919220415> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/painarmyop)")
              await message.reply(embed=embed, mention_author=False)
            else:

              embed = discord.Embed(description=f"""Hey, I'm **Odin**

Please use the following command instead: `{prefix}help`

If you continue to have problems, consider asking for help [PaiN ARMY](https://discord.gg/painarmyop)""",color=0x00FFE4) 
              view = View()
              view.add_item(button)
              view.add_item(button1)
              #view.add_item(button2)
              await message.reply(f"Hey {message.author.mention}",embed=embed, mention_author=True, view=view)
          else:
            return
      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return





