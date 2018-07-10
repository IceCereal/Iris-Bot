import discord
from discord.ext import commands
import ast


class AdminBot:
    def __init__(self, bot):
        self.botAdmin = bot

    def check_admin_channel(ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    @botAdmin.command(name="kickOut",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def welcomeTheMod(self, ctx, providedUserID : int, reason : str):
        kickUser = botAdmin.get_user(providedUserID)

        embedTitle = str(ctx.message.guild.name)
		embedColour = discord.Colour.red()

        with open("kick_Text_Embed", 'r') as kickTextFile:
            kickText = ast.literal_eval(kickTextFile.read())

        kickBed = discord.Embed(title=embedTitle, description=kickText["kick_description"], colour=embedColour)
        kickBed.set_thumbnail(url=kickText["embed_thumbnail"])

        kickBed.add_field(name="")
        kickBed.add_field(name="Reason", value=reason)

        guild = ctx.guild
        await guild.kick(kickUser, reason=ctx.user.display_name+" kicked "+kickUser.display_name+" Reason:"+reason)

        await kickUser.send(embed="Embed")

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(warnUser.id), warning=1)
        """

        sendUpdate = ">"+ctx.user.mention+"\tKicked\t"+kickUser.name+"\tReason: "+reason
        #await ctx.channel.send("```"+sendUpdate+"```")

        try:
            def check(msg):
                return (msg.content == "++unliftMyKick") and (msg.author.id == kickUser.id)
            await kickUser.wait_for(event='message', timeout=60, check=check)
        except:
            await kickUser.send(content="```Sorry, but you did not try to appeal. Please refrain from joining the server for another 7 days.```")
            return
a
