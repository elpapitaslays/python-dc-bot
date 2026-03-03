import discord
from discord.ext import commands
from discord import app_commands

class Handwash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="handwash", description="Learn how to wash your hands")
    async def wash(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🧼 Handwashing Guide",
            description=(
                "**Step 1 — Wet Hands**\n"
                "Use clean, running water (warm or cold) and apply soap.\n\n"

                "**Step 2 — Lather**\n"
                "Rub hands together thoroughly. Cover backs of hands, between fingers, and under nails.\n\n"

                "**Step 3 — Scrub (20 Seconds)**\n"
                "Scrub for at least **20 seconds** to effectively remove germs.\n\n"

                "**Step 4 — Rinse**\n"
                "Rinse well under clean, running water.\n\n"

                "**Step 5 — Dry**\n"
                "Use a clean towel or air dry completely.\n\n"

                "━━━━━━━━━━━━━━━━━━\n"
                "**Wash Your Hands:**\n"
                "• Before eating or preparing food\n"
                "• After using the restroom\n"
                "• After coughing or sneezing\n"
                "• After touching public surfaces\n"
                "• After handling trash"
            ),
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Handwash(bot))