import random

from bot.bot import Bot
from bot.constants import Colours, Gurks, NEGATIVE_REPLIES
from discord import Embed
from discord.ext import commands


class Gurkify(commands.Cog):
    """Cog for the gurkify command."""

    @commands.command(name="gurkify")
    async def gurkify(self, ctx: commands.Context) -> None:
        """Gurkifying users display name."""
        display_name = ctx.author.display_name

        if len(display_name) > 26:
            embed = Embed(
                title=f"{random.choice(NEGATIVE_REPLIES)}",
                description=(
                    "Your nick name is too long to be gurkified. "
                    "Please change it to be under 26 characters."
                ),
                color=Colours.soft_red,
            )
            await ctx.send(embed=embed)
            return
        else:
            display_name += random.choice(Gurks.gurks)
            await ctx.author.edit(nick=display_name)
            await ctx.send("Done!")


def setup(bot: Bot) -> None:
    """Loads the gurkify cog."""
    bot.add_cog(Gurkify())
