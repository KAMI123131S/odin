import os
import requests
import subprocess
from core.Astroz import Astroz
import asyncio, time, aiohttp, json
import jishaku, cogs
import psutil
import discord
from discord.ext import commands
from discord import app_commands
import traceback
import subprocess


os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client = Astroz()
tree = client.tree


class Embed(discord.ui.Modal, title='Embed Configuration'):
  tit = discord.ui.TextInput(
    label='Embed Title',
    placeholder='Embed title here',
  )

  description = discord.ui.TextInput(
    label='Embed Description',
    style=discord.TextStyle.long,
    placeholder='Embed description optional',
    required=False,
    max_length=400,
  )

  thumbnail = discord.ui.TextInput(
    label='Embed Thumbnail',
    placeholder='Embed thumbnail here optional',
    required=False,
  )

  img = discord.ui.TextInput(
    label='Embed Image',
    placeholder='Embed image here optional',
    required=False,
  )

  footer = discord.ui.TextInput(
    label='Embed footer',
    placeholder='Embed footer here optional',
    required=False,
  )

  async def on_submit(self, interaction: discord.Interaction):
    embed = discord.Embed(title=self.tit.value,
                          description=self.description.value,
                          color=0x00FFE4)
    if not self.thumbnail.value is None:
      embed.set_thumbnail(url=self.thumbnail.value)
    if not self.img.value is None:
      embed.set_image(url=self.img.value)
    if not self.footer.value is None:
      embed.set_footer(text=self.footer.value)
    await interaction.response.send_message(embed=embed)

  async def on_error(self, interaction: discord.Interaction,
                     error: Exception) -> None:
    await interaction.response.send_message('Oops! Something went wrong.',
                                            ephemeral=True)

    traceback.print_tb(error.__traceback__)


@tree.command(name="embed", description="Create A Embed Using Odin")
async def _embed(interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(Embed())


########################################


async def protect_vanity(guildid):
  start = time.perf_counter()
  with open('vanity.json') as idk:
    code = json.load(idk)
    if code[str(guildid)] != "":
      header = {
        "Authorization":
        "Bot MTA0OTMyODIzMTQzNTczMDk0NA.GPa5-e.8PnXpRAzKk77GIunqRal1GcaT2XwS0ZeogJ3g4",
        "X-Audit-Log-Reason": "Odin Security | Anti Vanity"
      }
      async with aiohttp.ClientSession(headers=header) as session:
        jsonn = {"code": code[str(guildid)]}
        async with session.patch(
            f"https://ptb.discord.com/api/v10/guilds/{guildid}/vanity-url",
            json=jsonn) as response:
          end = time.perf_counter()
          print(f"{end - start} | {response.status}")
    else:
      return

@client.event
async def on_command_completion(context) -> None:

    full_command_name = context.command.qualified_name
    split = full_command_name.split(",  ")
    executed_command = str(split[0])
    me = client.get_channel(1063497902820958299) 
    if context.guild is not None:
        await me.send(
            f"Executed `{executed_command}` command in `{context.guild.name}`  by `{context.author}`")
    else:
        await me.send(
            f"Executed `{executed_command}` command by `{context.author}` (ID: `{context.author.id}`) in DMs")

  
@client.listen("on_guild_update")
async def on_vanity_update(before, after):
  with open("vanity.json", "r") as f:
    data = json.load(f)
  if before.vanity_url_code != after.vanity_url_code:
    await asyncio.gather(*[
      asyncio.gather(*[
        asyncio.gather(*[
          asyncio.gather(*[
            asyncio.gather(*[
              asyncio.gather(*[
                asyncio.gather(*[
                  asyncio.gather(*[
                    asyncio.gather(*[
                      asyncio.gather(*[
                        asyncio.gather(
                          *[asyncio.gather(*[protect_vanity(before.id)])])
                      ])
                    ])
                  ])
                ])
              ])
            ])
          ])
        ])
      ])
    ])
  else:
    return


@client.event
async def on_ready():
  print("Loaded & Online!")
  print(f"Logged in as: {client.user}")
  print(f"Connected to: {len(client.guilds)} guilds")
  print(f"Connected to: {len(client.users)} users")
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)


@client.event
async def on_member_join(member):
  embed = discord.Embed(
    title="Do you own a server?",
    description=
    f"Odin offers  the fastest server protection available, with a powerful **anti-nuke**, **anti-spam**, **anti-link**, **Moderation**, **Logging** and time passing thing **Games**, i can protect your server in multiple ways today.\n\nThat's why **{member.guild.name}** and **{len(client.guilds)}** other servers use me to protect themselves! also join our support server for more help : discord.gg/painarmyop"
  )
  embed.set_thumbnail(url=member.avatar)
  embed.set_footer(text="Made By K4MI ⸸#8166",
                   icon_url=client.user.avatar.url)
  embed.set_author(name="Odin", icon_url=client.user.avatar.url)
  await member.send(
    f"- Sent From {member.guild.name}\nhttps://discord.gg/painarmyop",
    embed=embed,
    mention_author=True)


#import os
#os.system("pip install flask")
from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def home():
  return "Odin Security"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()


keep_alive()

@client.event
async def on_command_error(context, error):
  if isinstance(error, discord.errors.Forbidden):
    # Check if the error is a rate limit error
    if str(error).startswith("403 Forbidden (error code: 50013)"):
      # Run the shell command to execute "kill 1" in shell replit
      subprocess.run(["kill", "1"])
  else:
    # Handle other errors as you normally would
    pass


async def main():
  async with client:
    os.system("clear")
    await client.load_extension("cogs")
    await client.load_extension("jishaku")
    await client.start("MTA0MDE5NDk0ODQ5NjEwOTU2OQ.G0PZoo.FL6it1CYue3nEq-O4xdgecaZuwPfRpB_yizids")


if __name__ == "__main__":
  asyncio.run(main())
