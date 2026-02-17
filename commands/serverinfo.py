import discord
from discord.ext import commands
from discord import app_commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="View server metadata")
    async def server(self, interaction: discord.Interaction):

        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return
        
        owner = guild.get_member(guild.owner_id)
        if owner is None:
            owner = await guild.fetch_member(guild.owner_id)

        embed = discord.Embed(
            title=f"# Welcome to {guild.name}",
            description=(
                f"**Server ID:** {guild.id}\n"
                f"**Server Owner:** {owner.mention}\n"
                f"**Members:** {guild.member_count}\n"
                f"**Created at:** {guild.created_at}"
            ),
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
