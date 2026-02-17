import discord
import time
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.start_time = time.time()

        await self.load_extension("commands.test")
        await self.load_extension("commands.serverinfo")
        await self.load_extension("commands.userinfo")
        await self.load_extension("commands.avatar")
        await self.load_extension("commands.ping")

        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")

bot.run(TOKEN)