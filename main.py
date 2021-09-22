#from discord import channel, message
from discord.ext import commands
from os.path import isfile
from json import dump
from requests import get
import time



bot = commands.Bot(">", self_bot = True)

dcToken = "" # YOUR DISCORD TOKEN HERE

version = "2"

channelToSendInID = ""
inOn = False

owoWait = 10
huntWait = 13
sellAllWait = 110
prayWait = 303
dailyWait = 86460

start_time_owo = 0
start_time_hunt = 0
start_time_daily = 0
start_time_pray = 0
start_time_sellall = 0

elapsed_time_owo = 0
elapsed_time_hunt = 0
elapsed_time_daily = 0
elapsed_time_pray = 0
elapsed_time_sellall = 0

firstTime = True

latestVersionPastebin = "https://pastebin.com/raw/MZ3PG9KB"

def versionChecker(version):
    latestVersion = get("https://pastebin.com/raw/MZ3PG9KB").text

    latestVersion = int(latestVersion)

    if (version == latestVersion):
        print(f"Version is Up To Date!\nYour program version: {version}\nLatest Version: {latestVersion}")
    if (version < latestVersion):
        print(f"Version is OUTDATED! Please Update The Program!\nYour program version: {version}\nLatest Version: {latestVersion}")
    if (version > latestVersion):
        print(f"You are using Beta Version Of The Program! Please Report Any bugs!\nYour program version: {version}\nLatest Version: {latestVersion}")



@bot.event
async def on_ready():
    print("OwOAutoGrinder is ON! Prefix is >")
    print("\nPlease! For the love of the god! Don't use it in dms. I am not putting safety shit here.")
    print("I will never do it. Use it as intended. This program isn't Dumb-Proof.")

    versionChecker(int(version))



@bot.command()
async def setchannel(ctx):
    await ctx.message.delete()

    global channelToSendInID

    channelToSendInID = ctx.channel.id
    
    f = open("owogrinder.json", "w")
    channelToSendInID = int(channelToSendInID)
    
    tempPyJson = {
        "token": dcToken,
        "channelId": channelToSendInID
    }

    dump(tempPyJson, f)
    f.close()

    print(f"Channel Set To: {channelToSendInID}")

    
@bot.command()
async def start(ctx):
    await ctx.message.delete()

    if (channelToSendInID == None):
        print("You didn't specify the channel to start the grinder in! Type >setchannel")
    else:
        global isOn
        isOn = True

        await grinder()



async def grinder():
    while (isOn):
        channelToSendIn = bot.get_channel(channelToSendInID)

        global start_time_owo
        global start_time_hunt
        global start_time_daily
        global start_time_pray
        global start_time_sellall

        global elapsed_time_owo
        global elapsed_time_hunt
        global elapsed_time_daily
        global elapsed_time_pray
        global elapsed_time_sellall

        global firstTime

        

        if (firstTime):
            time.sleep(2.937)
            await channelToSendIn.send("owo hunt")
            time.sleep(1.830)
            await channelToSendIn.send("owo")
            time.sleep(2.341)
            await channelToSendIn.send("owo daily")
            time.sleep(1.542)
            await channelToSendIn.send("owo pray")
            time.sleep(6.31)
            await channelToSendIn.send("owo sell all")
            time.sleep(3.238)
            
            firstTime = False

            start_time_owo = time.time()
            start_time_hunt = time.time()
            start_time_daily = time.time()
            start_time_pray = time.time()
            start_time_sellall = time.time()

        if (not firstTime):
            elapsed_time_hunt = time.time() - start_time_owo
            elapsed_time_hunt = time.time() - start_time_hunt
            elapsed_time_daily = time.time() - start_time_daily
            elapsed_time_pray = time.time() - start_time_pray
            elapsed_time_sellall = time.time() - start_time_sellall

            if (elapsed_time_hunt > huntWait):
                time.sleep(2)
                await channelToSendIn.send("owo hunt")
                start_time_hunt = time.time()
            if (elapsed_time_owo > owoWait)
                time.sleep(2)
                await channelToSendIn.send("owo")
                start_time_owo = time.time()
            if (elapsed_time_daily > dailyWait):
                time.sleep(2)
                await channelToSendIn.send("owo daily")
                start_time_daily = time.time()
            if (elapsed_time_pray > prayWait):
                time.sleep(2)
                await channelToSendIn.send("owo pray")
                start_time_pray = time.time()
            if (elapsed_time_sellall > sellAllWait):
                time.sleep(2)
                await channelToSendIn.send("owo sell all")
                start_time_sellall = time.time()
        
        

bot.run(dcToken, bot=False)
