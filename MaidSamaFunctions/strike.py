import discord
from discord.ext import commands
import ast


class AdminBot:
    def __init__(self, bot):
        self.botAdmin = bot

    def check_admin_channel(ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    @botAdmin.command(name="strike",
                        description="strike",
                        brief="send a strike to a user",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def strike(self, ctx, providedUserID : int, reason : str):
        strikeUser = botAdmin.get_user(providedUserID)

        embedTitle = str(ctx.message.guild.name)
		embedColour = discord.Colour.red()

        with open("strike_Text_Embed", 'r') as strikeTextFile:
            strikeText = ast.literal_eval(strikeTextFile.read())

        strikeBed = discord.Embed(title=embedTitle, description=strikeText["strike_description"], colour=embedColour)

        strikeBed.set_thumbnail(url=strikeText["embed_thumbnail"])

        StrikeCount = 1

        """try:
            get user data
        """

        strikeBed.add_field(name="Issued To:", value=strikeUser.mention)
        strikeBed.add_field(name="Strikes Given:", value="0")
        strikeBed.add_field(name="Strike Count:", value=str(StrikeCount)+" / 3")
        strikeBed.add_field(name="Reason:", value=reason)

        await strikeUser.send(embed=strikeBed)

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(strikeUser.id), warning=1)
        """

        sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+strikeUser.name+"\tReason: "+reason
        #await ctx.channel.send("```"+sendUpdate+"```")
