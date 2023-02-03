import discord
from discord.ext import commands


class hacker111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""
  
    def help_custom(self):
		      emoji = '<:Games:1062676604326780948>'
		      label = "Games"
		      description = "Shows the fun commands."
		      return emoji, label, description

    @commands.group()
    async def __Games__(self, ctx: commands.Context):
        """`akinator` , `chess` , `hangman` , `typerace` , `rps` , `reaction` , `tick-tack-toe` , `wordle` , `2048` , `memory-game` , `number-slider` , `battleship` , `country-guesser`"""