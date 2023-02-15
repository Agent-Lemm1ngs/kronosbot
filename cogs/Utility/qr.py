from nextcord.ext import commands
import nextcord
from emojis import *
import os
try:
  import qrcode
except:
  os.system("pip install qrcode[pil]")
  import qrcode
try:
  import PIL
except:
  os.system("pip install pillow")
  import PIL
from PIL import Image
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage
try:
  import cooldowns
except:
  os.system("pip install function-cooldowns")
  import cooldowns

from nextcord import SlashOption
from nextcord.ext import application_checks
async def generate(link,save):
  basewidth = 50
  logo = Image.open("images/krono.png")

  # adjust image size
  wpercent = (basewidth/float(logo.size[0]))
  hsize = int((float(logo.size[1])*float(wpercent)))
  logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

  qr = qrcode.QRCode(
          version=1,
          box_size=10,
          border=5)
  qr.add_data(link)
  qr.make(fit=True)
  img = qr.make_image(fill_color='blue', back_color='white',module_drawer=RoundedModuleDrawer())  

  type(img)
  pos = ((img.size[0] - logo.size[0]) // 2,
         (img.size[1] - logo.size[1]) // 2)
  img.paste(logo, pos)
   
  img.save(save)
  return
class qrcodes(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @nextcord.slash_command(description="Send a QR code so you don't forget anything or to share it easily!")
  @application_checks.check(check_blacklist)
  @cooldowns.cooldown(1, 15, bucket=cooldowns.SlashBucket.author)
  async def qrcode(self,interaction,link=SlashOption(description="What do you want the QR code to show? Links & Text Supported.")):
    await generate(link,f"{interaction.user.id}-qrcode.png")
    await interaction.response.send_message(file=nextcord.File(fr"{interaction.user.id}-qrcode.png","qrcode.png"))
    os.remove(f"{interaction.user.id}-qrcode.png")



def setup(bot):
    bot.add_cog(qrcodes(bot))
