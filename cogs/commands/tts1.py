import discord
from discord.ext import commands


class hacker111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Text-To-Speech commands"""
  
    def help_custom(self):
		      emoji = '<:voice:1062677678404161536>'
		      label = "Text-To-Speech"
		      description = "Shows the TTS Commands."
		      return emoji, label, description

    @commands.group()
    async def __tts__(self, ctx: commands.Context):
        """`tts <message>`"""