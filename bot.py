import os
import disnake
from disnake.ext import commands

guilds = list(map(int, list(map(str.strip, os.getenv("GUILDS").split(",")))))
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


@commands.is_owner()
@bot.slash_command(default_permissions=False)
async def unload(ctx, extension):
    """Use this to unload cogs. Usage: $unload <cog_name>"""
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Cog {extension} is now unloaded!")


@commands.is_owner()
@bot.slash_command(default_permissions=False)
async def reload(ctx, extension):
    """Use this to reload individual cogs. Usage: $reload <cog_name>"""
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Cog {extension} is now reloaded!")


@commands.is_owner()
@bot.slash_command(default_permissions=False)
async def reloadall(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.reload_extension(f"cogs.{filename[:-3]}")
            await ctx.send(f"Cog {filename[:-3]} is now reloaded!")


bot.run(token)
