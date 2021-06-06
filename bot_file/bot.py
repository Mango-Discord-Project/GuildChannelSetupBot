import discord
import json
from discord.ext import commands

with open('./setting/Token.json') as TokenFile:
    TokenData = json.load(TokenFile)

with open('./setting/botSetting.json') as SettingFile:
    SettingData = json.load(SettingFile)

with open('./setting/channel.json', 'r', encoding='utf8') as channelFile:
    channelData = json.load(channelFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=SettingData['Prefix'], intents=intents)

@bot.event
async def on_ready():
    BotName = SettingData['BotName']
    print(f'>> {BotName} is on ready')

@bot.command()
async def Csetup(ctx):
    for index in channelData:
        category = await ctx.guild.create_category(name=index)
        for i in channelData[index]:
            await category.create_text_channel(name=i)

if __name__ == '__main__':
    bot.run(TokenData['Token'])