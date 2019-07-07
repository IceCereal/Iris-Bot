"""
	Name: Iris
	Objective: A discord bot for administrative purposes
	Date: 2019-Jul-06

	Author: IceCereal
"""

import discord
from discord.ext import commands

from asyncio import sleep
from argparse import ArgumentParser

from pathlib import Path
import os

corePath = Path("core")
resPath = Path("res")
utilsPath = Path("utils")

parser = ArgumentParser()
parser.add_argument('-v', "--verbose", required=False, help="Run Iris.py with verbosity")

args = parser.parse_args()

if args.verbose == "True":
	args.verbose = True
else:
	args.verbose = None

if args.verbose:
	print ("Reading Token...")

with open(resPath / "TOKEN", 'r') as TokenObj:
	TOKEN = TokenObj.read()

BOT_PREFIX = ('++', 'i+', '+')
bot = commands.Bot(command_prefix=BOT_PREFIX)

# Set args to bot
bot.verbose = args.verbose

@bot.event
async def on_ready():
	print ("\nLogged in as:\t" + str(bot.user))
	print ("-----------------")

	await bot.change_presence(activity=discord.Game(name="The Game of Life"))

if __name__ == '__main__':

	# Load Extensions
	cogs_dir = corePath / "cogs"
	cogs_list = []

	for root, directories, files in os.walk(cogs_dir):
		for fileName in files:
			if '-cog' in fileName.lower() and fileName.endswith('.py'):
				cogs_list.append(str(os.path.join(root, fileName )))

	updated_cogs_list = []

	for cog in cogs_list:
		cog_new = str(cog)

		# Windows
		cog_new = cog_new.replace('\\', '.')

		# Linux/Mac
		cog_new = cog_new.replace('/', '.')

		cog_new = cog_new.replace(".py", "")

		updated_cogs_list.append(cog_new)

	cogs_list = updated_cogs_list

	for cog in cogs_list:
		print ("Loading Cog from Iris:\t", cog)

		bot.load_extension(cog)


	# RUN THE BOT
	bot.run(TOKEN)

	# Nothing should come after this. It will not be processed
	# This comment won't even be encountered, r/funnyandsad :/
