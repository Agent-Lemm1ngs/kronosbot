import os
try:
  import aiohttp
except:
  os.system("pip install aiohttp")
  import aiohttp
try:
  
  from PIL import Image
except:
  os.system("pip install pillow")
  from PIL import Image
from io import BytesIO
import time,base64
from datetime import datetime
try:
  import asyncio
except:
  os.system(f'pip install asyncio')
import nextcord
from nextcord import SlashOption
from nextcord.ext import commands
import json,random
try:
  from better_profanity import profanity

except:
  os.system("pip install better_profanity")
  from better_profanity import profanity
try:
  import cooldowns
except:
  os.system("pip install function-cooldowns")
  import cooldowns
from emojis import *
class artSelections(nextcord.ui.Select):
  def __init__(self,images,optionStuff):
    select =[]
    for optio in optionStuff:
      select.append(nextcord.SelectOption(label=optio))
    self.images = images
    super().__init__(placeholder="Select an image",max_values=1,min_values=1,options=select)

  async def callback(self, interaction: nextcord.Interaction):
    file = self.values[0]
    file = self.images[int(file)]
    await interaction.edit(file=nextcord.File(file,"art.png"))

      
      

class artSelection(nextcord.ui.View):
    def __init__(self, *, timeout = None,options):
        super().__init__(timeout=timeout)
        self.add_item(artSelections(images=options,optionStuff=["1","2", "3", "4", "5", "6", "7", "8"]))
class artButtons(nextcord.ui.View):
  def __init__(self,*,timeout=None,data,user):
    super().__init__(timeout=timeout)
    self.imagething = data
    self.cooldown = 0
    self.user =user
  async def create_image(self,imageData,user,save):
    blank_image=Image.new("RGB",(800,800))
    img = Image.open(imageData)
    blank_image.paste(img.resize((800,800)),(0,0))
    blank_image.save(f"userImages/art/{user}{save}.png")
    return
  @nextcord.ui.button(label="1",style=nextcord.ButtonStyle.blurple)
  async def optionTwsdoLol(self,button,interaction):
    if interaction.user.id != self.user:
      return await interaction.send(f"{failed} Missing Access to this button.",ephemeral=True)
    if time.time() <self.cooldown:
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} You can use this button <t:{round(self.cooldown)}:R>",color=cRed),ephemeral=True)
    s =random.randint(1,5000)
    await self.create_image(self.imagething[0],interaction.user.id,s)
    
    await interaction.edit(embed=None,file=nextcord.File(f"userImages/art/{interaction.user.id}{s}.png","art.png"))
    os.remove(f"userImages/art/{interaction.user.id}{s}.png")
    self.cooldown = time.time() + 5
  @nextcord.ui.button(label="2",style=nextcord.ButtonStyle.blurple)
  async def optionTasdwsdoLol(self,button,interaction):
    if interaction.user.id != self.user:
      return await interaction.send(f"{failed} Missing Access to this button.",ephemeral=True)
    if time.time() <self.cooldown:
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} You can use this button <t:{round(self.cooldown)}:R>",color=cRed),ephemeral=True)
    s =random.randint(1,5000)
    await self.create_image(self.imagething[1],interaction.user.id,s)
    
    await interaction.edit(embed=None,file=nextcord.File(f"userImages/art/{interaction.user.id}{s}.png","art.png"))
    os.remove(f"userImages/art/{interaction.user.id}{s}.png")
    self.cooldown = time.time() + 5
  @nextcord.ui.button(label="3",style=nextcord.ButtonStyle.blurple)
  async def optionTwadssdoLol(self,button,interaction):
    if interaction.user.id != self.user:
      return await interaction.send(f"{failed} Missing Access to this button.",ephemeral=True)
    if time.time() <self.cooldown:
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} You can use this button <t:{round(self.cooldown)}:R>",color=cRed),ephemeral=True)
    s =random.randint(1,5000)
    await self.create_image(self.imagething[2],interaction.user.id,s)
    
    await interaction.edit(embed=None,file=nextcord.File(f"userImages/art/{interaction.user.id}{s}.png","art.png"))
    os.remove(f"userImages/art/{interaction.user.id}{s}.png")
    self.cooldown = time.time() + 5
  @nextcord.ui.button(label="4",style=nextcord.ButtonStyle.blurple)
  async def optionTwdssdoLol(self,button,interaction):
    if interaction.user.id != self.user:
      return await interaction.send(f"{failed} Missing Access to this button.",ephemeral=True)
    if time.time() <self.cooldown:
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} You can use this button <t:{round(self.cooldown)}:R>",color=cRed),ephemeral=True)
    s =random.randint(1,5000)
    await self.create_image(self.imagething[3],interaction.user.id,s)
    
    await interaction.edit(embed=None,file=nextcord.File(f"userImages/art/{interaction.user.id}{s}.png","art.png"))
    os.remove(f"userImages/art/{interaction.user.id}{s}.png")
    self.cooldown = time.time() + 5
  @nextcord.ui.button(label="All Images",style=nextcord.ButtonStyle.blurple)
  async def lmaowhatthehellisthis(self,button,interaction):
    if interaction.user.id != self.user:
      return await interaction.send(f"{failed} Missing Access to this button.",ephemeral=True)
    if time.time() <self.cooldown:
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} You can use this button <t:{round(self.cooldown)}:R>",color=cRed),ephemeral=True)   
    num = random.randint(1,31231231232)
    blank_image = Image.new("RGB", (800, 800))
    img1 = Image.open(self.imagething[0])
    img2 = Image.open(self.imagething[1])
    img3 = Image.open(self.imagething[2])
    img4 = Image.open(self.imagething[3])
    blank_image.paste(img1.resize((400,400)), (0,0))
    blank_image.paste(img2.resize((400,400)), (400,0))
    blank_image.paste(img3.resize((400,400)), (400,400))
    blank_image.paste(img4.resize((400,400)), (0,400))
    blank_image.save(f"userImages/art/{interaction.user.id}{num}.png")
    await interaction.edit(file=nextcord.File(f"userImages/art/{interaction.user.id}{num}.png","art.png"))
    os.remove(f"userImages/art/{interaction.user.id}{num}.png")   
    self.cooldown = time.time() + 5
