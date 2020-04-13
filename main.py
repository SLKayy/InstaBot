import os
import discord
from getpass import getpass
from discord.ext import commands

bot = commands.Bot(command_prefix='insta ')

usr_ = input("What is your Instagram username?\n")
passwd = getpass("What is the password of your Instagram account?\n")

i = 0

usrCmdArg = "omarmwaseem"

@bot.event
async def on_ready():

    print(f'Logged in as {bot.user.name} on {len(bot.guilds)} server(s).')

@bot.command()
async def usr(ctx, arg):
    global i
    global usrCmdArg
    usrCmdArg = arg
    await ctx.send("Processing your request... ")
    print("Starting to fetch data... ")
    if (os.path.isdir("./" + arg)):
        pass
    else:
        os.system("instagram-scraper " + arg + " -u " + usr_ + " -p " + passwd)
    print("Done.")
    repeat = True
    while(repeat == True):
        if str(os.listdir("./" + arg)[i]).endswith('.jpg'):
            await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
            repeat = False
        elif str(os.listdir("./" + arg)[i]).endswith('.mp4'):
            print("File is not of JPEG type, skipping... ")
            i = i + 1
            repeat = True
        else:
            print("Some other file type than *.mp4 and *.jpg is in this directory. Please post this in the \"Issues\" tab of ansarirayyan's InstaBot GitHub repo")
            i = i + 1
            repeat = True

@bot.command()
async def N(ctx, *arg):
    global i
    global usrCmdArg
    i = i + 1
    repeat = True
    while(repeat == True):
        if str(os.listdir("./" + usrCmdArg)[i]).endswith('.jpg'):
            await ctx.send(file=discord.File('./' + usrCmdArg + '/' + os.listdir("./" + usrCmdArg)[i]))
            repeat = False
        elif str(os.listdir("./" + usrCmdArg)[i]).endswith('.mp4'):
            print("File is not of JPEG type, skipping... ")
            i = i + 1
            repeat = True
        else:
            print("Some other file type than *.mp4 and *.jpg is in this directory. Please post this in the \"Issues\" tab of ansarirayyan's InstaBot GitHub repo")
            i = i + 1
            repeat = True

@bot.command()
async def tag(ctx, arg, maxNumb='10'):
    global i
    global usrCmdArg
    usrCmdArg = arg + "_tag"
    await ctx.send("Processing your request... ")
    print("Starting to fetch data... ")
    if (os.path.isdir("./" + arg + "_tag")):
        pass
    else:
        os.system("instagram-scraper " + arg + " --tag -m " + maxNumb)
        os.rename(arg, arg + "_tag") # just in case if there's a username with the same tag name
    print("Done.")
    repeat = True
    while(repeat == True):
        if str(os.listdir("./" + arg + "_tag")[i]).endswith('.jpg'):
            await ctx.send(file=discord.File('./' + arg + '_tag' + '/' + os.listdir("./" + arg + "_tag")[i]))
            repeat = False
        elif str(os.listdir("./" + arg + "_tag")[i]).endswith('.mp4'): # can videos be tagged?
            print("File is not of JPEG type, skipping... ")
            i = i + 1
            repeat = True
        else:
            print("Some other file type than *.mp4 and *.jpg is in this directory. Please post this in the \"Issues\" tab of ansarirayyan's InstaBot GitHub repo")
            i = i + 1
            repeat = True

@bot.command()
async def reload_usr(ctx, arg): # to get the latest posts
    os.system("instagram-scraper " + arg + " -u " + usr_ + " -p " + passwd)

@bot.command()
async def reload_tag(ctx, arg, maxNumb): # will this fetch the latest or the oldest? only time will tell
    os.system("instagram-scraper " + arg + " --tag -m " + maxNumb)
    os.rename(arg, arg + "_tag")

@bot.command()
async def ls(ctx, *arg):
    p = os.listdir("./")
    for i1 in p:
        if os.path.isdir(i1):
            if (i1 == ".git"):
                pass
            else:
                await ctx.send(i1)

bot.run('Njk3NjUxMzc3NjY0NTU3MTA4.XpNakg.PN5D44Apg1uK3-opJqmCKNtzXeo')
