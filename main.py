import discord, os, random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    bot_name = str(bot.user).split('#')[0]
    bot_id = str(bot.user).split('#')[1]

    print(f"Hey! This Bantos, id: {bot_id} in the house 🔥")

    channel = bot.get_channel(596948734093426704)
    embd_msg = discord.Embed(title="Hey! This Bantos in the house 🔥", description="Hey 🖐! This Bantos 🐰, I'm a bot from the Bantu and Bantos community 👾👾👾. Nice to meet you.\n\n\n\n\n", color=0x290805)
    embd_msg.set_author(name=bot_name, url="https://github.com/debjeet-dev/bantos", icon_url="https://raw.githubusercontent.com/debjeet-dev/bantos/21d7293cde48217e9d10cd448b5c897e7796e4e1/bantos.jpg")
    # embd_msg.set_thumbnail(url="https://raw.githubusercontent.com/debjeet-dev/blogIt/main/blogIt_ui.png")
    embd_msg.add_field(name="Commands (start with '/'):", value="\nhello \nbal", inline=True)
    embd_msg.set_footer(text="\n\n\nMade by Debjeet 💖.")

    await channel.send(embed = embd_msg)




random_msg = ["dhur baal 😡🤬", "ki sob bolche 🥴", "haga saala 💩", "chudey chaat babhughat ⚡🔥", "baal er sever baal er host @Sourav01 🤬", "khub khiday pache 🍔🤤"]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith("/"):
        uname = str(message.author).split('#')[0]
        await message.channel.send(f"{uname}, " + random.choice(random_msg))
    await bot.process_commands(message)

@bot.command(name = "coms")
async def hello(ctx):
    await ctx.reply(f"Commands (start with '/'): \nhello \nbal")

@bot.command(name = "hello")
async def hello(ctx):
    uname = ctx.message.author.name
    await ctx.reply(f"Ki re {uname}, bantu! 😃🖐")

@bot.command(name = "bal")
async def baal(ctx):
    uname = ctx.message.author.name
    await ctx.reply(f'{uname}, tui bal 💩🤣')


@bot.command(name = "love")
async def love(ctx):
    await ctx.reply(f"Love u too, {uname}")

bot.run(os.getenv("DISCORD_TOKEN"))
