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
            print("Some other file type than *.mp4 and *.jpg is in this directory. Please post this in the \"Issues\" tab of ")
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
            print("Some other file type than *.mp4 and *.jpg is in this directory. Please post this in the \"Issues\" tab of ")
            i = i + 1
            repeat = True

bot.run('')
