import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="avatar", description="Check the avatar of a user")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member):

        embed = discord.Embed(
            title=f"Avatar from @{user.name}",
            timestamp=datetime.utcnow()
        )
        embed.set_image(url=user.avatar.url)

        await interaction.response.send_message(embed=embed)
async def setup(bot):
    await bot.add_cog(Avatar(bot))