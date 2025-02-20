import discord
from discord.ext import commands

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

bot = commands.Bot(command_prefix=".", intents=permissoes)
# o prefixo para chamar o bot é um "." como dito na linha acima

@bot.command()
async def ola(ctx:commands.context):
    await ctx.reply("O Pai ta on PORRA")










bot.run("MTI3NjMxMTMyODY0MTc3Nzc3NA.G9jjM5.SOrj28-47J0cx5P-Ckqij17Zd1VECNoyx1cVtU")


