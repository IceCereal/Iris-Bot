import discord
from discord.ext import commands
import ast

# NOTE: Organize this way
# NOTE: Check if command exists / print it out if exists / delete feature
# NOTE: Make A Command

class FalseCommands:
    def __init__(self, bot):
        self.Bot = bot

    def check_admin_channel(self, ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    def PrintArgs(self):
        print ("False Commands")
        print ("The *Args for the above mentioned are:")
        print ("\n-edit : Edits the command.")
        print ("\n-delete: Deletes the command.")
        print ("\n-changeaccess: Changes the access level of the command (i.e. who can invoke it and who can't).")

    async def CheckCommand(ctx)






    @bot.command(name="MakeACommand", hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def MakeACommand(self, *args)
