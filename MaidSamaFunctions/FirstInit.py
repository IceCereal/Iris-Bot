Cereal"""
A bot command that is to be used only once.
This initializes every thing that is to be required.
"""

import discord
from discord.ext import commands
import datetime

class AdminDeployBot:
    def __init__(self, bot):
        self.botAdmin = bot

    """When Maid-Sama joins a guild
    this function gets executed"""
    @botAdmin.event:
    async def on_guild_join(self, guild):
        print ("\nJoined Guild:\t"+str(guild.name))
        print ("Time:\t"+str(datetime.datetime.now()))

        sysChannel = guild.system_channel

        joinedMsg = "```"

        joinedMsg += "\nHello. My name is Maid-Sama. Thank you for inviting me. I'm here to help you with your chores."
        joinedMsg += "\n\n>You can call for me by using the '++' command prefix"
        joinedMsg += "\n\nInstructions:"
        joinedMsg += "\n\n>Run the command: ++inititiateACerealSequence"
        joinedMsg += "\n\nThis creates two channels: AdminBot_Control and Polls."
        joinedMsg += "\n\nAdminBot_Control is the channel where the Admin's can communicate with me. "
        joinedMsg += "I shall be sending you updates on the server's happenings and you can assign me chores there."
        joinedMsg += " An important note about AdminBot_Control:"
        joinedMsg += "\n\tModerators will need to be given permissions to view this channel"
        joinedMsg += "\n\nPolls is a channel where you can deploy a poll. Please refrain from sending anything in that channel."
        joinedMsg += "\n\n>All the Admin's and Moderators need to switch on developer mode."
        joinedMsg += " You can do this by:"
        joinedMsg += "\n\tGo to User Settings"
        joinedMsg += "\n\tClick on Appearance"
        joinedMsg += "\n\tToggle developer mode"
        joinedMsg += "\n\nYou will need to do this because I operate on ID's (right-click on my name to see copy ID)."
        joinedMsg += " For example: To send a strike to a user, you do:"
        joinedMsg += "\n\t++strike <User ID> <Reason>\t\t(btw, don't include the < >'s)"
        joinedMsg += "\n\n\nWhenever you assign the role of moderator to a member, write this:"
        joinedMsg += "\n\t++welcomeTheMod <Mod's ID>"
        joinedMsg += "\n\nThis sends a direct message to the person you want to make a moderator about the rules of being"
        joinedMsg += " a moderator and the commands that they can use."
        joinedMsg += "\n\nThank you for inviting me to this server and I hope to serve you well. If you have any questions,"
        joinedMsg += " please ask it to my creator: IceCereal in your private admins channel"

        joinedMsg += "```"

        await sysChannel.send(joinedMsg)

    """
    Authorizes an Admininstrative HQ for the Guild
    Creates a Polls Channel
    """
    @botAdmin.command(name="inititiateACerealSequence",
    					hidden=True,)
    @botAdmin.guild_only()
    @botAdmin.has_permissions(administrator=True)
    async def inititiateACerealSequence(self, ctx):

        await ctx.channel.send(content="```Type: Cereal\nYou have 10 seconds```", delete_after=10)

        try:

            msg = await client.wait_for('message', timeout=10)

            AdminBotMessage = 0

            if (msg.content == "Cereal" and msg.channel == ctx.channel):

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

                    AdminBotMessage = await ctx.message.guild.create_text_channel("AdminBot_Control", overwritesAdmin=overwrites)
                    await AdminBotMessage.channel.send("```Initialized.\nPlease drag this channel to where ever you want to keep.```")
                    #log("Admin", AdminBotMessage.channel.id) --> Set up in Storage.py
                    await ctx.channel.send(content="```Completed AdminBot_Control!```", delete_after=5)
                except:

                    if (AdminBotMessage == 0):

                        await ctx.channel.send(content="```Fail#ABD01.01\nYou have to give me \"administrator / manage channels\" permissions\n\n"
                        "It would be better if you give me all the permissions```")
                        print ("Fail#ABD01.01 Command: inititiateACerealSequence")

                    else:

                        await ctx.channel.send(message="```Fail#ABD01.02\nYou have to give me \"administrator\" permission\n\n"
                        "It would be better if you give me all the permissions```")

                        await ctx.channel.send(message="```Deleting Channel: AdminBot_Control")
                        AdminBotMessage.channel.delete(reason="administrator permissions were not given")

                        print ("Fail#ABD01.02 Command: inititiateACerealSequence")

                    return 0

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
                    #log("Polls", pollsChannel.channel.id) --> Set up in Storage.py
                    await ctx.channel.send(content="```Completed Polls!```", delete_after=5)
                except:

                    await ctx.channel.send(content="```Fail#ABD02```")
                    print ("Fail#ABD02 Command: inititiateACerealSequence")

                    await ctx.message.guild.delete("")

                    return 0


            else:
                await ctx.channel.send(content="```Wrong Password/ Wrong Channel. 🙄```", delete_after=10)
                await msg.delete()
        except:
            pass
