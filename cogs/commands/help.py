import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Astroz import Astroz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import json
from utils import help as vhelp


client = Astroz()







class HelpCommand(commands.HelpCommand):
  async def on_help_command_error(self, ctx, error):
    damn = [commands.CommandOnCooldown, 
           commands.CommandNotFound, discord.HTTPException, 
           commands.CommandInvokeError]
    if not type(error) in damn:
      await self.context.reply(f"Unknown Error Occurred\n{error.original}", mention_author=False)
    else:
      if type(error) == commands.CommandOnCooldown:
        return
      
        return await super().on_help_command_error(ctx, error)

  async def command_not_found(self, string: str) -> None:
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<a:wrong:1040661606310367303> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=0x00FFE4)
      await self.context.reply(embed=embed, mention_author=False)
    else:
      

      if string in ("oknchhfehheng3g", "oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Games")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      else:
        msg = f"Command `{string}` is not found...\n"
        cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
        mtchs = get_close_matches(string, cmds)
        if mtchs:
          for okaay, okay in enumerate(mtchs, start=1):
            msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
        embed1 = discord.Embed(color=0x00FFE4,title=f"Command `{string}` is not found...\n",description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
        embed1.set_footer(name="Made By K4MI ⸸#8166", icon_url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
        return embed1

  
  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(title="<a:wrong:1040661606310367303> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/painarmyop)", color=0x00FFE4)
      return await self.context.reply(embed=embed, mention_author=False)
    data = getConfig(self.context.guild.id)
    prefix = data["prefix"]
    perms = discord.Permissions.none()
    perms.read_messages = True
    perms.external_emojis = True
    perms.send_messages = True
    perms.manage_roles = True
    perms.manage_channels = True
    perms.ban_members = True
    perms.kick_members = True
    perms.manage_messages = True
    perms.embed_links = True
    perms.read_message_history = True
    perms.attach_files = True
    perms.add_reactions = True
    perms.administrator = True
    inv = discord.utils.oauth_url(self.context.bot.user.id, permissions=perms)
    embed = discord.Embed(title="Help Command Overview :",description=f"• Prefix for this server is `{prefix}`\n• Type `{prefix}help <command | module>` for more info.\n• [Invite]({inv}) | [Support](https://discord.gg/painarmyop) | Total `{len(set(self.context.bot.walk_commands()))}` Commands.",color=0x00FFE4)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
    embed.set_footer(text="Made By K4MI ⸸#8166", icon_url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
    embed.add_field(name="__**Main Module**__", value="""<:i_globe:1062677096482209872> `:` **General**\n<:astroz_music:1062676833449033748> `:` **Music**\n<:astroz_fun:1062676733788172328> `:` **Moderation**\n<:i_guardian:1062677128178573382> `:` **Security**\n<:icons_leave:1062680206822887434> `:` **Raidmode**\n<:text:1062677645164281936> `:` **Logging**\n<:i_join:1062677166648737842> `:` **Welcome**\n<:astroz_fun:1062676733788172328> `:` **Fun**\n<:Games:1062676604326780948> `:` **Games**\n<:automod:1061687057153523732> `:` **Extra**""", inline=True) 
    embed.set_author(name=self.context.author.name, icon_url=self.context.author.display_avatar.url)
    embed.timestamp = discord.utils.utcnow()

    view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2)
    await self.context.reply(embed=embed, mention_author=False, view=view)

    
  async def send_command_help(self, command):
    with open('blacklist.json', 'r') as f:
       data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
       embed = discord.Embed(title="<a:wrong:1040661606310367303> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/painarmyop)", color=0x00FFE4)
       await self.context.reply(embed=embed, mention_author=False)
    else:
       hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
       embed = discord.Embed( description=f"""```toml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""", color=0x00FFE4)
       alias = ' | '.join(command.aliases)
      
       embed.add_field(name="**Aliases**", value=f"{alias}" if command.aliases else "No Aliases", inline=False)
       embed.add_field(name="**Usage**", value=f"`{self.context.prefix}{command.signature}`\n")
       embed.set_author(name=f"{command.cog.qualified_name.title()}", icon_url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
       await self.context.reply(embed=embed, mention_author=False)

  def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

  def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'

  
  async def send_group_help(self, group):
    with open('blacklist.json', 'r') as f:
        idk = json.load(f)
    if str(self.context.author.id) in idk["ids"]:
        embed = discord.Embed(title="<a:wrong:1040661606310367303> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/painarmyop)", color=0x00FFE4)
        await self.context.reply(embed=embed, mention_author=False)
    else:
        await self.context.typing()
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]

        if not group.commands:
            return await self.send_command_help(group)

        embed = discord.Embed(color=0x00FFE4)

        embed.title = f""
        _help = group.help or "No description provided..."
        _cmds = "\n\n".join(f"<:arrow:1060839014724280320> `{c.qualified_name}`\n{c.short_doc}" for c in group.commands)

        embed.description = f"\n<...> Duty | [...] Optional\n\n{_cmds}"
        embed.set_footer(text="Made By K4MI ⸸#8166", icon_url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
        embed.set_author(name=f"{group.qualified_name} Commands", icon_url=self.context.author.display_avatar.url)

      
        if group.aliases:
            #embed.add_field(name="Aliases", value=", ".join(f"`{aliases}`" for aliases in group.aliases), inline=False)
             embed.timestamp = discord.utils.utcnow()
        await self.context.send(embed=embed)

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<a:wrong:1040661606310367303> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/painarmyop)",  color=0x00FFE4)
      return await self.context.reply(embed=embed, mention_author=False)
    await self.context.typing()
    embed = discord.Embed( color=0x00FFE4)
    embed.title = cog.qualified_name.title()
    #desc = "No Description Provided..." if not cog.description else cog.description
    embed.description = f"""\n<...> Duty | [...] Optional\n\n\n\n"""
    for cmd in cog.get_commands():
      if not cmd.hidden:
        _brief = cmd.short_doc if cmd.short_doc else "No Help Provided..."
     # otay = ', '.join(f"`<{param}>`" for param in cmd.clean_params)
      #params = [param for param in cmd.clean_params]
        embed.add_field(name=f"<:arrow:1060839014724280320> `{self.context.prefix}{cmd.name}`", value=f"{_brief}\n\n", inline=False)
    embed.timestamp = discord.utils.utcnow()
    embed.set_author(name=self.context.author, icon_url=self.context.author.display_avatar.url)
    embed.set_footer(text="Made By K4MI ⸸#8166", icon_url="https://cdn.discordapp.com/attachments/1046001142057934939/1062786768753147984/odin.png")
    await self.context.send(embed=embed)

class Help(Cog, name="help "):
  def __init__(self, client:Astroz):
    self._original_help_command = client.help_command
    attributes = {
            'name': "help",
            'aliases': ['h'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
            'help': 'Shows help about bot, a command or a category'
        }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command
