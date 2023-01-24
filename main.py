import discord
from discord.ext import commands

import settings


def run():

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        ...

    @bot.event
    async def on_message(message: discord.Message):
        ...

    @bot.event
    async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
        ...

    @bot.event
    async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
        ...

    bot.run(settings.DISCORD_TOKEN)


if __name__ == "__main__":
    run()
