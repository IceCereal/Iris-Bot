"""2018-May-24 09:55
Maid-Sama
Name given by:
Alex Rothschild#6666
"""

import discord
from discord.ext import commands
import asyncio
import ast

from os import listdir
from os.path import isfile, join

import sys, traceback

BOT_PREFIX = ('++')
bot = commands.Bot(command_prefix=BOT_PREFIX)

"""cogs_dir = " "

#Load Extensions
if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except:
            print ("FAIL#3 bot.load_extension(...)")
            traceback.print_exc()
"""
@bot.command(name="testo", hidden=True)
async def testo(ctx,  *args):
    print ("Testing Function")

"""OnReady_________"""
@bot.event
async def on_ready():
    print ("\nLogged in as:\t" + str(bot.user.name))
    print ("-----------------")

    try:
        await bot.change_presence(activity=discord.Game(name="my masters chores"))
    except:
        print ("FAIL#MS02 bot.change_presence(...)")

try:
    bot.run(TOKEN)
except:
    print ("FAIL#MS01 bot.run(TOKEN)")
