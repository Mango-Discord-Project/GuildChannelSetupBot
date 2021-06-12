import discord
import json
from discord.ext import commands
from datetime import datetime

def now(): return f'[{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}]'

with open('./Token.json', 'r') as TokenFile:
    TokenData = json.load(TokenFile)

with open('./channel.json', 'r', encoding='utf8') as channelFile:
    channelData = json.load(channelFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='gs.', intents=intents)

@bot.event
async def on_ready():
    print(f'>> Guild Channel Setup Bot is on ready')

@bot.is_owner()
@bot.command()
async def Csetup(ctx):
    for index in channelData:
        category = await ctx.guild.create_category(name=index)
        for i in channelData[index]:
            await category.create_text_channel(name=i)

if __name__ == '__main__':
    bot.run(TokenData['Token'])