class art(commands.Cog):
  
  def __init__(self,bot):
    self.bot=bot
  @nextcord.slash_command(description="Use AI to generate DIGITAL ART! Powered by Craiyon")
  @application_checks.check(check_blacklist)
  @cooldowns.cooldown(1, 65, bucket=cooldowns.SlashBucket.author)
  async def art(self,interaction,*,prompt:str=SlashOption(description="What you want the art to look like",required=True)):
    if profanity.contains_profanity(prompt):
      return await interaction.response.send_message(embed=nextcord.Embed(title=f"{failed} That looks like that contains profanity.",color=cRed))
    ETA = int(time.time() + 60)

    msg = await interaction.send(embed=nextcord.Embed(title=f"{loading} Generating art with prompt: `{prompt}`",description=f"ETA: <t:{ETA}:R>",color=cUnknown))
    async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={'prompt': prompt}) as response:
        # response = async with aiohttp.request("https://backend.craiyon.com/generate", json={'prompt': text})
        r = await response.json()
        images = r['images']
    imageThing=[]
    for i in images:
      image = BytesIO(base64.decodebytes(i.encode("utf-8")))
      imageThing.append(image)
    blank_image = Image.new("RGB", (800, 800))
    img1 = Image.open(imageThing[0])
    img2 = Image.open(imageThing[1])
    img3 = Image.open(imageThing[2])
    img4 = Image.open(imageThing[3])
    blank_image.paste(img1.resize((400,400)), (0,0))
    blank_image.paste(img2.resize((400,400)), (400,0))
    blank_image.paste(img3.resize((400,400)), (400,400))
    blank_image.paste(img4.resize((400,400)), (0,400))
    blank_image.save(f"userImages/art/{interaction.user.id}.png")

    await msg.edit(content=None,embed=nextcord.Embed(title=f"{success} Generated Your AI Art",color=cGreen),file=nextcord.File(f"userImages/art/{interaction.user.id}.png","art.png"),view=artButtons(data=imageThing,user=interaction.user.id,))
    os.remove(f"userImages/art/{interaction.user.id}.png")


def setup(bot):
  bot.add_cog(art(bot))





  
