import discord
from discord.ext import commands
from utils import *
from functions import *

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!l ", intents=intents)
game = Game()


@Bot.event
async def on_ready():
    print("Yüce Bot L0ck Önünde Diz Çök!!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channel, name="genel")
    await channel.send(f"{member} Server'a Katıldı!")
    print(f"{member} Server'a Katıldı!")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channel, name="genel")
    await channel.send(f"{member} Defoool!")
    print(f"{member} Defooool!")


@Bot.command(aliases=["game", "zar"])
async def oyun(ctx, *args):
    if "roll" in args:
        await ctx.send(f"Bir zar atıldı: {game.roll_dice()}")
    else:
        await ctx.send("Yürü ya kulum!")


@Bot.command()
async def yuceLock(msg):
    print(msg.message)
    await msg.send("Şımartma yahu!")


@Bot.command()
async def naber(mesaj):
    await mesaj.send("İyiyim Teşekkürler, Sen Nasılsın <3")


@Bot.command()
async def kura(x, *y):
    liste = list(y)
    await x.send(random.choice(liste))


@Bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@Bot.command(aliases=["copy"])
async def clone_channel(ctx):
    await ctx.channel.clone()


Bot.run(TOKEN)
