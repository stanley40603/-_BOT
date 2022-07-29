import discord
from discord.ext import commands
import json
import random,os,asyncio

with open('setting.json', 'r', encoding='utf8')as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')
    
bot.run(jdata['TOKEN']) 