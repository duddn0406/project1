import discord
from discord.ext import commands
from discord.utils import get

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
    await ctx.send(usermessage)

@bot.command()


@bot.command()
async def 역할 변경 (ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="관리자")
    await ctx.channel.send(str(member) + "당신은 이제 관리자 입니다")

@bot.command()
async def on_member_join(ctx):
    await ctx.send('{member} 가 들어왔습니다')




@bot.command(pass_context = True)
async def mute(ctx, member : discord.Member):
    if ctx.message.author.sever_permission.administrator:
        user = ctx.message.author
        role = discord.utils.get(user.sever.roles, name="유배지")
        await client.add_roles(user, role)
    else:
        embed=discord.Embed(title="안되지", description="안되지", color=0xff00f6)
        await bot.say(embed=embed)

bot.run('토큰')
