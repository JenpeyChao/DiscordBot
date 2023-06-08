import discord
from discord.ext import commands
import os
import asyncio
#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog
import tracemalloc

tracemalloc.start()


async def setup(bot):
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

# define an asynchronous main function to start the bot
async def main(bot):
    TOKEN = "ADD YOUR OWN DISCORD BOT TOKEN"
    await setup(bot)
    await bot.login(TOKEN)
    await bot.connect()
    await bot.wait_until_ready()

# start the bot using the asyncio.run() function
if __name__ == '__main__':
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    #remove the default help command so that we can write out own
    bot.remove_command('help')
    asyncio.run(main(bot))
    
