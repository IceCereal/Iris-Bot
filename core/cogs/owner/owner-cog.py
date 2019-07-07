"""
	A Cog for the Bot Owner

	Author: IceCereal
"""

import discord
from discord.ext import commands
from asyncio import sleep
from os import path, makedirs
from json import dump, load
from pathlib import Path

from utils.log import Logger

class ownerCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

		if (self.bot.verbose):
			print ("Loaded Cog:\t", "owner-cog.py:\townerCog")

	@commands.command(
		name = "logout",
		brief = "Log the client out",
		usage = "logout",
		enabled = True,
		description = "Log the client out. This is only an owner command.",
		hidden = True
	)
	@commands.is_owner()
	async def logout(self, ctx):
		if (self.bot.verbose):
			print ("Logout - Initiated")
			await ctx.channel.send(content="Logout Sequence Initiated")

		#Any clean-up code goes here
		await self.bot.change_presence(status = discord.Status.offline)

		if (self.bot.verbose):
			print ("Logout - Completed")
			await ctx.channel.send(content="Logout Sequence Completed")

		await sleep(1)
		await self.bot.logout()

def setup(bot):
	bot.add_cog(ownerCog(bot))