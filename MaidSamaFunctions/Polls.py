import discord
from discord.ext import commands
import ast


class Polls:
    def __init__(self, bot):
        self.PollsBot = bot

    def check_admin_channel(self, ctx):
        return ctx.channel.id == get_channel_id("AdminBot_Control")

    def PrintArgs(self):
        print ("Polls")
        print ("The *Args for the above mentioned are:")
        print ("\n-HideName :\tShow's 'Poll' as the Embed Title.\n\t\tDefault: NameOfPollCreator's Poll")
        print ("\n-SetName :\tSets the argument right after this arg as the Poll Title.\n\t\tThe Title must be in \"'s")
        print ("\n-PollPic :\tSets the url right after this arg as the Poll's Image.\n\t\tDefault = Question Mark\n\t\tThe url should be in \"'s")
        print ("\n-SetTimeout :\tSets the time right after this arg as the timeout in seconds.\n\t\tDefault = 120s")
        print ("\n-SetDeployChannel :\tSets the channel id right after this arg as the channel where this poll will be deployed.\n\t\tThe Channel ID must be given\n\t\tdefault = Polls")


    @PollsBot.command(name="poll",
                        description="Poll",
                        brief="Make a Poll",
                        hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.check(check_admin_channel)
    async def poll(self, ctx, type : int, *args):
        args = list(args)

        #These are the args:
        embedTitle = ctx.message.author
        embedThumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Question_mark_white-transparent.svg/2000px-Question_mark_white-transparent.svg.png"
        questionTimeout = 120
        deployChannel = get_channel_id("Polls")

        #Parse Args:
        i = 0
        while (i < len(args)):
            if (args[i] == "-HideName"):
                embedTitle = "Poll"

            elif (args[i] == "-SetName"):
                embedTitle = args[i + 1]
                i += 1

            elif (args[i] == "-PollPic"):
                embedThumbnail = args[i + 1]
                i += 1

            elif (args[i] == "-SetTimeout"):
                questionTimeout = args[i + 1]
                i += 1

            elif (args[i] == "-SetDeployChannel"):
                deployChannel = args[i + 1]
                i += 1

            else:
                await ctx.channel.send(content="Did not recognize argument:\t"+str(args[i]))
                #LOG
                return

            i += 1


        if (type != 1) and (type != 2):
            await ctx.channel.send(content="Oops. You need to send either 1 (Y/N) or 2 (Multi-Options).", delete_after = 10)

        if (type == 1):

            await ctx.channel.send(content="Enter the (y/n) Question:", delete_after=questionTimeout)

            try:
                def check(msg):
                    return (ctx.channel.id == msg.channel.id and ctx.message.author.id == msg.author.id)
                rawQuestionMessage = await PollsBot.wait_for('message', check=check, timeout=questionTimeout)

                if (rawQuestionMessage.content.lower() == "exitcereal"):
                    await ctx.channel.send(content="ABORTED. Messages will delete automatically", delete_after = 20)
                    rawQuestionMessage.delete()
                    return

                SetQuestion = rawQuestionMessage.content()

            except:
                await ctx.channel.send(content="Timeout Reached.", delete_after=10)
                return

        else:
            await ctx.channel.send(content="Enter the (Multiple Options) Question:", delete_after=120)

            try:
                print ("Try begin")
                def check(msg):
                    return (ctx.channel.id == msg.channel.id and ctx.message.author.id == msg.author.id)
                rawQuestionMessage = await bot.wait_for('message', check=check, timeout=120)

                if (rawQuestionMessage.content.lower() == "exitcereal"):
                    await ctx.channel.send(content="ABORTED. Messages will delete automatically.", delete_after = 20)
                    await rawQuestionMessage.delete()
                    return

                SetQuestion = rawQuestionMessage.content
                print (SetQuestion)

                rawOptionsMessage = []

                for i in range(0,9,1):
                    await ctx.channel.send(content="Enter Option# "+str(i+1), delete_after=30)

                    try:
                        def check(msg):
                            return (ctx.channel.id == msg.channel.id and ctx.message.author.id == msg.author.id)
                        ATemporaryMsg = await bot.wait_for('message', check=check, timeout=30)
                        rawOptionsMessage.append(ATemporaryMsg)

                        print (rawOptionsMessage[i].content)

                        if (rawOptionsMessage[i].content.lower() == "exitcereal"):
                            await ctx.channel.send(content="ABORTED. Messages will delete automatically.", delete_after=20)
                            await ctx.channel.delete_messages(rawOptionsMessage)
                            await rawQuestionMessage.delete()
                            return

                        if (rawOptionsMessage[i].content.lower() == "completed the poll"):
                            break

                    except Exception as e:
                        await ctx.channel.send(content="Timeout Reached." +str(e))
                        await ctx.channel.delete_messages(rawOptionsMessage)
                        await rawQuestionMessage.delete()

                        return
            except Exception as e:
                print (await ctx.channel.send(content="Timeout Reached." +str(e))
                await rawQuestionMessage.delete()

        #Create Embed And Send It
        embedTitle =
        if (type == 1):
