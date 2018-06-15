import discord
from discord.ext import commands
import ast


class AdminBot:
    def __init__(self, bot):
        self.botAdmin = bot

    def check_admin_channel(ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

"""___________"""
    @botAdmin.command(name="warn",
                        aliases=['warning'],
                        description="Warning",
                        brief="warn a user",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def warning(self, ctx, providedUserID : int, reason : str):

        try:
            warnUser = botAdmin.get_user(providedUserID)
        except:
            await ctx.channel.send(content="```Fail#AB03```")
            print ("Fail#AB03 Command: warning-warnUser")

        embedTitle = "Infraction"
		embedColour = discord.Colour.red()
        embedDesc = "**__Infraction__**\n\n"
        embedDesc += str(warnUser.mention)+"This is a Formal Infraction through a warning."
        embedDesc += "\nIf you think your infraction is undoubtedly unjustified,"
        embedDesc += " please **do not** post about it in a public channel but take it up with an administrator.\n"
        embedThumbnail = "http://i.imgur.com/XKmsqJN.jpg"

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

        sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+warnUser.name+"\tReason: "+reason
        await ctx.channel.send("```"+sendUpdate+"```")

"""___________"""
    @botAdmin.command(name="strike",
                        description="strike",
                        brief="send a strike to a user",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def strike(self, ctx, providedUserID : int, reason : str):
        try:
            strikeUser = botAdmin.get_user(providedUserID)
        except:
            await ctx.channel.send(content="```Fail#AB09```")
            print ("Fail#AB03 Command: strike-srtikeUser")

        embedTitle = "Infraction"
		embedColour = discord.Colour.red()
        embedDesc = "**__Infraction__**\n\n"
        embedDesc += str(strikeUser.mention)+"This is a Formal Infraction through a strike."
        embedDesc += "\nIf you think your infraction is undoubtedly unjustified,"
        embedDesc += " please **do not** post about it in a public channel but take it up with an administrator.\n"
        embedThumbnail = "https://orig00.deviantart.net/3e08/f/2017/299/0/3/tohru_by_sethster3000-dbrrbnh.png"

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
            await strikeUser.send(embed=sendEmbed)
        except:
            await ctx.channel.send(content="```Fail#AB07```")
            print ("Fail#AB07 Command: warning-send(embed=...)")
            return -1

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(strikeUser.id), warning=1)
        """

        sendUpdate = ">"+ctx.user.mention+"\tWarned\t"+strikeUser.name+"\tReason: "+reason
        #await ctx.channel.send("```"+sendUpdate+"```")

"""___________"""
    @botAdmin.command(name="welcomeTheMod",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.check(check_admin_channel)
    async def welcomeTheMod(self, ctx, providedUserID : int):
        #Get the new mod's id
        try:
            newMod = botAdmin.get_user(providedUserID)
        except:
            await ctx.channel.send("```Fail#AB09\n(most likely that the ID provided is incorrect)\n(Did you leave a space between the command and the ID?)```")
            print ("Fail#AB09 Command: welcomeTheMod-newMod = bot.get_user(...)")
            return

        await ctx.channel.send("```The new member you want to make a mod is: "+str(newMod.display_name))
        await ctx.channel.send("```Type \"Blue\" to confirm (10 s)")

        #confirmation that one wants to make the user a mod
        try:
            def check(msg):
                return (confirmMsg.author.id == ctx.message.author.id) and (confirmMsg.channel.id = ctx.message.channel.id)
            confirmMsg = await  botAdmin.wait_for(event = 'message', timeout = 10, check=check)
        except:
            await ctx.channel.send("```Aborted```")
            return

        #check whether they confirmed it right
        if (confirmMsg.content != "Blue"):
            await ctx.channel.send("```Aborted```")
            return

        #EmbedProcess
        embedTitle = str(ctx.guild.name)

        #Retrieve data from file
        with open("Resources/welcomeTheMod_Text_Embed", 'r') as welcomeFile:
            welcomeText = ast.literal_eval(welcomeFile.read())

        embedThumbnail = 'https://data.whicdn.com/images/277871774/original.gif'

        #Create Embed
        welcomeBed = discord.Embed(title=embedTitle, description=welcomeText["embedDesc"], colour=discord.Colour.gold())
        welcomeBed.set_thumbnail(url=embedThumbnail)

        count = 1
        for rule in welcomeText["ruleFields"]:
            welcomeBed.add_field(name=str(count), value=rule)

        for welcomeCommand in welcomeText["commands"]:
            welcomeBed.add_field(name=welcomeCommand, value=welcomeCommand["commands"][welcomeCommand])

        welcomeBed.add_field(name="Welcome to the fam",
        value="If you have any further questions, please ask in the admins channel. For now, welcome to the family, fam! BTW, if you are on your laptop, click on the photo!")

        #Send the Embed to the user
        try:
            sentMsg = await newMod.send(embed=welcomeBed)
            newModChannel = sentMsg.channel.id
            await newMod.send("```You have 120 seconds to read this message and type: Blue to accept.```")
        except:
            await ctx.channel.send("```Fail#AB10```")
            print ("Fail#AB10 command-welcomeTheMod newMod.send(embed=...)")
            return

        #Check if the new Mod accepts
        try:
            def check(msg):
                return (confirmMsg.author.id == newMod.user.id) and (newModChannel == confirmMsg.channel.id)
            confirmMsg = await  botAdmin.wait_for(event = 'message', timeout = 120, check=check)
        except:
            await ctx.channel.send("```"+str(newMod.display_name)+" has not accepted. You can inquire to find out why and repeat this process, if desired.```")
            await newMod.send("```Aborted. You did not type Blue to confirm within 120 seconds. Contact a moderator to repeat this process.")
            return

        #All Done. Now send a message to welcome them
        congratsMsg = await ctx.channel.send("```"+str(newMod.display_name)+" has accepted. Please welcome "+str(newMod.display_name)+"```")
        await congratsMsg.add_reaction("\U0001f389")

"""___________"""
    @botAdmin.command(name="kickOut",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.check(check_admin_channel)
    async def welcomeTheMod(self, ctx, providedUserID : int, reason : str):
        kickUser = botAdmin.get_user(providedUserID)

        embedTitle = "Kick"
		embedColour = discord.Colour.red()
        embedDesc = "**__Kick__**\n\n"
        embedDesc += str(kickUser.mention) + ", we're very sorry for it to happen this way, but you have been kicked out."
        embedDesc += "\nPlease **do not** attempt to rejoin the server for 7 days. If you feel like the reason you have been kicked out was incorrect, please"
        embedDesc += " please type: ++unliftMyKick here. You can fill a form where it will be reviewed. However, if you join within 7 days, you will be banned."
        embedDesc += "\n\nYou have been warned."
        embedThumbnail = "https://orig00.deviantart.net/3e08/f/2017/299/0/3/tohru_by_sethster3000-dbrrbnh.png"

        sendEmbed = discord.Embed(title=embedTitle, description=embedDesc, colour=embedColour)
        sendEmbed.set_thumbnail(url=embedThumbnail)
        sendEmbed.add_field(name="Reason", value=reason)

        #memberKick

        """
        Update(Guild=str(Message.guild.id)), modUser=(ctx.user.id), affectedUser=(warnUser.id), warning=1)
        """

        sendUpdate = ">"+ctx.user.mention+"\tKicked\t"+kickUser.name+"\tReason: "+reason
        #await ctx.channel.send("```"+sendUpdate+"```")
