import disnake
from disnake.ext import commands


class slash_command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Check bot ping.")
    async def ping(self, inter):
        await inter.response.send_message(
            f"pong ({self.bot.latency*1000}ms)", ephemeral=True
        )


def setup(bot):
    bot.add_cog(slash_command(bot))
