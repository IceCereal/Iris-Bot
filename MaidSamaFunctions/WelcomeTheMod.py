import discord
from discord.ext import commands
import ast


class AdminBot:
    def __init__(self, bot):
        self.botAdmin = bot

    def check_admin_channel(ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    @botAdmin.command(name="welcomeTheMod",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.check(check_admin_channel)
    async def welcomeTheMod(self, ctx, providedUserID : int):
        #Get the new mod's id
        newMod = botAdmin.get_user(providedUserID)

        await ctx.channel.send("```The new member you want to make a mod is: "+str(newMod.display_name))
        await ctx.channel.send("```Type \"Cereal\" to confirm (10 s)")

        #confirmation that one wants to make the user a mod
        try:
            def check(msg):
                return (confirmMsg.author.id == ctx.message.author.id) and (confirmMsg.channel.id = ctx.message.channel.id)
            confirmMsg = await  botAdmin.wait_for(event = 'message', timeout = 10, check=check)
        except:
            await ctx.channel.send("```Aborted```")
            return

        #check whether they confirmed it right
        if (confirmMsg.content != "Cereal"):
            await ctx.channel.send("```Aborted```")
            return

        #EmbedProcess
        embedTitle = str(ctx.guild.name)

        #Retrieve data from file
        with open("Resources/welcomeTheMod_Text_Embed", 'r') as welcomeTextFile:
            welcomeText = ast.literal_eval(welcomeTextFile.read())

        #Create Embed
        welcomeBed = discord.Embed(title=embedTitle, description=welcomeText["embedDesc"], colour=discord.Colour.gold())
        welcomeBed.set_thumbnail(url=welcomeText["embed_thumbnail"])

        count = 1
        for rule in welcomeText["ruleFields"]:
            welcomeBed.add_field(name=str(count), value=rule)
            count += 1

        for welcomeCommand in welcomeText["commands"]:
            welcomeBed.add_field(name=welcomeCommand, value=welcomeCommand["commands"][welcomeCommand])

        welcomeBed.add_field(name="Welcome to the fam",
        value="If you have any further questions, please ask in the admins channel. For now, welcome to the family, fam! BTW, if you are on your laptop, click on the photo!")

        #Send the Embed to the user
        sentMsg = await newMod.send(embed=welcomeBed)
        newModChannel = sentMsg.channel.id
        await newMod.send("```You have 120 seconds to read this message and type: Cereal to accept.```")

        #Check if the new Mod accepts
        try:
            def check(msg):
                return (confirmMsg.author.id == newMod.user.id) and (newModChannel == confirmMsg.channel.id)
            confirmMsg = await  botAdmin.wait_for(event = 'message', timeout = 120, check=check)
        except:
            await ctx.channel.send("```"+str(newMod.display_name)+" has not accepted. You can inquire to find out why and repeat this process, if desired.```")
            await newMod.send("```Aborted. You did not type Cereal to confirm within 120 seconds. Contact a moderator to repeat this process.")
            return

        #All Done. Now send a message to welcome them
        congratsMsg = await ctx.channel.send("```"+str(newMod.display_name)+" has accepted. Please welcome "+str(newMod.display_name)+"```")
        await congratsMsg.add_reaction("\U0001f389")
