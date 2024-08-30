import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
from quotes import quotes

load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$$', intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
        print(f"Cobra Kai bot is in {guild_count} guilds")
    print(f'We have logged in as {bot.user}')

# Event when a message is sent in a channel the bot is in
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for character in quotes.keys():
        if character in message.content.lower():
            response = random.choice(quotes[character])
            await message.channel.send(f'{character.capitalize()}: {response}')
            break
    
    # Process commands after checking messages so commands will still run
    await bot.process_commands(message)

#Define command for getting a random quote
@bot.command(name='quote')
async def quote(ctx):
    character = random.choice(list(quotes.keys()))
    response = random.choice(quotes[character])
    await ctx.send(f'{character.capitalize()}: {response}')


bot.run(bot_token)