import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def 봇(ctx):
    await ctx.send('가동!')

@bot.command()
async def 청소(ctx, amount=80000000000000000000000000000):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def kick (ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@bot.command()
async def 말해 (ctx, usermessage):
    await ctx send(usermessage)


bot.run('토큰')
