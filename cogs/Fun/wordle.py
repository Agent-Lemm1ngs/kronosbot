from emojis import *
import random
from nextcord.ext import commands
class wordleGuess(nextcord.ui.Modal):
  def __init__(self,data,word,stage):
    super().__init__(
          "Wordle Guess",
          timeout=5 * 60,  # 5 minutes
      )
    self.val = nextcord.ui.TextInput(
      label=f"Guess word",
      min_length=5,
      max_length=5,
      required=True,
    
    )
    self.add_item(self.val)
    self.data,self.word,self.stage = data,word,stage

  async def callback(self, interaction: nextcord.Interaction) -> None:
    if len(self.val.value)!=5:
      return await interaction.send(f"{failed} Guess must be 5 characters")
    
    guessData = list(self.val.value.lower())
    

    self.data.append(guessData)
    if self.val.value.lower() == self.word:
      em=nextcord.Embed(title=f"{success} You guessed the word correctly! It was `{self.word}`",color=cGreen)
    elif self.stage + 1 == 5:
      em=nextcord.Embed(title=f"You failed! The word was `{self.word}`",color=cRed)
    else:
      em=nextcord.Embed(title="Guess the `5 letter word` that I'm thinking of!\n🟥・Found in the word, but not in that place\n🟩・Found in the word, in that place\n<:kronos_wordle_grey:1065732816677118012>・Not found in the word at all",color=cUnknown)
      
    await interaction.message.edit(embed=em,view=wordleButtons(self.data,self.word,self.stage+1,self.val.value.lower()==self.word,interaction.user.id))
    
class wordleButtons(nextcord.ui.View):

  def __init__(self,data,word,stage,done,id):
    super().__init__(timeout=None)
    self.add_buttons(stage,data,word,done,id)

  def add_buttons(self,stage,data,word,done,id):
    def make_button(data,word):
      wordleData = list(word)
      guessData=data
      output=[]
      choices = [nextcord.ButtonStyle.success,nextcord.ButtonStyle.danger,nextcord.ButtonStyle.gray]
      for i in range(len(guessData)):
        if guessData[i] == wordleData[i]:
          output.append(choices[0])
        elif guessData[i] in wordleData:
          output.append(choices[1])
        else:
          output.append(choices[2])
      return output
    if stage==0:
      data=[]
    async def test(interaction):
      if interaction.user.id != id:
        return await interaction.send(f"{failed} Missing Access!",ephemeral=True)
      await interaction.response.send_modal(wordleGuess(data,word,stage))
    choices = [nextcord.ButtonStyle.success,nextcord.ButtonStyle.danger,nextcord.ButtonStyle.gray]
    
    
    if stage>=1:
      datas=data[0]
      datass = make_button(datas,word)
      letter1,letter2,letter3,letter4,letter5=datas[0],datas[1],datas[2],datas[3],datas[4]
      self.add_item(nextcord.ui.Button(style=datass[0],label=letter1,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[1],label=letter2,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[2],label=letter3,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[3],label=letter4,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[4],label=letter5,disabled=True))

      
    if stage>=2:
      datas=data[1]
      datass = make_button(datas,word)
      letter1,letter2,letter3,letter4,letter5=datas[0],datas[1],datas[2],datas[3],datas[4]
      self.add_item(nextcord.ui.Button(style=datass[0],label=letter1,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[1],label=letter2,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[2],label=letter3,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[3],label=letter4,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[4],label=letter5,disabled=True))
    if stage>=3:
      datas=data[2]
      datass = make_button(datas,word)
      letter1,letter2,letter3,letter4,letter5=datas[0],datas[1],datas[2],datas[3],datas[4]
      self.add_item(nextcord.ui.Button(style=datass[0],label=letter1,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[1],label=letter2,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[2],label=letter3,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[3],label=letter4,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[4],label=letter5,disabled=True))
    if stage>=4:
      datas=data[3]
      datass = make_button(datas,word)
      letter1,letter2,letter3,letter4,letter5=datas[0],datas[1],datas[2],datas[3],datas[4]
      self.add_item(nextcord.ui.Button(style=datass[0],label=letter1,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[1],label=letter2,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[2],label=letter3,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[3],label=letter4,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[4],label=letter5,disabled=True))
    if stage==5:
      datas=data[4]
      datass = make_button(datas,word)
      letter1,letter2,letter3,letter4,letter5=datas[0],datas[1],datas[2],datas[3],datas[4]
      self.add_item(nextcord.ui.Button(style=datass[0],label=letter1,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[1],label=letter2,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[2],label=letter3,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[3],label=letter4,disabled=True))
      self.add_item(nextcord.ui.Button(style=datass[4],label=letter5,disabled=True))
    if stage!=5 and not done:
      guess=nextcord.ui.Button(style=nextcord.ButtonStyle.blurple,label="Guess")
      guess.callback=test
      self.add_item(guess)

class wordle(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @nextcord.slash_command(description="Try the FAMOUS word game from Discord!")
  async def wordle(self,interaction):
    with open("databases/words.txt","r") as f:
      words =[]
      for word in f:
        words.append(word)

    em=nextcord.Embed(title="Guess the `5 letter word` that I'm thinking of!\n🟥・Found in the word, but not in that place\n🟩・Found in the word, in that place\n<:kronos_wordle_grey:1065732816677118012>・Not found in the word at all",color=cUnknown)
    word=random.choice(words).lower().replace("\n","")
    await interaction.send(embed=em,view=wordleButtons(None,word,0,False,interaction.user.id))
    


def setup(bot):
  bot.add_cog(wordle(bot))