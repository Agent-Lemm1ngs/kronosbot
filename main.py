import os
try:
  import nextcord
except:
  os.system("pip install nextcord")
  import nextcord
from nextcord.ext import commands
from emojis import *
try:
  import cooldowns
except:
  os.system("pip install function-cooldowns")
  import cooldowns
from cooldowns import CallableOnCooldown
import time
import asyncio
bot = commands.Bot(command_prefix="+",intents=nextcord.Intents.all())
bot.remove_command("help")
token = "REPLACE THIS WITH YOUR TOKEN"
from nextcord.ext import application_checks, commands
from nextcord.ext.application_checks import *

@bot.event
async def on_application_command_error(interaction: nextcord.Interaction, error):
  print(error)
  try:
    error = getattr(error, "original", error)
  
    if isinstance(error, CallableOnCooldown):
      date = time.time()
      return await interaction.send(embed=nextcord.Embed(title=f"{lock} You can use this command <t:{round(date + error.retry_after)}:R>",color=cRed))

    elif isinstance(error,nextcord.Forbidden):
      return
    elif isinstance(error,nextcord.NotFound):
      return
    elif isinstance(error,nextcord.InteractionResponded):
      return
    elif isinstance(error,nextcord.InvalidArgument):
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} Invalid argument...",color=cRed))
    elif isinstance(error,application_checks.errors.ApplicationMissingPermissions):
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} {error}",color=cRed))
    elif isinstance(error,application_checks.errors.ApplicationBotMissingPermissions):
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} {error} {missing_permissions}",color=cRed))
    elif isinstance(error,nextcord.errors.ApplicationCheckFailure):
      with open("databases/blacklist.txt","r") as f:
        data = f.read()
      if "BLACKLIST" in data:
        bEmbed = nextcord.Embed(title=f"{failed} Missing Access",description=f"{lock} Commands are currently locked.\n{unknown} If this affects you, please [Join The Support Server]({support})",color=cRed)
      else:
        bEmbed = nextcord.Embed(title=f"{failed} Blacklisted",description=f"You are blacklisted from using `Kronos Bot`\n{unknown} If you think this was a mistake, [Join The Support Server]({support})",color=cRed)
      bEmbed.set_thumbnail(url=interaction.user.avatar.url)
      return await interaction.response.send_message(embed=bEmbed)
    else:
      if interaction.user.id in owners:
        return await interaction.send(f"{error}")
      id = (interaction.application_command).command_ids
      id = id[None]
      command = interaction.client.get_application_command(id)
      commands = f"</{command.name}:{id}>"        
      channel = bot.get_channel(1038818566562132099)
      await channel.send(embed=nextcord.Embed(title=f"{failed} Error found by `{interaction.user} ({interaction.user.id})`",description=f"Command: `{command.name}`{commands}\nServer: `{interaction.guild} ({interaction.guild.id}`\nChannel: `{interaction.channel} ({interaction.channel.id})`\n{failed} Error:\n```py\n{error}```",color=cRed))
      await interaction.send(embed=nextcord.Embed(title=f"{failed} Whoops! Looks like I've encountered an error!",description="This error has been logged and will be fixed ASAP",color=cRed),ephemeral=True)
      raise error
  except Exception as e:
    print(e)
@bot.slash_command(name="ping",description="Get the bot's ping!",force_global=True)
async def ping(interaction: nextcord.Interaction):
  myMessage = nextcord.Embed(title=f"{success} Bot ping: {round(bot.latency*1000)}ms🎈",color=nextcord.Color.purple())
  await interaction.send(embed=myMessage)    
@bot.event
async def on_dbl_vote(data):
    print(data)

@bot.event
async def on_ready():
  print("Bot IS UP!")
bot.load_extension(name="cogs.owner")
@bot.message_command(name="asads")
async def asdasdas(inter):
  await inter.send("hi")
@bot.event
async def on_command_error(ctx,error):
  if isinstance(error, (commands.CommandNotFound, nextcord.HTTPException)):
  	return    
  if ctx.author.id in owners:
    return await ctx.send(error)
  channel = bot.get_channel(1038818566562132099)
  await channel.send(embed=nextcord.Embed(title=f"{failed} Error found by `{ctx.author} ({ctx.author.id})`",description=f"Command: `{ctx.command}`\nServer: `{ctx.guild} ({ctx.guild.id}`\nChannel: `{ctx.channel} ({ctx.channel.id})`\n{failed} Error:\n```py\n{error}```",color=cRed))
  await ctx.message.reply(embed=nextcord.Embed(title=f"{failed} Whoops! Looks like I've encountered an error!",description="This error has been logged and will be fixed ASAP",color=cRed))
amount = 0
win = 0
for cog in cogs:
  amount = amount + 1
  try:
    bot.load_extension(f"cogs.{cog}")
    length = len(cog)
    number = 30-length
    output = ""
    while number != 0:
      output = output + " "
      number = number - 1
    print (cog + output + "Status: ✅" )
    win = win + 1
  except Exception as e:
    length = len(cog)
    number = 30-length
    output = ""
    while number != 0:
      output = output + "-"
      number = number - 1
    print (cog + output + f"Status: ❌\n❌ Error Output: {e}")

print ('------------------------------------')
print (f"{win}/{amount} commands loaded succesfully!")
bot.run(token)

