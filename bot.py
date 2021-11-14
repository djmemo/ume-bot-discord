import os
import disnake
from disnake.ext import commands

guilds = list(map(str.strip, os.getenv("GUILDS").split(",")))
token = os.getenv("TOKEN")

intents = disnake.Intents(guilds=True, members=True, messages=True, reactions=True)
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("dj!"),
    test_guilds=guilds,
    intents=intents,
    sync_commands_debug=True,
    reload=True,
)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename[:-3]}.")


# When the bot is ready, run this code.
@bot.event
async def on_ready():
    print("The bot is ready!")


bot.run(token)
