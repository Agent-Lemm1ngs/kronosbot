import os
imports = ["nextcord","asyncio","aiosqlite"]
try:
  import asyncio
except:
  os.system(f'pip install asyncio')
try:
  import aiosqlite
except:
  os.system(f'pip install aiosqlite')
try:
    import cooldowns
except:
    os.system("pip install function-cooldowns")
    import cooldowns
from cooldowns import SlashBucket    
import nextcord
from nextcord.ext import commands
import random
from nextcord import SlashOption
import time
from datetime import datetime
from emojis import *
class afk(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author.bot:
      return
    async with self.bot.afkDB.cursor() as cursor:
      await cursor.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?",(message.author.id,message.guild.id,))
      data = await cursor.fetchone()
      if data:
        await message.channel.send(f"{message.author.mention}, Welcome back! I've removed your AFK.")
        await cursor.execute("DELETE FROM afk WHERE user = ? AND guild = ?",(message.author.id,message.guild.id,))
      if message.mentions:
        for mention in message.mentions:
          await cursor.execute("SELECT reason,long FROM afk WHERE user = ? AND guild = ?",(mention.id,message.guild.id))
          data2 = await cursor.fetchone()
          if data2 and mention.id != message.author.id:
     
            await message.reply(f"{mention} is AFK! `{data2[0]}`{eLength} <t:{round(data2[1])}:F>(<t:{round(data2[1])}:R>)",delete_after=5)
    await self.bot.afkDB.commit()
            
  @commands.Cog.listener()
  async def on_ready(self):
    setattr(self.bot,"afkDB",await aiosqlite.connect("databases/afk.db"))
    await asyncio.sleep(3)
    async with self.bot.afkDB.cursor() as cursor:
      await cursor.execute("CREATE TABLE IF NOT EXISTS afk(user INTEGER, guild INTEGER, reason TEXT,long INT)")
    await self.bot.afkDB.commit()
    print ("AFK Database is ready!")
  @nextcord.slash_command(description="Set Your AFK to let others know!")
  @cooldowns.cooldown(1,30,bucket=cooldowns.SlashBucket.author)	
  async def afk(self,interaction,*,reason:str=SlashOption(description="What to tell Others - Your AFK Message",required=False)):
    if reason == None:
      reason ="No reason given."
    async with self.bot.afkDB.cursor() as cursor:
      await cursor.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?",(interaction.user.id,interaction.guild.id,))
      data = await cursor.fetchone()
      if data:
        if data[0] == reason:
          return await interaction.response.send_message(embed=nextcord.Embed(title=":x: You already afk!",color=nextcord.Color.red()))
        await cursor.execute("UPDATE afk SET reason = ? WHERE user = ? AND guild =?",(reason,interaction.user.id,interaction.guild.id,))
      else:
        await cursor.execute("INSERT INTO afk VALUES (?,?,?,?)",(interaction.user.id,interaction.guild.id,reason,time.time(),))
        await interaction.response.send_message(embed=nextcord.Embed(title=":white_check_mark: You are now AFK!",description="Reason: " + reason,color=nextcord.Color.green()))
    await self.bot.afkDB.commit()
def setup(bot):
  bot.add_cog(afk(bot))