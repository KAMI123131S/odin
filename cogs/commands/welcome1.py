import discord
from discord.ext import commands


class hacker1111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:i_join:1062677166648737842>'
		      label = "Welcome"
		      description = "Shows the welcome commands."
		      return emoji, label, description

    @commands.group()
    async def __Welcome__(self, ctx: commands.Context):
        """`welcome` , `welcome enable` , `welcome  disable` , `welcome message` , `welcome channel` , `welcome test `"""