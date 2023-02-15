import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random
import json
import aiohttp,asyncio
from emojis import *
urls = ["funny","hotmemes","dank","hilarious","trending","meme"]
class Confirm(nextcord.ui.View):
    def __init__(self,author,urlThing,*,timeout=300):
      self.author=author
      super().__init__(timeout=timeout)
      self.add_item(nextcord.ui.Button(label="Link",emoji="🔗", url=urlThing))
    @nextcord.ui.button(label="Next", style=nextcord.ButtonStyle.success)
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      if self.author != interaction.user.id:
        return await interaction.send(f"{failed} Missing Access!",ephemeral=True)
      await interaction.response.defer()
      meme = meme = await self.get_meme()
      await interaction.edit(embed=meme[0],view=Confirm(interaction.user.id,meme[1]))
    async def get_meme(self):
      url="https://meme-api.com/gimme/" + random.choice(urls)
      nsfw=True
      while nsfw:
        async with aiohttp.ClientSession() as session:
          async with session.get(url) as resp:
            memeApi = json.loads(await resp.text())        
        if not memeApi["nsfw"]:
          url=memeApi["url"]
          title=memeApi["title"]
          author = memeApi["author"]
          ups=memeApi["ups"]
          link=memeApi["postLink"]
          nsfw =False
      embed=nextcord.Embed(title=title,color=cUnknown)
      embed.set_image(url=url)
      embed.set_footer(text=f"Meme by: {author} | {ups}👍 | Post: {link}")
      return embed,link
class memes(commands.Cog):

  def __init__(self, bot):
      self.bot = bot
  async def get_meme(self,url):
    nsfw=True
    while nsfw:
      async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
          memeApi = json.loads(await resp.text())
      if not memeApi["nsfw"]:
        url=memeApi["url"]
        title=memeApi["title"]
        author = memeApi["author"]
        ups=memeApi["ups"]
        link=memeApi["postLink"]
        nsfw =False
    embed=nextcord.Embed(title=title,color=cUnknown)
    embed.set_image(url=url)
    embed.set_footer(text=f"Meme by: {author} | {ups}👍")
    return embed,link
      
  @nextcord.slash_command(name="meme", description="Get some EPIC memes from the MEME world!",force_global=True)
  async def meme(self, interaction: nextcord.Interaction,subreddit=SlashOption(description="Choose a specific subreddit to generate memes from!",required=False,choices=urls)):
    await interaction.response.defer()
    if subreddit:
      
      memeURL = "https://meme-api.com/gimme/"+subreddit
    else:
      memeURL = "https://meme-api.com/gimme/"
    meme = await self.get_meme(memeURL)
    await interaction.send(embed=meme[0],view=Confirm(interaction.user.id,meme[1]))

def setup(bot):
    bot.add_cog(memes(bot))



