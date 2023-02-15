import nextcord
from nextcord.ext import application_checks
from nextcord import SlashOption
cUnknown = 3092790#10066329

cGreen = 51209
cRed = 14354440
owners = [REPLACE THIS WITH YOUR USERIDS]
cogs = ["Utility.qr","Utility.reaction","eval","Moderation.nuke","Moderation.kick","Fun.art","Utility.tickets","Utility.help","votes","e","giveaways","Utility.afk","Fun.sudo","Utility.logs","Fun.meme","Fun.wordle","Utility.points"]
support = "https://discord.gg/JccSNuYPcR"
invite = "https://discord.com/api/oauth2/authorize?client_id=1038808244375785483&permissions=2048161999991&scope=bot%20applications.commands"
#status

failed = "<:kronos_no:1044339059604074576>" 
unknown = "<:kronos_unknown:1044339339007623328>" 
success = "<:kronos_yes:1044339061340508270>"
iLoading = "<a:kronos_idle:1038825280732680273>"
loading = "<a:kronos_loading:1038825245261430896>"
offline = "<a:kronos_offline:1038825186117562428>"
online = "<a:kronos_online:1038825215834210444>"
eWinners = "<:kronos_winner:1044337813698650134>"
#customization
sparkles = "<:kronos_sparkles:1038836949038932058>"
lock =  "<:kronos_lock:1044335500871344208>"
dot = "<:kronos_coin:1045055692597383278> "
members = "<:kronos_members:1043988618273882163>"
eLength = "<:kronos_length:1044335271170277446>"

#checks


def check_blacklist(interaction):
  with open("databases/blacklist.txt","r") as f:
    text = f.read()
  if interaction.user.id in owners:
    return True
  if "BLACKLIST" in text:
    return False
  if str(interaction.user.id) in text:
    return False
  else:
    return True

async def convert(date):
    pos = ["s", "m", "h", "d"]
    time_dic = {"s": 1, "m": 60, "h": 3600, "d": 3600 *24}
    i = {"s": "Seconds", "m": "Minutes", "h": "Hours", "d": "Days"}
    unit = date[-1]
    if unit not in pos:
        return -1
    try:
        val = int(date[:-1])

    except:
        return -2

    if val == 1:
        return val * time_dic[unit], i[unit][:-1]
    else:
        return val * time_dic[unit], i[unit]

