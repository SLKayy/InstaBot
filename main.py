import os
import discord
from getpass import getpass
from discord.ext import commands
#from filetype import filetype

bot = commands.Bot(command_prefix='insta ')

usr_ = input("What is your Instagram username?\n")
passwd = getpass("What is the password of your Instagram account?\n")


@bot.event
async def on_ready():

    print(f'Logged in as {bot.user.name} on {len(bot.guilds)} server(s).')

@bot.command()
async def usr(ctx, arg):
    await ctx.send("Processing your request... ")
    print("Starting to fetch data... ")
    os.system("instagram-scraper " + arg + " -u " + usr_ + " -p " + passwd)
    print("Done.")
    i = 0
    repeat = True
    while(repeat == True):
        try:
            await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
            repeat = False
        except:
            i = i + 1
            try:
                await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
                repeat = False
            except:
                i = i + 1
                await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
                repeat = True

@bot.command()
async def N(ctx, arg):
    i = i + 1
    repeat = True
    while(repeat == True):
        try:
            await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
            repeat = False
        except:
            i = i + 1
            try:
                await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
                repeat = False
            except:
                i = i + 1
                await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[i]))
                repeat = True

#@bot.command()
#async def usr(ctx, arg):
#    await ctx.send("Processing your request... ")
#    print("Starting to fetch data... ")
#    #os.system("instagram-scraper " + arg + " -u " + usr_ + " -p " + passwd)
#    print("Done.")
#    print(os.listdir("./" + arg)[0])
#    kind = filetype.guess('./' + arg + '/' + os.listdir("./" + arg)[0])
#    #print(kind.extension)
#    print('File extension: %s' % kind.extension)
#    if kind is not image/jpeg:
#        pass;
#    await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[0]))



#client = MyClient()
bot.run('Njk3NjUxMzc3NjY0NTU3MTA4.Xo6YhA.hUmgnBJggnhWszkl5zXEgf5Irpw')
