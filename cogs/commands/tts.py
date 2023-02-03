import discord
from discord.ext import commands
from gtts import gTTS
import os

class TTS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, *, message:str):
        tts = gTTS(message)
        tts.save("tts.mp3")
        voice = await ctx.author.voice.channel.connect()
        source = discord.FFmpegPCMAudio("tts.mp3")
        voice.play(source)
        await ctx.send(f"Playing TTS: {message}")
        os.remove("tts.mp3")
        await voice.disconnect()

def setup(bot):
    bot.add_cog(TTS(bot))
