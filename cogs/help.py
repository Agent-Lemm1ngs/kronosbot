from emojis import *
import nextcord,json,os
from nextcord.ext import commands
from nextcord import SlashOption

class Select(nextcord.ui.Select):
    def __init__(self,id):
      allFiles = os.listdir("help")
      self.id = id
      options = [nextcord.SelectOption(label="Home",emoji="🏘️",description="Return to the Homepage")]
      for file in allFiles:
        if ".json" in file:
          with open(f"help/{file}","r") as f:
            data =json.load(f)
            data = data["INFODATA"]
          file =file.replace(".json","")
          options.append(nextcord.SelectOption(label=file.title(),emoji=data["emoji"],description=data["desc"]))
      
      super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def get_file_help_commands(self,modules):
      with open(f"help/{modules}.json", "r") as f:
        users = json.load(f)
      return users

    async def callback(self, interaction: nextcord.Interaction):
      if self.id != interaction.user.id:
        return await interaction.send(f"{failed} Missing Access!",ephemeral=True)
      await interaction.response.defer()
      if self.values[0].lower()=="home":
        embed=nextcord.Embed(title="🏘️ Home",description=f"Welcome to the Homepage, select a module below\n\n🇸・[Kronos HQ Support Server]({support})\n🇮・[Invite Kronos]({invite})",color=cUnknown)
        embed.set_thumbnail(interaction.client.user.avatar.url)
        return await interaction.edit(embed=embed)
      data = await self.get_file_help_commands(modules=self.values[0].lower())
      output = ""
  
      for i in data:
        if i != "INFODATA":
          id = data[i]["id"]
          desc = data[i]["description"]
        
          output=f"{output}</{i}:{id}>・{desc}\n"
        else:
          e =data[i]["desc"]
          emojiss=data[i]["emoji"]

      embed=nextcord.Embed(title=f"{emojiss}・{self.values[0]}",description=f"{output}",color=cUnknown)
      embed.set_thumbnail(interaction.client.user.avatar.url)
      embed.set_footer(text=e,icon_url=interaction.user.avatar.url)
      await interaction.edit(embed=embed)
class SelectView(nextcord.ui.View):
    def __init__(self,id):
        super().__init__(timeout=None)
        
        self.add_item(Select(id=id))


class helpCommandAddorDelete(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  #economyDB

  @nextcord.slash_command()
  async def admin(self,interaction):
    pass
  @admin.subcommand(description="Set Module Data")
  async def setmodule(self,interaction,module,emoji,description):
    if interaction.user.id not in owners:
      return await interaction.send(f"{failed} Missing Access!")
    if not os.path.exists(f"help/{module}.json"):
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} `{module.title()}` is not found.",color=cRed))
    with open(f"help/{module}.json","r") as f:
      data =json.load(f)

    data["INFODATA"]["desc"]=description
    data["INFODATA"]["emoji"]=emoji
    with open(f"help/{module}.json","w") as f:
      json.dump(data,f,indent=4)
    await interaction.send(embed=nextcord.Embed(title=f"{success} `{module.title()}` has been set.",color=cGreen))
  @nextcord.slash_command(description="Display the help panel")
  async def help(self,interaction):
    embed=nextcord.Embed(title="🏘️ Home",description=f"Welcome to the Homepage, select a module below\n\n🇸・[Kronos HQ Support Server]({support})\n🇮・[Invite Kronos]({invite})",color=cUnknown)
    embed.set_thumbnail(interaction.client.user.avatar.url)
    await interaction.send(embed=embed,view=SelectView(id=interaction.user.id))

  @admin.subcommand(description="Delete help command")
  async def deletecommand(self,interaction,cmd=SlashOption(description="The command to delete"),module=SlashOption(description="Which cateogry is it from?")):
    if interaction.user.id not in owners:
      return await interaction.send(f"{failed} Missing Access!")
    if not os.path.exists(f"help/{module}.json"):
      return await interaction.send(embed=nextcord.Embed(title=f"{failed} `{module.title()}` is not found.",color=cRed))
    data = await self.get_file_help_commands(modules=module)
    if cmd not in data:
      await interaction.send(embed=nextcord.Embed(title=f"{failed} `{cmd}` is not found.",color=cRed))
    del data[cmd]
    with open(f"help/{module}.json","w") as f:
      json.dump(data,f)
    await interaction.send(embed=nextcord.Embed(title=f"{success} `{cmd}` has been deleted.",color=cGreen))
  @admin.subcommand(description="Add a help command")
  async def addcomand(self,interaction,command=SlashOption(description="Commnd to add"),id=SlashOption(description="The ID of the slash command"),modules:str=SlashOption(description="Which category does this command go into?"),dsc=SlashOption(description="Description of the command",required=False)):
    if interaction.user.id not in owners:
      return await interaction.send(f"{failed} Missing Access!")
    if dsc==None:
      dsc ="*No Description Given Yet*"
    await self.add_command(command,int(id),dsc,modules)
    await interaction.send(embed=nextcord.Embed(title=f"{success} command added",color=cGreen))

  async def find_file(self,modules):
    if os.path.exists(f"help/{modules}.json"):
      return
    f = open(f"help/{modules}.json","w")
    data={}
    data["INFODATA"]={}
    data["INFODATA"]["desc"]="No description given"
    data["INFODATA"]["emoji"]="❓"
    json.dump(data,f,indent=4)

    return
      
  async def add_command(self,command,id,description,modules):
    await self.find_file(modules)
    commandss=await self.get_file_help_commands(modules)
    if command in commandss:
      commandss[command]["id"]=int(id)
      commandss[command]["description"]=description
    else:
      commandss[command] = {}
      commandss[command]["id"] = int(id)
      commandss[command]["description"] = description
    with open(f"help/{modules}.json", "w") as f:
      json.dump(commandss,f,indent=4)
    return
  async def get_file_help_commands(self,modules):
    with open(f"help/{modules}.json", "r") as f:
      users = json.load(f)
    return users

    


def setup(bot):
  bot.add_cog(helpCommandAddorDelete(bot))