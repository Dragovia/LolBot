import discord
import random
from discord.ext import commands
#from discord.ext import Bot
import asyncio
#import chalk


client = commands.Bot(command_prefix ='.')

@client.event
async  def on_ready():
    print('Bot is ready')
    print ("I am running on " + client.user.name)
    #print ("With the ID: " + client.user.id)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    if not question:
        print("please add a question")

    responses =['It is certain','its is deciely so','without a doubt'
                                                    'yes'
                                                    'you may rely on it'
                                                    'as i see it, yes'
                                                    'most likely'
                                                    'outlook good'
                                                    'yes'
                                                    'signs point to yes'
                                                    'repl hazy try again'
                                                    'ask again later'
                                                    'better not tell you now'
                                                    'cannot predict now'
                                                    'concerntrate and ask again'
                                                    'dont cout oon it'
                                                    'my reply is no'
                                                    'my soucrs say no'
                                                    'outlook not so good'
                                                    'very doubtful']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')


@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    if user:
        await ctx.send(":boot: Cya, {}. Ya loser!".format(user.name))
        await ctx.kick(user)
        print ("!kick on {}".format(user.name))
    else:
        await ctx.send("Please tag a user to kick")


@client.command
async def kick_error(ctx, error):
    if isinstance(error, discord.ext.commands.BadArgument):
        await ctx.send('Could not recognize user')


client.run('NTkzNTYxMTg0MjQ3MDg3MTMz.XRPq_Q.RRLvUeZZ-g8yCIBo9xrRlG9pAOg')