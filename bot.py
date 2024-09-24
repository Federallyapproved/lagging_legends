import discord
from discord.ext import commands
import requests
import os

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='/')

# Azure Function URL
AZURE_FUNCTION_URL = 'https://therefereebot.azurewebsites.net/api/referee_func?code=Uq01KCalwfazdyjd2ahkUXdjcL9RScITv6jlAek3YPuUAzFueUCGJw%3D%3D'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='TheRef')
async def the_ref(ctx, game_name: str):
    response = requests.get(AZURE_FUNCTION_URL, params={'game_name': game_name})
    if response.status_code == 200:
        await ctx.send(response.text)
    else:
        await ctx.send("Sorry, there was an error retrieving the game rules.")

# Run the bot with token
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
