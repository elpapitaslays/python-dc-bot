import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def coin(ctx):
    num = random.randint(1,2)
    answer = ""
    if num == 1:
        answer = "Moneda de Oro!"
    else:
        answer = "Moneda de Plata!"
    await ctx.send(answer)

bot.run(token)