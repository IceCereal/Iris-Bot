import discord
from discord.ext import commands
import ast


class WarnBot:
    def __init__(self, bot):
        self.WarnBot= bot

    def check_admin_channel(ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    @WarnBot.command(name="warn",
                        aliases=['warning'],
                        description="Warning",
                        brief="warn a user",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def warning(self, ctx, providedUserID : int, reason : str):

        warnUser = WarnBot.get_user(providedUserID)

        embedTitle = str(ctx.message.guild.name)
        embedColour = discord.Colour.red()

        #Read the file:
        with open("warning_Text_Embed", 'r') as warningTextFile:
            warningText = ast.literal_eval(warningTextFile.read())

        warnBed = discord.Embed(title=embedTitle, description=warningText["warning_description"], colour=embedColour)

        warnBed.set_thumbnail(url=warningText["embed_thumbnail"])

        StrikeCount = 0

        """try:
            get user data
        """

        warnBed.add_field(name="Isuued To:", value=warnUser.mention)
        warnBed.add_field(name="Strikes Given:", value="0")
        warnBed.add_field(name="Strike Count:", value=str(StrikeCount)+" / 3")
        warnBed.add_field(name="Reason:", value=reason)

        await warnUser.send(embed=warnBed)

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(warnUser.id), warning=1)
        """

        sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+warnUser.name+"\tReason: "+reason
        await ctx.channel.send("```"+sendUpdate+"```")
