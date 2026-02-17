import discord
from discord.ext import commands
from discord import app_commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def format_uptime(self):
        if not hasattr(self.bot, "start_time"):
            return "Unknown"

        uptime_seconds = int(time.time() - self.bot.start_time)

        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{days}d {hours}h {minutes}m {seconds}s"

    @app_commands.command(name="ping", description="View bot health and latency")
    async def ping(self, interaction: discord.Interaction):

        start = time.perf_counter()

        await interaction.response.defer()

        end = time.perf_counter()

        api_latency = round((end - start) * 1000)
        gateway_latency = round(self.bot.latency * 1000)
        uptime = self.format_uptime()

        if gateway_latency < 120:
            status = "🟢 Excellent"
        elif gateway_latency < 250:
            status = "🟡 Good"
        else:
            status = "🔴 High latency"

        embed = discord.Embed(
            title="🏓 Pong — Bot Health",
            color=discord.Color.blurple()
        )

        embed.add_field(name="Gateway Latency", value=f"{gateway_latency} ms")
        embed.add_field(name="API Latency", value=f"{api_latency} ms")
        embed.add_field(name="Uptime", value=uptime, inline=False)
        embed.add_field(name="Status", value=status, inline=False)

        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))