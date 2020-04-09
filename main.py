import os
import discord
from getpass import getpass
from discord.ext import commands

#usrFile = open("usr", "r+")
#passwdFile = open("passwd", "r+")

#if '' == usrFile.read:
#    print ("What is your Instagram username?")
#    input(usr)

#class MyClient(discord.Client):

    # set-up the program
#    usr = input("What is your Instagram username?\n")
#    passwd = getpass("What is the password of your Instagram account?\n")

#    async def on_ready(self):
#        print('Logged on as', self.user)

#    async def on_message(self, message):
        # don't respond to ourselves
#        if message.author == self.user:
#            return

    #    if message.content == 'insta':
    #        os.system("instagram-scraper omarmwaseem -u " + self.usr + " -p " + self.passwd)
    #        await client.send_file(message.channel, "./omarmwaseem/82748276_855403461561603_6777149114328894202_n.jpg")

bot = commands.Bot(command_prefix='insta ')

usr_ = input("What is your Instagram username?\n")
passwd = getpass("What is the password of your Instagram account?\n")


@bot.event
async def on_ready():

    print(f'Logged in as {bot.user.name} on {len(bot.guilds)} server(s).')

# THIS WORKS
#@bot.command()
#async def test(ctx, arg):
#    await ctx.send("Processing your request... ")
#    await ctx.send(arg)
#    await ctx.send(file=discord.File('./omarmwaseem/82748276_855403461561603_6777149114328894202_n.jpg'))

@bot.command()
async def usr(ctx, arg):
    await ctx.send("Processing your request... ")
    print("Starting to fetch data... ")
    os.system("instagram-scraper " + arg + " -u " + usr_ + " -p " + passwd)
    print("Done.")

    await ctx.send(file=discord.File('./' + arg + '/' + os.listdir("./" + arg)[0]))

#client = MyClient()
bot.run('')
