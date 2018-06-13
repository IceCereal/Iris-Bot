import discord
from discord.ext import commands

class AdminBot:
    def __init__(self, bot):
        self.botAdmin = bot

"""___________"""
    @botAdmin.command(name="warn",
                        aliases=['warning'],
                        description="Warning",
                        brief="warn a user",
                        hidden=True)
    @botAdmin.guild_only()
    @botAdmin.has_permissions(kick_members=True)
    async def warning(self, ctx, providedUserID : int, reason : str):
        try:
            warnUser = botAdmin.get_user(providedUserID)
        except:
            await ctx.channel.send(content="```Fail#AB03```")
            print ("Fail#AB03 Command: warning-warnUser")

        embedTitle = "Infraction"
		embedColour = discord.Colour.red()
        embedDesc = "**__Infraction__**\n\n"
        embedDesc += "This is a Formal Infraction through a warning."
        embedDesc += "\nIf you think your infraction is undoubtedly unjustified,"
        embedDesc += " please **do not** post about it in a public channel but take it up with an administrator.\n"
        embedThumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Angry_robot.svg/404px-Angry_robot.svg.png"

        try:
            sendEmbed = discord.Embed(title=embedTitle, description=embedDesc, colour=embedColour)
        except:
            await ctx.channel.send(content="```Fail#AB04```")
            print ("Fail#AB04 Command: warning-discord.Embed()")
            return -1

        try:
            sendEmbed.set_thumbnail(url=embedThumbnail)
        except:
            await ctx.channel.send(content="```Fail#AB05```")
            print ("Fail#AB05 Command: warning-Embed.set_thumbnail()")
            return -1

        StrikeCount = 0

        """try:
            get user data
        """
        try:
            sendEmbed.add_field(name="Strikes Given:", value="0")
            sendEmbed.add_field(name="Strike Count:", value=str(StrikeCount)+" / 3")
            sendEmbed.add_field(name="Reason:", value=reason)
        except:
            await ctx.channel.send(content="```Fail#AB06```")
            print ("Fail#AB06 Command: warning-Embed.add_field()")
            return -1

        try:
            await warnUser.send(embed=sendEmbed)
        except:
            await ctx.channel.send(content="```Fail#AB07```")
            print ("Fail#AB07 Command: warning-send(embed=...)")
            return -1

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(warnUser.id), warning=1)
        """

        try:
            sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+warnUser.mention+"\tReason: "+reason
            await ctx.channel.send("```"+sendUpdate+"```")
        except:
            await ctx.channel.send("```Sent warning. Fail#AB08```")
            print ("Fail#AB08 Command: warning-sendUpdate")

"""___________"""
    @botAdmin.command(name="strike",
                        description="strike",
                        brief="send a strike to a user",
                        hidden=True)
    @botAdmin.guild_only()
    @botAdmin.has_permissions(kick_members=True)
    async def strike(self, ctx, providedUserID : int, reason : str):
        try:
            strikeUser = botAdmin.get_user(providedUserID)
        except:
            await ctx.channel.send(content="```Fail#AB09```")
            print ("Fail#AB03 Command: strike-srtikeUser")

        embedTitle = "Infraction"
		embedColour = discord.Colour.red()
        embedDesc = "**__Infraction__**\n\n"
        embedDesc += "This is a Formal Infraction through a strike."
        embedDesc += "\nIf you think your infraction is undoubtedly unjustified,"
        embedDesc += " please **do not** post about it in a public channel but take it up with an administrator.\n"
        embedThumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Angry_robot.svg/404px-Angry_robot.svg.png"

        try:
            sendEmbed = discord.Embed(title=embedTitle, description=embedDesc, colour=embedColour)
        except:
            await ctx.channel.send(content="```Fail#AB04```")
            print ("Fail#AB04 Command: warning-discord.Embed()")
            return -1

        try:
            sendEmbed.set_thumbnail(url=embedThumbnail)
        except:
            await ctx.channel.send(content="```Fail#AB05```")
            print ("Fail#AB05 Command: warning-Embed.set_thumbnail()")
            return -1

        StrikeCount = 1

        """try:
            get user data
        """
        try:
            sendEmbed.add_field(name="Strikes Given:", value="0")
            sendEmbed.add_field(name="Strike Count:", value=str(StrikeCount)+" / 3")
            sendEmbed.add_field(name="Reason:", value=reason)
        except:
            await ctx.channel.send(content="```Fail#AB06```")
            print ("Fail#AB06 Command: warning-Embed.add_field()")
            return -1

        try:
            await warnUser.send(embed=sendEmbed)
        except:
            await ctx.channel.send(content="```Fail#AB07```")
            print ("Fail#AB07 Command: warning-send(embed=...)")
            return -1

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(warnUser.id), warning=1)
        """

        try:
            sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+warnUser.mention+"\tReason: "+reason
            await ctx.channel.send("```"+sendUpdate+"```")
        except:
            await ctx.channel.send("```Sent warning. Fail#AB08```")
            print ("Fail#AB08 Command: warning-sendUpdate")
