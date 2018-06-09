"""
A bot command that is to be used only once.
This initializes every thing that is to be required.
"""

import discord
from discord.ext import commands

class AdminDeployBot:
    def __init__(self, bot):
        self.botAdmin = bot

    """
    Authorizes an Admininstrative HQ for the Guild
    Creates a Polls Channel
    """
    @botAdmin.command(name="inititiateABlueSequence",
    					description=
                        "++inititiateABlueSequence makes the following channels:"
                        "\n\t>AdminBot_Control"
                        "\n\t>Polls",
    					brief="Creates a Bot environment",
    					hidden=True,)
    @botAdmin.guild_only()
    @botAdmin.has_permissions(administrator=True)
    async def inititiateABlueSequence(self, ctx):

        await ctx.channel.send(content="```Type: Blue\nYou have 10 seconds```", delete_after=10)

        try:

            msg = await client.wait_for('message', timeout=10)

            if (msg.content == "Blue" and msg.channel == ctx.channel):

                roles = ctx.message.guild.roles

                #AdminBot
                try:
                    setPerm = None
                    overwritesAdmin={}

                    for role in roles:
                        if (discord.Permissions(8) <= role.permissions):
                            setPerm = True
                        else:
                            setPerm = False
                        overwritesAdmin[role] = discord.PermissionOverwrite(read_messages=setPerm)

                    AdminBotChannel = await ctx.message.guild.create_text_channel("AdminBot_Control", overwritesAdmin=overwrites)
                    #log("Admin", AdminBotChannel) --> Set up in Storage.py
                    await ctx.channel.send(content="```Completed AdminBot_Control!```", delete_after=5)
                except:

                    await ctx.channel.send(content="```Fail#ABD01```")
                    print ("Fail#ABD01 Command: inititiateABlueSequence")

                #Polls
                try:
                    setPerm = None
                    overwritesPolls={}

                    for role in roles:
                        if (discord.Permissions(8) <= role.permissions):
                            pass
                        else:
                            overwritesPolls[role] = discord.PermissionOverwrite(
                            read_messages = True,
                            send_messages = False,
                            external_emojis = False,
                            add_reactions = False)

                    pollsChannel = await ctx.message.guild.create_text_channel("Polls", overwrites)
                    #log("Polls", pollsChannel) --> Set up in Storage.py
                    await ctx.channel.send(content="```Completed Polls!```", delete_after=5)
                except:

                    await ctx.channel.send(content="```Fail#ABD02```")
                    print ("Fail#ABD02 Command: inititiateABlueSequence")


            else:
                await ctx.channel.send(content="```Wrong Password/ Wrong Channel. 🙄```", delete_after=10)
                await msg.delete()
        except:
            pass
