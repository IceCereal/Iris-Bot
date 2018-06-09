"""2018-May-24 09:55
Maid-Sama
Name given by:
Alex Rothschild#6666
"""

import discord
from discord.ext import commands

from os import listdir
from os.path import isfile, join

import sys, traceback

TOKEN = ""
BOT_PREFIX = ('++')
bot = commands.Bot(command_prefix=BOT_PREFIX)

"""cogs_dir = "MaidSamaFunctions"

#Load Extensions
if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except:
            print ("FAIL#3 bot.load_extension(...)")
            traceback.print_exc()
"""

"""Switch On"""
@bot.event
async def on_ready():
    print ("Logged in as:\t" + str(bot.user.name))
    print ("-----------------")

    try:
        await bot.change_presence(activity=discord.Game(name="my masters chores"))
    except:
        print ("FAIL#MS02 bot.change_presence(...)")


"""A Message that prints when a command invoker does not have enough permissions to invoke the command"""
@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You have no power here.")

try:
    bot.run(TOKEN)
except:
    print ("FAIL#MS01 bot.run(TOKEN)")
