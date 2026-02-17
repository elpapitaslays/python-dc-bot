import discord
from discord.ext import commands
from discord import app_commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="server", description="View server metadata")
    async def server(self, interaction: discord.Interaction):

        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"Welcome to {guild.name}",
            description=(
                f"Server ID: {guild.id}\n"
                f"Server Owner: {guild.owner}\n"
                f"Members: {guild.member_count}\n"
                f"Created at: {guild.created_at}"
            ),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Server(bot))
