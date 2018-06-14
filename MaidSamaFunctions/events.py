"""All the possible events that can happen"""

import discord
import datetime

class Events:
    def __init__(self, bot):
        self.botEvent = bot

    """OnMessage_________"""
    @botEvent.event
    async def on_message(self, message):

        await bot.process_commands(message)

    """OnMemberJoin_________"""
    @botEvent.event
    @botEvent.guild_only()
    async def on_member_join(self, member):

        embedTitle = "Welcome"
        embedColour = discord.Colour.blue()
        embedDesc = "Welcome " + member.mention() + "!"
        embedThumbnail = str(member.avatar)

        welcomeEmbed = discord.Embed(title=embedTitle, description=embedDesc, colour=embedColour)

        embedRules = "\n1. Go through rules at #rules"
        embedRules += "\n2. No Table-flipping in this server"
        embedRules += "\n\n\t\t(╯°□°）╯︵ ┻━┻"
        embedRules += "\n\t\t\t_Not Allowed_"

        #Add randomized rules that can be added from the AdminBot_Control Channel

        welcomeEmbed.add_field(name="Instructions", value=embedRules)
        welcomeEmbed.set_thumbnail(url=embedThumbnail)

        #welcomeChannel = retrieveChannel("welcome")

        await welcomeChannel.send(embed=welcomeEmbed)

    """OnConnect_________"""
    @botEvent.event
    async def on_connect(self):

        print ("\nConnected to Discord")

    """OnMessageDelete_________"""
    @botEvent.event
    async def on_message_delete(self,message):

        print ("\nMessage Delete:")
        print ("Author:\t"+str(message.author))
        print ("Content:\t"+str(message.content))
        print ("Guild, Channel:\t"+(message.guild.name)+", "+(message.channel.name))
        print ("Time:\t"+str(datetime.datetime.now()))

    """OnCommandError_________"""
    @botEvent.event
    async def on_command_error(self, ctx, error):

         print ("\nError:")
         print ("User:\t"+str(ctx.message.author))
         print ("Tried:\t"+str(ctx.message.content))
         print ("Guild, Channel:\t"+ctx.message.guild.name+", "+ctx.message.channel.name)
         print ("Time:\t"+str(datetime.datetime.now()))

         if isinstance(error, commands.CheckFailure):
             if "missing Administrator permission(s)" in error:
                 await ctx.channel.send("You have no power here.")
             else:
                 await ctx.channel.send(str(error))
