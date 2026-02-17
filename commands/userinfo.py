import discord
from discord.ext import commands
from discord import app_commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="userinfo", description="Select a user and see their information")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member):

        embed = discord.Embed(
            title=f"{user.name}",
            description=f"""
            **ID:** {user.id}
            **Joined:** {user.joined_at.strftime('%Y-%m-%d') if user.joined_at else 'Unknown'}\n
            **Created At:** {user.created_at.strftime('%Y-%m-%d')}
            """,
            color= discord.Color.blurple()
        )

        if user.avatar:
            embed.set_thumbnail(url=user.avatar.url)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(UserInfo(bot))