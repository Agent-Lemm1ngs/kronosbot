from nextcord.ext import commands
import nextcord
from emojis import *
import json
import aiohttp
from nextcord import SlashOption


class sudo(commands.Cog):
  def __init__(self,bot):
    self.bot   = bot
  @nextcord.slash_command(description="Pretend to be someone!")
  async def sudo(self,interaction,person:nextcord.Member=SlashOption(name="user",description="The user to sudo"),content=SlashOption(description="The message")):
    await interaction.response.defer(ephemeral=True)
    data = await interaction.channel.create_webhook(name=person.name,avatar=person.avatar,)
    async with aiohttp.ClientSession() as session:
      webhook = nextcord.Webhook.from_url(data.url, session=session)
      allowed = nextcord.AllowedMentions.none()
      await webhook.send(content,allowed_mentions=allowed)
    await data.delete()
    await interaction.send(f"{success} Sudoed <@{person.id}>!",ephemeral=True)
def setup(bot):
    bot.add_cog(sudo(bot))