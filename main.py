import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import cooldown
from discord.ext.commands import CommandOnCooldown
from discord.ext import menus
import time
import random
import json
import aiohttp
import datetime
from datetime import datetime
import requests
import asyncio
from googletrans import Translator
import levelsys
import string
import pymongo
import pytemperature

cogs = [levelsys]

myclient = pymongo.MongoClient("mongodb+srv://Mako:Mko-3270@cluster0.oigbj.mongodb.net/MakoBot?retryWrites=true&w=majority")
mydb = myclient["makobotdb"]
mainbank = mydb["bank"]
enter = mydb["enterpreneurship"]
crequests = mydb["requests"]

def get_prefix(client, message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

class helpcommand(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        embed = discord.Embed(title="Help Commands Page One", colour=discord.Colour.blue())
        embed.add_field(name="ping", value="`Checks the bot ping`", inline=False)
        embed.add_field(name="Mako", value="`Adore the bot creator`", inline=False)
        embed.add_field(name="h", value="`hhhhhhh`", inline=False)
        embed.add_field(name="yorkie", value="`My beloved :heart:`", inline=False)
        embed.add_field(name="hackme", value="`I will hack you`", inline=False)
        embed.add_field(name="howgoodareyou", value="`Ask me how good am I`", inline=False)
        embed.add_field(name="whoareyou", value="`Check who am I`", inline=False)
        embed.add_field(name="userinfo", value="`Make me doxx an user`", inline=False)
        embed.add_field(name="8ball", value="`Answers from the beyond`", inline=False)
        embed.add_field(name="star", value="`Giving away free stars!`", inline=False)
        embed.add_field(name="love", value="`*May I be your valentine?*`", inline=False)
        embed.add_field(name="btc", value="`Checks the bitcoin price`", inline=False)
        embed.add_field(name="putin", value="`veri thicc`", inline=False)
        embed.add_field(name="cat", value="`cute cat pics owo`", inline=False)
        embed.add_field(name="dog", value="`cute doggo pics *bark*`", inline=False)
        embed.add_field(name="weather", value="`Check the temperature for any place in the world!`", inline=False)
        embed.add_field(name="translate", value="`Translate English to any language!`", inline=False)
        embed.add_field(name="tesla", value="`very s3xy. check out yourself`", inline=False)
        embed.add_field(name="getsomehelp", value="`Stop it`", inline=False)
        embed.add_field(name="ineedhelp", value="`Are you sure you need-`", inline=False)
        embed.add_field(name="hentai", value="`bet you'll fap`", inline=False)
        embed.add_field(name="rickroll", value="`Rickroll yourself`", inline=False)
        embed.add_field(name="build", value="`Version of the bot, coming-soon commands and more info!`", inline=False)
        embed.add_field(name="metar", value="`Access metar of an airport (ICAO code required)`", inline=False)
        embed.set_footer(text="Add the reaction to swipe pages!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820737057693499415/824901552967909376/mako_bot.png")
        return await channel.send(embed=embed)

    @menus.button('1️⃣')
    async def on_page_one(self, payload):
        embed_a = discord.Embed(title="Callisto Help Center 1 - Fun", colour=discord.Colour.blue())
        embed_a.add_field(name="ping", value="`Checks the bot ping`", inline=False)
        embed_a.add_field(name="Mako", value="`Adore the bot creator`", inline=False)
        embed_a.add_field(name="h", value="`hhhhhhh`", inline=False)
        embed_a.add_field(name="yorkie", value="`My beloved :heart:`", inline=False)
        embed_a.add_field(name="hackme", value="`I will hack you`", inline=False)
        embed_a.add_field(name="howgoodareyou", value="`Ask me how good am I`", inline=False)
        embed_a.add_field(name="whoareyou", value="`Check who am I`", inline=False)
        embed_a.add_field(name="userinfo", value="`Make me doxx an user`", inline=False)
        embed_a.add_field(name="8ball", value="`Answers from the beyond`", inline=False)
        embed_a.add_field(name="star", value="`Giving away free stars!`", inline=False)
        embed_a.add_field(name="love", value="`*May I be your valentine?*`", inline=False)
        embed_a.add_field(name="btc", value="`Checks the bitcoin price`", inline=False)
        embed_a.add_field(name="putin", value="`veri thicc`", inline=False)
        embed_a.add_field(name="cat", value="`cute cat pics owo`", inline=False)
        embed_a.add_field(name="dog", value="`cute doggo pics *bark*`", inline=False)
        embed_a.add_field(name="weather", value="`Check the temperature for any place in the world!`", inline=False)
        embed_a.add_field(name="translate", value="`Translate English to any language!`", inline=False)
        embed_a.add_field(name="tesla", value="`very s3xy. check out yourself`", inline=False)
        embed_a.add_field(name="getsomehelp", value="`Stop it`", inline=False)
        embed_a.add_field(name="ineedhelp", value="`Are you sure you need-`", inline=False)
        embed_a.add_field(name="hentai", value="`bet you'll fap`", inline=False)
        embed_a.add_field(name="rickroll", value="`Rickroll yourself`", inline=False)
        embed_a.add_field(name="build", value="`Version of the bot, coming-soon commands and more info!`", inline=False)
        embed_a.add_field(name="metar", value="`Access metar of an airport (ICAO code required)`", inline=False)
        embed_a.set_footer(text="Add a reaction to swipe pages!")
        embed_a.set_thumbnail(url="https://cdn.discordapp.com/attachments/820737057693499415/824901552967909376/mako_bot.png")
        await self.message.edit(embed=embed_a)
        channel = client.get_channel(payload.channel_id)
        messg = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await messg.remove_reaction("1️⃣", user)

    @menus.button('2️⃣')
    async def on_page_two(self, payload):
        embed = discord.Embed(title="Callisto Help Center 2 - Fun", colour=discord.Colour.blue())
        embed.add_field(name="penismusic", value="`penis music`", inline=False)
        embed.add_field(name="windoge", value="`most best system`", inline=False)
        embed.add_field(name="gamestop", value="`stonks`", inline=False)
        embed.add_field(name="fight", value="`Fight a user and see who wins!`", inline=False)
        embed.add_field(name="ban", value="`Remember I'm not a moderating bot...`", inline=False)
        embed.add_field(name="amogus", value="`amogus`", inline=False)
        embed.add_field(name="hi", value="`hi`", inline=False)
        embed.add_field(name="woah", value="`WOOOAAA`", inline=False)
        embed.add_field(name="slap", value="`Slap someone lol.`", inline=False)
        embed.add_field(name="channelstats", value="`Make me doxx a channel`", inline=False)
        embed.add_field(name="whymathisuseless", value="`Send this to your math teacher`", inline=False)
        embed.add_field(name="imagine", value="`yes, imagein`", inline=False)
        embed.add_field(name="why", value="`Why?`", inline=False)
        embed.add_field(name="whynot", value="`Why not?`", inline=False)
        embed.add_field(name="doyoureallyloveme", value="`Do I really love you?`", inline=False)
        embed.add_field(name="bored", value="`Being bored is the worst.`", inline=False)
        embed.add_field(name="fun", value="`Have fun!`", inline=False)
        embed.add_field(name="bestbot", value="`who's the best bot?`", inline=False)
        embed.add_field(name="encode", value="`Encode binary`", inline=False)
        embed.add_field(name="decode", value="`Decode binary`", inline=False)
        embed.add_field(name="thanks", value="`Special thanks`", inline=False)
        embed.add_field(name="bean", value="`Be a cool kid(minimod) and bean someone!`", inline=False)
        embed.add_field(name="whysomanyfuncommands", value="`I myself don't know that, ask mako`", inline=False)
        embed.set_footer(text="Add a reaction to swipe pages!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820737057693499415/824901552967909376/mako_bot.png")
        await self.message.edit(embed=embed)
        channel = client.get_channel(payload.channel_id)
        messg = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await messg.remove_reaction("2️⃣", user)

    @menus.button('3️⃣')
    async def on_page_three(self, payload):
        embed = discord.Embed(title="Callisto Help Center 3 - Animals", colour=discord.Colour.blue())
        embed.add_field(name="dogimage", value="`Show a random image of a dog!`", inline=False)
        embed.add_field(name="catimage", value="`Show a random image of a cat!`", inline=False)
        embed.add_field(name="foximage", value="`Show a random image of a fox!`", inline=False)
        embed.add_field(name="birdimage", value="`Show a random image of a bird!`", inline=False)
        embed.add_field(name="koalaimage", value="`Show a random image of a koala!`", inline=False)
        embed.add_field(name="pandaimage", value="`Show a random image of a panda!`", inline=False)
        embed.add_field(name="redpandaimage", value="`Show a random image of a red panda!`", inline=False)
        embed.add_field(name="dogfact", value="`Show a random fact about dog!`", inline=False)
        embed.add_field(name="catfact", value="`Show a random fact about cat!`", inline=False)
        embed.add_field(name="foxfact", value="`Show a random fact about fox!`", inline=False)
        embed.add_field(name="birdfact", value="`Show a random fact about bird!`", inline=False)
        embed.add_field(name="koalafact", value="`Show a random fact about koala!`", inline=False)
        embed.add_field(name="pandafact", value="`Show a random fact about panda!`", inline=False)
        embed.set_footer(text="Add a reaction to swipe pages!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820737057693499415/824901552967909376/mako_bot.png")
        await self.message.edit(embed=embed)
        channel = client.get_channel(payload.channel_id)
        messg = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await messg.remove_reaction("3️⃣", user)

    @menus.button('4️⃣')
    async def on_page_four(self, payload):
        embed = discord.Embed(title="Callisto Help Center 4 - Economy", colour=discord.Colour.blue())
        embed.add_field(name="balance", value="`Check your balance!`", inline=False)
        embed.add_field(name="deposit", value="`Deposit money from wallet to bank.`", inline=False)
        embed.add_field(name="withdraw", value="`Withdraw money from bank to wallet`", inline=False)
        embed.add_field(name="send", value="`Send somebody money from bank account`", inline=False)
        embed.add_field(name="shop", value="`View shop`", inline=False)
        embed.add_field(name="bag", value="`Check which items do you have`", inline=False)
        embed.add_field(name="buy", value="`Buy something from the shop`", inline=False)
        embed.add_field(name="sell", value="`Sell something from the shop`", inline=False)
        embed.add_field(name="work", value="`Work (to work you need to have right item from the shop)`", inline=False)
        embed.add_field(name="search", value="`Search for free money!`", inline=False)
        embed.add_field(name="rob", value="`Rob someone!`", inline=False)
        embed.add_field(name="slots", value="`Bet your money on slots`", inline=False)
        embed.add_field(name="economyleaderboard", value="`Check the top 10 players!`", inline=False)
        embed.add_field(name="beg", value="`Beg for money`", inline=False)
        embed.set_footer(text="Add a reaction to swipe pages!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820737057693499415/824901552967909376/mako_bot.png")
        await self.message.edit(embed=embed)
        channel = client.get_channel(payload.channel_id)
        messg = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await messg.remove_reaction("4️⃣", user)

    @menus.button('5️⃣')
    async def on_page_five(self, payload):
        embed = discord.Embed(title="Callisto Help Center", colour=discord.Colour.blue())
        embed.add_field(name="Remember this bot is still in beta testing.", value="Do not blame me if something fails.",inline=False)
        embed.set_footer(text="This isn't really a help page, more like Mako explaning himself why he's so lazy and doesn't want to properly code me :(")
        await self.message.edit(embed=embed)
        channel = client.get_channel(payload.channel_id)
        messg = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await messg.remove_reaction("5️⃣", user)


client = commands.Bot(command_prefix = "+", help_command=None, intents=discord.Intents.all())
TOKEN = 'ODIwNTcwOTE0ODMxODU5NzEy.YE3GNw.jZYQYgV2OYSV2KAlM-TfJTkZ8Q8' #real token doe no leak or bot is ded 💀


themainshop = [{"displayname":"🧻 Toilet Paper","name":"toilet_paper","price":1000,"description":"Work as Toilet Paper Handler!","workcom":"+work Toilet Paper"},
            {"displayname":"🧹 Vacuum","name":"vacuum","price":5000,"description":"Work as house cleaner!","workcom":"+work Cleaner"},
            {"displayname":"🏡 Lawn Mower","name":"lawn_mower","price":5000,"description":"Work as gardener!","workcom":"+work Gardener"},
            {"displayname":"🖥️ PC","name":"pc","price":10000,"description":"Unlock more work possibilities!","workcom":None},
            {"displayname":"🚗 Car Mechanic Degree","name":"car_mechanic","price":15000,"description":"Work on fixing cars!","workcom":"+work Car Mechanic"},
            {"displayname":"⌨️ Keyboard","name":"keyboard","price":15000,"description":"Work as copywriter! Caution: PC needed.","workcom":"+work Copywriter"},
            {"displayname":"🖱️ Mouse","name":"mouse","price":15000,"description":"Work on survey completing! Caution: PC needed.","workcom":"+work Survey"},
            {"displayname":"🎮 Game","name":"game","price":100000,"description":"Work as pro gamer! Caution: PC needed.","workcom":"+work Gamer"},
            {"displayname":"*www.* Website","name":"website","price":100000,"description":"Work as blogger! Caution: PC needed.","workcom":"+work Blogger"},
            {"displayname":"🛍️ Shopily","name":"shopily","price":500000,"description":"Work as dropshipper! Caution: PC and website needed.","workcom":"+work Dropshipper"},
            {"displayname":"✈️ Pilot License","name":"pilot_license","price":1000000,"description":"Work as a pilot!.","workcom":"+work Pilot"},
            {"displayname":"⚖️ Lawyer Degree","name":"lawyer","price":1000000,"description":"Work as lawyer!","workcom":"+work Lawyer"},
            {"displayname":"🩺 Doctor Certificate","name":"doctor","price":1000000,"description":"Work as doctor!","workcom":"+work Doctor"},
            {"displayname":"📈 Financial Analytic","name":"finance","price":5000000,"description":"Work as financial analytic!","workcom":"+work Finance"},]

themultiplierlist = [{"name":"fly","displayname":"Fly","description":"Fly helps you with working, giving you a 1% boost!","rarity":"common"},
                     {"name":"mosquito","displayname":"Mosquito","description":"Mosquito threatens your boss to give you more money, so you get 1% pay raise!","rarity":"common"},
                     {"name":"ladybird","displayname":"Ladybird","description":"Ladybird motivates you to work, and you work for 1% more!","rarity":"common"},
                     {"name":"spider","displayname":"Spider","description":"Spider scares you, but it also scares your boss, so he gave you 1% more to have you take your spider away","rarity":"common"},
                     {"name":"mouse","displayname":"Mouse","description":"Mouse helps you with carrying stuff, so you work more effectively and get paid 1% more","rarity":"common"},
                     {"name":"salmon","displayname":"Salmon","description":"Salmon catches you fish, so you can work 3% more effectively.","rarity":"uncommon"},
                     {"name":"newton","displayname":"Newton","description":"His cuteness gives you 100% boost on everything!","rarity":"mythic"}]

@client.event
async def on_ready(ctx):
    ctx.send('Bot is online!')

@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, CommandOnCooldown):
        if 60 < exc.retry_after <= 3599:
            embed = discord.Embed(title="Woah what a fast typer!", colour=discord.Colour.red())
            embed.add_field(name="Now, chill down, dude", value=f"This command is on cooldown, try again in {exc.retry_after/60:,.0f} minutes!")
            embed.set_footer(text="This is a cooldown message.")
            await ctx.send(embed=embed)
        elif 3600 <= exc.retry_after <= 86399:
            embed = discord.Embed(title="Woah what a fast typer!", colour=discord.Colour.red())
            embed.add_field(name="Now, chill down, dude", value=f"This command is on cooldown, try again in {exc.retry_after/3600:,.0f} hours!")
            embed.set_footer(text="This is a cooldown message.")
            await ctx.send(embed=embed)
        elif 86400 <= exc.retry_after:
            embed = discord.Embed(title="Woah what a fast typer!", colour=discord.Colour.red())
            embed.add_field(name="Now, chill down, dude", value=f"This command is on cooldown, try again in {exc.retry_after /86400:,.0f} days!")
            embed.set_footer(text="This is a cooldown message.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Woah what a fast typer!", colour=discord.Colour.red())
            embed.add_field(name="Now, chill down, dude", value=f"This command is on cooldown, try again in {exc.retry_after:,.0f} seconds!")
            embed.set_footer(text="This is a cooldown message.")
            await ctx.send(embed=embed)

@client.event
async def on_ready():
    activeServers = client.guilds
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Over {sum} users!'))

@client.command()
async def usercount(ctx):
    activeServers = client.guilds
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    await ctx.send(f"Over {sum} people are using me!")

@client.event
async def on_guild_join(guild):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "+"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

    await ctx.send(f"The prefix was changed to {prefix}")

@client.command()
async def help(ctx, argument=None):
    if argument == None:
        em=discord.Embed(title="Callisto Help Center", description="Reply to this message with an argument to get help of a specific category!", colour=discord.Colour.random())
        em.add_field(name="⚒️ Utility", value="Write `u`")
        em.add_field(name="😜 Fun", value="Write `f`")
        em.add_field(name="🐶 Animals", value="Write `a`")
        em.add_field(name="🏦 Economy", value="Write `e`")
        em.add_field(name="🤡 Other useless stuff", value="Write `o`")
        foredit = await ctx.send(embed=em)
        msg = await client.wait_for("message")
        if msg.content == "u" or msg.content == "utility":
            embed=discord.Embed(title="⚒️ Utility", description="", colour=discord.Colour.random())
            embed.add_field(name="ping", value="`Checks the bot ping`", inline=False)
            embed.add_field(name="btc", value="`Checks the bitcoin price`", inline=False)
            embed.add_field(name="weather", value="`Check the temperature for any place in the world!`", inline=False)
            embed.add_field(name="translate", value="`Translate English to any language!`", inline=False)
            embed.add_field(name="build", value="`Version of the bot, coming-soon commands and more info!`",inline=False)
            embed.add_field(name="metar", value="`Access metar of an airport (ICAO code required)`", inline=False)
            embed.add_field(name="encode", value="`Encode binary`", inline=False)
            embed.add_field(name="decode", value="`Decode binary`", inline=False)
            embed.add_field(name="support", value="`Access Calisto support`", inline=False)
            embed.add_field(name="channelstats", value="`See stats of a channel`", inline=False)
            embed.add_field(name="covid", value="`See the covid stats of a country!`", inline=False)
            embed.add_field(name="feedback", value="Send feedback!", inline=False)
            embed.add_field(name="invite", value="`Invite the bot to your server!`", inline=False)
            await foredit.edit(embed=embed)
        if msg.content == "f" or msg.content == "fun":
            embed = discord.Embed(title="😜 Fun", description="", colour=discord.Colour.random())
            embed.add_field(name="8ball", value="`Answers from the beyond`", inline=False)
            embed.add_field(name="fight", value="`Fight a user and see who wins!`", inline=False)
            embed.add_field(name="cat", value="`cute cat pics owo`", inline=False)
            embed.add_field(name="dog", value="`cute doggo pics *bark*`", inline=False)
            embed.add_field(name="meme", value="`Show a random meme.`", inline=False)
            embed.add_field(name="howgay", value="`Check how gay is a user! (this command isn't meant to insult any of the LGBTQ+ community members, we're not homophobic!)`", inline=False)
            embed.add_field(name="calculator", value="`Calculate something!`", inline=False)
            embed.add_field(name="reverse", value="`Reverse a text!`", inline=False)
            embed.add_field(name="nitro", value="`Send a random nitro!`", inline=False)
            embed.add_field(name="rockpaperscissors", value="`Play rock paper scissors!`")
            await foredit.edit(embed=embed)
        if msg.content == "a" or msg.content == "animals":
            embed = discord.Embed(title="🐶 Animals", description="", colour=discord.Colour.random())
            embed.add_field(name="dogimage", value="`Show a random image of a dog!`", inline=False)
            embed.add_field(name="catimage", value="`Show a random image of a cat!`", inline=False)
            embed.add_field(name="foximage", value="`Show a random image of a fox!`", inline=False)
            embed.add_field(name="birdimage", value="`Show a random image of a bird!`", inline=False)
            embed.add_field(name="koalaimage", value="`Show a random image of a koala!`", inline=False)
            embed.add_field(name="pandaimage", value="`Show a random image of a panda!`", inline=False)
            embed.add_field(name="redpandaimage", value="`Show a random image of a red panda!`", inline=False)
            embed.add_field(name="dogfact", value="`Show a random fact about dog!`", inline=False)
            embed.add_field(name="catfact", value="`Show a random fact about cat!`", inline=False)
            embed.add_field(name="foxfact", value="`Show a random fact about fox!`", inline=False)
            embed.add_field(name="birdfact", value="`Show a random fact about bird!`", inline=False)
            embed.add_field(name="koalafact", value="`Show a random fact about koala!`", inline=False)
            embed.add_field(name="pandafact", value="`Show a random fact about panda!`", inline=False)
            await foredit.edit(embed=embed)
        if msg.content == "e" or msg.content == "economy":
            embed = discord.Embed(title="🏦 Economy", description="", colour=discord.Colour.random())
            embed.add_field(name="balance", value="`Check your balance!`", inline=False)
            embed.add_field(name="deposit", value="`Deposit money from wallet to bank.`", inline=False)
            embed.add_field(name="withdraw", value="`Withdraw money from bank to wallet`", inline=False)
            embed.add_field(name="send", value="`Send somebody money from bank account`", inline=False)
            embed.add_field(name="shop", value="`View shop`", inline=False)
            embed.add_field(name="bag", value="`Check which items do you have`", inline=False)
            embed.add_field(name="buy", value="`Buy something from the shop`", inline=False)
            embed.add_field(name="sell", value="`Sell something from the shop`", inline=False)
            embed.add_field(name="work", value="`Work (to work you need to have right item from the shop)`", inline=False)
            embed.add_field(name="search", value="`Search for free money!`", inline=False)
            embed.add_field(name="rob", value="`Rob someone!`", inline=False)
            embed.add_field(name="slots", value="`Bet your money on slots`", inline=False)
            embed.add_field(name="economyleaderboard", value="`Check the top 10 players!`", inline=False)
            await foredit.edit(embed=embed)
            await foredit.add_reaction("⬅️")
            await foredit.add_reaction("➡️")
            def check(reaction, user):
                return user == ctx.author
            reaction, user = await client.wait_for('reaction_add', check=check)
            if str(reaction.emoji) == '➡️':
                embed1 = discord.Embed(title="🏦 Economy Page 2", description="", colour=discord.Colour.random())
                embed1.add_field(name="beg", value="`Beg for money`", inline=False)
                embed1.add_field(name="hunt", value="`Hunt for pets!`", inline=False)
                embed1.add_field(name="multipliers", value="`Show all your multipliers!`", inline=False)
                embed1.add_field(name="dice", value="`Roll a dice`", inline=False)
                embed1.add_field(name="horsebet", value="`Bet on horses with someone!`", inline=False)
                embed1.add_field(name="fish", value="`Fish for coins! (salmon pet required)`", inline=False)
                embed1.add_field(name="bankrob", value="`Attempt to rob 10% of somebody's bank (spider pet required)`", inline=False)
                embed1.add_field(name="roulette", value="`Roll a roulette! (warning: advanced command, make sure you understand how roulette works!)`", inline=False)
                embed1.add_field(name="createcompany", value="`Create a company for 25m coins`", inline=False)
                embed1.add_field(name="employ", value="`Send a work offer to a user (only for enterpreneurs)`", inline=False)
                embed1.add_field(name="request", value="`Accept or reject a work offer`", inline=False)
                embed1.add_field(name="cwithdraw", value="`Withdraw all company's revenue`", inline=False)
                await foredit.edit(embed=embed1)
            if str(reaction.emoji) == '⬅️':
                embed = discord.Embed(title="🏦 Economy", description="", colour=discord.Colour.random())
                embed.add_field(name="balance", value="`Check your balance!`", inline=False)
                embed.add_field(name="deposit", value="`Deposit money from wallet to bank.`", inline=False)
                embed.add_field(name="withdraw", value="`Withdraw money from bank to wallet`", inline=False)
                embed.add_field(name="send", value="`Send somebody money from bank account`", inline=False)
                embed.add_field(name="shop", value="`View shop`", inline=False)
                embed.add_field(name="bag", value="`Check which items do you have`", inline=False)
                embed.add_field(name="buy", value="`Buy something from the shop`", inline=False)
                embed.add_field(name="sell", value="`Sell something from the shop`", inline=False)
                embed.add_field(name="work", value="`Work (to work you need to have right item from the shop)`", inline=False)
                embed.add_field(name="search", value="`Search for free money!`", inline=False)
                embed.add_field(name="rob", value="`Rob someone!`", inline=False)
                embed.add_field(name="slots", value="`Bet your money on slots`", inline=False)
                await foredit.edit(embed=embed)
        if msg.content == "o" or msg.content == "others":
            embed = discord.Embed(title="🤡 Other useless stuff", description="", colour=discord.Colour.random())
            embed.add_field(name="Too many to add description for each lol", value="`mako, qlaudie, bluejay, plyut, blurjay, aeroboy, floppa. h, yorkie, hackme, howgoodareyou, whoareyou, star, love, putin, tesla, getsomehelp, ineedhelp, hentai, rickroll, build, penismusic, windoge, gamestop, ban, amogus, hi, woah, slap, whymathisuseless, imagine, why, why not, doyoureallyloveme, bored, fun, testbot, thanks, whysomanyfuncommands`")
            await foredit.edit(embed=embed)

@client.command()
async def oldhelp(ctx):
    if ctx.author.id == 414829561621118977:
        m = helpcommand()
        await m.start(ctx)
    else:
        await ctx.send("Can't use this command as it's private and exclusive to the staff!")

@client.command()
async def dbcheck(ctx):
    print(mydb.list_collection_names())
    await ctx.send("Done!")

@client.command()
async def chkl(ctx):
    x = mainbank.find_one({"testing":"test"})

    await ctx.send(str(x))

@client.command()
async def callisto(ctx):
    await ctx.send('Callisto means "The most beautiful"')

@client.command()
async def servercount(ctx):
    await ctx.send(f"I am right now in {str(len(client.guilds))} servers!")

@client.event
async def on_message(message):
    if message.author.client:
        return
    if "fuck you" in message.content or "gtfo" in message.content or "fuck u" in message.content or "get the fuck off" in message.content or "shut up" in message.content or "shut the fuck up" in message.content or "stfu" in message.content or "shut the up" in message.content:
        await message.channel.send('no u')
    if message.content == "Hello":
        await message.channel.send("Hello!")
    await client.process_commands(message)

@client.command()
async def uptheb(ctx):
    await updatethebank(ctx.author, 100)
    await ctx.send("Done!")

async def updatethebank(user: discord.User, change=0, mode=None):
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]
    bank_amt = doc["bank"]

    change = bank_amt + change

    if mode == None:
        mode = "bank"
    elif mode == "wallet":
        mode = "wallet"
    elif mode == "bank":
        mode = "bank"
    else:
        mode = "bank"

    new = {"$set": {mode:change}}

    mainbank.update_one(doc, new)

@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(f'Pong: {round(client.latency * 1000)}ms!')

@client.command(aliases=['Mako','Owner'])
async def mako(ctx):
    await ctx.send(f'Mako is the best!')

@client.command(aliases=['Qlaudie','klaudia'])
async def qlaudie(ctx):
    await ctx.send(f'Qlaudie is the best!')

@client.command()
async def bluejay(ctx):
    await ctx.send(f"https://cdn.discordapp.com/attachments/817709756646817794/826354173762600970/sfw_fixed_01-29-2011-223.jpg")

@client.command(aliases=['H'])
async def h(ctx):
    await ctx.send(f'https://tenor.com/view/h-apple-apple-h-apple-gif-18834689')

@client.command(aliases=['Plyut'])
async def plyut(ctx, user : discord.Member=None):
    if user == None:
        await ctx.send(f'Plyut is best, worship plyut, if you dont worship plyut, you will banned')
    else:
        await ctx.send(f'{user.mention}, plyut is best, worship plyut, if you dont worship plyut, you will banned')

@client.command(aliases=['Blurjay'])
async def blurjay(ctx):
    await ctx.send(f'syop insluting bluejay.')
    await ctx.send(f'fuck off you shit')

@client.command()
async def coinflip(ctx):
    rn = random.randint(1, 2)
    if rn == 1:
        await ctx.send("Heads!")
    if rn == 2:
        await ctx.send("Tails!")

@client.command(aliases=['yorkie'])
async def newton(ctx):
    await ctx.send(f'my beloved :heart: https://cdn.discordapp.com/attachments/817709756646817794/820696533216526406/image0.jpg')

@client.command(aliases=['hack','Hackme','Hack'])
async def hackme(ctx):
    m1=await ctx.send(f'Hacking you: 10% █▒▒▒▒▒▒▒▒▒▒▒▒▒')
    time.sleep(1)
    await m1.edit(content='Hacking you: 30% ███▒▒▒▒▒▒▒▒▒▒')
    time.sleep(1)
    await m1.edit(content='Hacking you: 69% ███████▒▒▒▒')
    time.sleep(1)
    await m1.edit(content='Hacking you: 90% █████████▒')
    time.sleep(3)
    await m1.edit(content='Successifully stole your IP!')
    time.sleep(1)
    await ctx.send(f'Your IP is ||get spoilerrolled||')

@client.command(aliases=['Areyougood','howgoodareyou','howgood','Howgoodareyou','Howgood'])
async def areyougood(ctx):
    await ctx.send(f'Bruh, I am the best bot in the world. I am way better than you and than anyone. Nobody will ever beat me in my amazingness.')

@client.command(aliases=['whoyou','whoru','Whoareyou','introduceyourself','whoare'])
async def whoareyou(ctx):
    await ctx.send(f'I am yet another general entertainment bot, created by Mako#6252. It is still in development, do not expect me to be like all these MEE7 or sth. I am greater than them tho.')

@client.command()
async def howgay(ctx, user:discord.User=None):
    if user == None:
        embed = discord.Embed(title=f"How gay is {ctx.author}?", colour=discord.Colour.blue())
        embed.add_field(name=f"{ctx.author} is `{random.randrange(1, 100)}%` gay!", value="-=-=-=-=-=-", inline=False)
        embed.set_footer(text="Callisto Gay Checker")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"How gay is {user}?", colour=discord.Colour.blue())
        embed.add_field(name=f"{user} is `{random.randrange(1, 100)}%` gay!", value="-=-=-=-=-=-", inline=False)
        embed.set_footer(text="Callisto Gay Checker")
        await ctx.send(embed=embed)

@client.command(aliases=["ui"])
async def userinfo(ctx, Member:discord.Member=None):
    if Member == None:
        Member = ctx.author
    else:
        Member = Member
    e = discord.Embed(title=f"I doxxed {Member.display_name}", color=discord.Colour.blue())
    e.add_field(name="The most important role:", value=f"{Member.top_role}", inline=False)
    e.add_field(name="Username:", value=f"{Member.display_name}", inline=False)
    e.add_field(name="ID:", value=f"{Member.id}", inline=False)
    e.add_field(name="Cool dude since:", value=f"{Member.premium_since}", inline=False)
    e.add_field(name="Global Username:", value=f"{Member}", inline=False)
    e.add_field(name="Joined", value=Member.joined_at.strftime("%a, %d %B %Y, %I:%M %P UTC"), inline=False)
    e.add_field(name="Registered", value=Member.created_at.strftime("%a, %d %B %Y, %I:%M %P UTC"), inline=False)
    e.set_thumbnail(url=Member.avatar_url)
    await ctx.send(embed=e)

@client.command(aliases=['8ball','answer','Eightball','roll'])
async def eightball(ctx):
    possible_responses = [
        'Most likely no',
        'I do not think that yes',
        'In my opinion no',
        'Quite possible',
        'It is quite possible',
        'Quite hard to tell',
        'Too hard to tell',
        'Definetly',
        'Surely',
        'Not sure',
        'Bruh',
        'Nah',
        'Aye',
        'Nay',
        'Nope.',
        'Yeah',
        'I do believe that yes',
        'I dont really think that yes',
        'For sure not',
        'It is not a question worth asking',
        'Possible',
        'Yes, but actually no.',
    ]
    await ctx.send(random.choice(possible_responses) + ", " +
         ctx.message.author.mention)

@client.command()
async def floppa(ctx):
    await ctx.send(f"https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053")

@client.command(aliases=['Star','starme','starthis','Starme'])
async def star(ctx):
    await ctx.message.add_reaction('⭐')

@client.command(aliases=['Love','doyouloveme','youloveme','doyoulove'])
async def love(ctx):
    await ctx.message.add_reaction('❤️')
    await ctx.send(f'I love you so much! :sparkling_heart:')

@client.command(aliases=['btc'])
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed=discord.Embed(title="", colour=discord.Colour.blue())
        embed.add_field(name="Bitcoin is right now at:", value="$" + response['bpi']['USD']['rate'])
        await ctx.send(embed=embed)

@client.command()
async def putin(ctx):
    await ctx.send("https://tenor.com/blmiu.gif thicc")

@client.command()
async def nerd(ctx):
    await ctx.send("\"Nerd, what a name, its like he is copying someone? No, that can't be, he's a nerd, and he's original.\" - \"Nerd\"")

@client.command()
async def welcome(ctx, user:discord.User = None):
    if user == None:
        await ctx.send(f"Welcome everyone! Have a great time here!")
    else:
        await ctx.send(f"Warm welcome to {user.mention}!")

@client.command()
async def calculator(ctx, ctype, number1:int, number2:int):
    if ctype == "+" or ctype == "add" or ctype == "addition":
        embed = discord.Embed(title="Callisto Calculator", description=f"The result of the equation is {number1 + number2}")
        await ctx.send(embed=embed)
    if ctype == "-" or ctype == "subtract" or ctype == "minus":
        embed = discord.Embed(title="Callisto Calculator", description=f"The result of the equation is {number1 - number2}")
        await ctx.send(embed=embed)
    if ctype == "*" or ctype == "multiply" or ctype == "multiplication":
        embed = discord.Embed(title="Callisto Calculator", description=f"The result of the equation is {number1 * number2}")
        await ctx.send(embed=embed)
    if ctype == "/" or ctype == "divide" or ctype == "division":
        embed = discord.Embed(title="Callisto Calculator", description=f"The result of the equation is {number1 / number2}")
        await ctx.send(embed=embed)

@calculator.error
async def calculator_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+calculator <type> <number1> <number2>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as s:
        async with s.get("https://api.ksoft.si/images/random-image", params={"tag": "cat"}, headers={"Authorization": f"Bearer a43660a9f4c73f5f2d8aea7b3a8697d3b6652b41"}) as resp:
            data = await resp.json()

    await ctx.send(f'Ya want some cute cat pics?')

    time.sleep(1)

    await ctx.send(f'Heres one owo:')

    embed = discord.Embed(colour=discord.Colour.blue())

    embed.set_image(url=data["url"])

    await ctx.send(embed=embed)

@client.command()
async def support(ctx):
    ticketer = ctx.author
    embed = discord.Embed(title=f"Support system is used to contact a Callisto helper privately using MakoBot DMs.",
                          description=f"If you want to proceed - react with ✅, if not - react with ❌")
    ask = await ctx.send(embed=embed)
    await ask.add_reaction("✅")
    await ask.add_reaction("❌")

    def check(reaction, user):
        return user == ticketer
    reaction, user = await client.wait_for('reaction_add', check=check)
    if str(reaction.emoji) == '✅':
        embed = discord.Embed(title="<:bluetick:830431366222184468>  Hello! Welcome to the Callisto DM Support Center", description="Calisto Support Team member will contact you soon.", color=discord.Colour.blue())
        await ctx.author.send(embed=embed)
        embed = discord.Embed(description=f"✅  {ctx.author.mention} I have sent you a DM", colour=discord.Color.green())
        await ctx.send(embed=embed)
        server = client.get_guild(820737057143259147)
        category = server.categories[6]
        await server.create_text_channel(f'{ctx.author.id}', category=category)
        for channel in server.channels:
            if channel.name == f"{ctx.author}":
                channel = channel.id
        utc = datetime.utcnow().strftime("%H:%M UTC")
        embed = discord.Embed(title="<:bluetick:830431366222184468>  New support ticket", colour=discord.Color.blue())
        embed.add_field(name=f"Username:", value=f"{ctx.author}", inline=True)
        embed.add_field(name=f"ID:", value=f"{ctx.author.id}", inline=True)
        embed.add_field(name=f"Mention:", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name=f"Account created at:", value=f"{ctx.author.created_at.strftime('%d/%m/%Y, %H:%M')}", inline=True)
        embed.add_field(name=f"Ticket created at:", value=f"{datetime.utcnow().strftime('%d/%m/%Y, %H:%M')}", inline=True)
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"Today at {utc}")
        await channel.send("<@&830206019526328340h>")
        await channel.send(embed=embed)
        try:
            helper_role = discord.utils.get(ctx.guild.roles, name="Moderator")
        except:
            await ctx.guild.create_role(name="Moderator", permissions=discord.Permissions(send_messages=True))
            helper_role = discord.utils.get(ctx.guild.roles, name="Moderator")

        await channel.set_permissions(helper_role, send_messages=True, read_messages=True)
        @client.event
        async def on_message(message):
            await client.process_commands(message)
            if message.author.bot:
                return
            else:
                if message.guild is None:
                    for channel in server.channels:
                        if channel.name == f"{message.author.id}":
                            channelid = channel.id
                            channelsend = await client.fetch_channel(channelid)
                            await channelsend.send(f"**[USER] {message.author}:** {message.content}")
    if str(reaction.emoji) == '❌':
        embed = discord.Embed(description=f"❌  {ctx.author.mention} You have cancelled the command")
        await ctx.send(embed=embed)


@client.command(aliases=["reply"])
async def r(ctx, *, content=None, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
        await user.send(f"**[STAFF] {staff}:** {content}")
        await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def wlc(ctx, *, user:discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Welcome! Callisto Discord Support! How may we help you?"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def askformod(ctx, *, user:discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "You can’t get any staff position unless you apply and we do not accept applications via direct request either. You will need to wait for the next round of applications if you want to apply so keep an eye on #announcements or #updates for any updates on application openings."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def icanthelp(ctx, *, user:discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Unfortunately I can't help with your situation. Please wait until another staff member takes over this thread, please be patient as it may take a few minutes."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def verify(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "To enter the server please make sure you complete the remaining steps prompted to you in the bottom or in the top of your screen in the #rules channel."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def isthatall(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Is that all you need from us today?"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def thank(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Thank you for contacting Callisto Support and for your cooperation with the staff team! Is that all you need from us today?"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def bye(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Thanks for contacting Callisto support, this thread will now be closed. If you have any further problems/questions, feel free to open another thread."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def cRoles(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Custom roles are only achievable if an Administrator gives it to you, if you win a giveaway or if you boosted the server, please don't ask for custom roles if you do not meet the requirements."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def roles(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "We have self assignable roles, which you can achieve at #info"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def tempbanappeal(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "If you would like to appeal your recent ban, please respond with why you think you should be unbanned. The staff team may take up 24 hours to review this ban appeal"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def id(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "To get someone's ID, make sure you have Developer mode enabled in Discord's appearance settings. Then, right click (PC) or go to their profile and click the three dots (mobile) and press Copy ID."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def timeout(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "If there is no reply to this thread within the next 2 minutes, it will be closed in order to ensure you are able to open a new ticket if you still need help when you come back."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def abuse(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "Please do not abuse the Mail feature on this bot, This bot is for people who need assistance or support with the server. The mail feature cannot be used if you are bored either, and we do not appreciate questions like What's your favourite flight sim or Which plane do you like in these threads, you can ask us in General :)"
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def cc(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "2,000 Subscribers are required for youtube role and 2,000 followers for instagram role. You must also have Twitch affiliate status for the Twitch Streamer rank."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")


@client.command()
async def timeoutBye(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
    content = "This thread has been inactive for 2+ minutes, it will now be closed, please don't hesitate to create another ticket if you need support."
    await user.send(f"**[STAFF] {staff}:** {content}")
    await ctx.send(f"**[STAFF] {staff}:** {content}")

@client.command()
async def snippets(ctx):
    em = discord.Embed(title="Snippets", description="Callisto Snippets.", colour=discord.Colour.dark_purple())
    em.add_field(name="askformod", value="You can’t get any staff position unless you apply and we do not accept applications via direct request either. You will need to wait for the next round of applications if you want to apply so keep an eye on #announcements or #updates for any updates on application openings.", inline=False)
    em.add_field(name="icanthelp", value="Unfortunately I can't help with your situation. Please wait until another staff member takes over this thread, please be patient as it may take a few minutes.", inline=False)
    em.add_field(name="verify", value="To enter the server please make sure you complete the remaining steps prompted to you in the bottom or in the top of your screen in the #rules channel.", inline=False)
    em.add_field(name="isthatall", value="Is that all you need from us today?", inline=False)
    em.add_field(name="thank", value="Thank you for contacting Calisto Support and for your cooperation with the staff team! Is that all you need from us today?", inline=False)
    em.add_field(name="bye", value="Thanks for contacting Calisto support, this thread will now be closed. If you have any further problems/questions, feel free to open another thread.", inline=False)
    em.add_field(name="cRoles", value="Custom roles are only achievable if an Administrator gives it to you, if you win a giveaway or if you boosted the server, please don't ask for custom roles if you do not meet the requirements.", inline=False)
    em.add_field(name="roles", value="We have self assignable roles, which you can achieve at #info", inline=False)
    em.add_field(name="tempbanappeal", value="If you would like to appeal your recent ban, please respond with why you think you should be unbanned. The staff team may take up 24 hours to review this ban appeal", inline=False)
    em.add_field(name="id", value="To get someone's ID, make sure you have Developer mode enabled in Discord's appearance settings. Then, right click (PC) or go to their profile and click the three dots (mobile) and press Copy ID.", inline=False)
    em.add_field(name="timeout", value="If there is no reply to this thread within the next 2 minutes, it will be closed in order to ensure you are able to open a new ticket if you still need help when you come back.", inline=False)
    em.add_field(name="abuse", value="Please do not abuse the Mail feature on this bot, This bot is for people who need assistance or support with the server. The mail feature cannot be used if you are bored either, and we do not appreciate questions like What's your favourite flight sim or Which plane do you like in these threads, you can ask us in General :)", inline=False)
    em.add_field(name="cc", value="2,000 Subscribers are required for youtube role and 2,000 followers for instagram role. You must also have Twitch affiliate status for the Twitch Streamer rank.", inline=False)
    em.add_field(name="timeoutBye", value="This thread has been inactive for 2+ minutes, it will now be closed, please don't hesitate to create another ticket if you need support.", inline=False)
    await ctx.send(embed=em)

@client.command()
async def itaclose(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
        await ctx.send(f"**[{staff}]:** `Is this all you needed help with? If so react with with ✅, if not react with ❌`")
        con = await user.send(f"**[{staff}]:** Is this all you needed help with? If so react with `✅`, if not react with `❌`")
        await con.add_reaction("✅")
        await con.add_reaction("❌")
        await asyncio.sleep(2)
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: reaction.emoji == '✅' or '❌')
        if str(reaction.emoji) == "✅":
            await user.send(f"**[{staff}]:** Your Support ticket has been closed. Feel free to use `*support` whenever you need help. Thank you for using SwissTraining DM Support System. Have a nice day!")
            await ctx.send(f"**[{staff}]:** `Your Support ticket has been closed. Feel free to use `<support` whenever you need help regarding KotBot. Thank you for using KotBot DM Support System. Have a nice day!`")
            embed = discord.Embed(colour=discord.Color.red(), title="The ticket has been closed. This channel will be deleted in 10 seconds.", description="To abort the process type `x`")
            await ctx.send(embed=embed)
            msg = await client.wait_for("message")
            if msg.content == "x":
                embed = discord.Embed(colour=discord.Color.red(), title="The process has been cancelled. This channel will not be deleted.", description="To delete the channel manually - `*close`")
                await ctx.send(embed=embed)
            else:
                await asyncio.sleep(10)
                await ctx.channel.delete()

        if str(reaction.emoji) == "❌":
            await user.send(f"**[{staff}]:** What else could I help you with?")
            await ctx.send(f"**[STAFF] {staff}:** What else could I help you with?")


@client.command()
@commands.has_role(830206019526328340)
async def close(ctx, *, user: discord.User = None):
    staff = ctx.author
    if user is None:
        user = await client.fetch_user(ctx.channel.name)
        content = "Your ticket has been closed. Feel free to use `+support` whenever you need help regarding Callisto. Thank you for using Callisto DM Support System. Have a nice day!"
        await user.send(f"**[Staff - {staff}]:** {content}")
        embed = discord.Embed(title="User received a message:", description=f"`{content}`", colour=discord.Color.dark_red())
        await ctx.send(embed=embed)
        embed = discord.Embed(colour=discord.Color.red(),
                              title="The ticket has been closed. This channel will be deleted in 10 seconds.",
                              description="To abort the process type `x`")
        await ctx.send(embed=embed)
        msg = await client.wait_for("message")
        if msg.content == "x":
            embed = discord.Embed(colour=discord.Color.red(),
                                  title="The process has been canceled. This channel will not be deleted.",
                                  description="To delete the channel manually - `+delete`")
            await ctx.send(embed=embed)
        else:
            await asyncio.sleep(10)
            await ctx.channel.delete()

@client.command()
async def new(ctx):
    channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}')
    await channel.set_permissions(ctx.guild.default_role, send_messages = False, read_messages = False)
    await channel.set_permissions(ctx.guild.owner, send_messages = True, read_messages = True)

    try:
        helper_role = discord.utils.get(ctx.guild.roles, name = "Moderator")
    except:
        await ctx.guild.create_role(name = "Moderator", permissions = discord.Permissions(send_messages = True))
        helper_role = discord.utils.get(ctx.guild.roles, name = "Moderator")

    await channel.set_permissions(helper_role, send_messages = True, read_messages = True)
    em = discord.Embed(title = "Ticket Support")
    em.add_field(name = "Description", value = f"Support will be with you shortly {ctx.author.mention}")
    em.set_footer(text="Callisto Support.")
    await ctx.author.send(embed = em)
    utc = datetime.utcnow().strftime("%H:%M UTC")
    embed = discord.Embed(title="<:bluetick:830431366222184468>  New support ticket", colour=discord.Color.blue())
    embed.add_field(name=f"Username:", value=f"{ctx.author}", inline=True)
    embed.add_field(name=f"ID:", value=f"{ctx.author.id}", inline=True)
    embed.add_field(name=f"Mention:", value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name=f"Account created at:", value=f"{ctx.author.created_at.strftime('%d/%m/%Y, %H:%M')}", inline=True)
    embed.add_field(name=f"Ticket created at:", value=f"{datetime.utcnow().strftime('%d/%m/%Y, %H:%M')}", inline=True)
    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    embed.set_footer(text=f"Today at {utc}")
    await channel.send(embed=embed)


@client.command()
async def kot(ctx):
    async with aiohttp.ClientSession() as s:
        async with s.get("https://api.ksoft.si/images/random-image", params={"tag": "cat"},
                         headers={"Authorization": f"Bearer a43660a9f4c73f5f2d8aea7b3a8697d3b6652b41"}) as resp:
            data = await resp.json()

    await ctx.send(f'Ya want some cute kot pics?')

    time.sleep(1)

    await ctx.send(f'Heres one owo:')

    embed = discord.Embed(colour=discord.Colour.blue())

    embed.set_image(url=data["url"])

    await ctx.send(embed=embed)

@client.command(aliases=['doggo'])
async def dog(ctx):
    async with aiohttp.ClientSession() as s:
        async with s.get("https://api.ksoft.si/images/random-image", params={"tag": "dog"},
                         headers={"Authorization": f"Bearer a43660a9f4c73f5f2d8aea7b3a8697d3b6652b41"}) as resp:

            data = await resp.json()

    await ctx.send(f'Ya want some cute doggo pics?')

    time.sleep(1)

    await ctx.send(f'Heres one *bark bark*:')

    embed = discord.Embed(colour=discord.Colour.blue())

    embed.set_image(url=data["url"])

    await ctx.send(embed=embed)

@client.command(aliases=["coronavirus"])
async def covid(ctx, reason="None"):
    author = ctx.message.author

    embed=discord.Embed(colour=discord.Colour.red())
    r = requests.get('https://corona-stats.online/' + reason + '?format=json')
    stats = r.json()['data'][0]['country'], r.json()['data'][0]['cases']
    embed.set_author(name=r.json()['data'][0]['country'])
    embed.add_field(name="Cases:", value=r.json()['data'][0]['cases'], inline=False)
    embed.add_field(name="Cases today:", value=r.json()['data'][0]['todayCases'], inline=False)
    embed.add_field(name="Recovered:", value=r.json()['data'][0]['recovered'], inline=False)
    embed.add_field(name="Total deaths:", value=r.json()['data'][0]['deaths'], inline=False)
    embed.add_field(name="Deaths today:", value=r.json()['data'][0]['todayDeaths'], inline=False)
    embed.add_field(name="Active cases:", value=r.json()['data'][0]['active'], inline=False)
    await ctx.send(embed=embed)

@covid.error
async def covid_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+covid <country>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command(aliases=["rockpaperscissors"])
async def rps(ctx, type):
    h = random.randint(1, 3)
    if h == 1:
        if type == "r" or type == "rock":
            await ctx.send("Rock! Draw!")
        if type == "p" or type == "paper":
            await ctx.send("Rock! You won!")
        if type == "s" or type == "scissors":
            await ctx.send("Rock! You lost!")
    if h == 2:
        if type == "r" or type == "rock":
            await ctx.send("Paper! You lost!")
        if type == "p" or type == "paper":
            await ctx.send("Paper! Draw!")
        if type == "s" or type == "scissors":
            await ctx.send("Paper! You win!")
    if h == 3:
        if type == "r" or type == "rock":
            await ctx.send("Scissors! You won!")
        if type == "p" or type == "paper":
            await ctx.send("Scissors! You lost!")
        if type == "s" or type == "scissors":
            await ctx.send("Scissors! Draw!")

@client.command()
async def translate(ctx, lang, *, args):

    t = Translator()
    a = t.translate(args, dest=lang)

    embed = discord.Embed(color=discord.Colour.blue())
    embed.add_field(name=f"From English:", value=f"{args}", inline=False)
    embed.add_field(name=f"To {lang}:", value=f"{a.text}", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)

@translate.error
async def translate_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+translate <language> <text>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def tesla(ctx):

    embed = discord.Embed(title="Tesla Models List:", color=discord.Colour.blue())
    embed.add_field(name=f"Tesla Model **S**", value=f'$80,000', inline=False)
    embed.add_field(name=f"Tesla Model **3**", value=f'$35,000', inline=False)
    embed.add_field(name=f"Tesla Model **X**", value=f'$79,000', inline=False)
    embed.add_field(name=f"Tesla Model **Y**", value=f'$41,000', inline=False)
    embed.set_footer(text=f'psst: s3xy')

    await ctx.send(embed=embed)

@client.command()
async def getsomehelp(ctx):
    await ctx.send(f'https://tenor.com/view/stop-it-get-some-help-gif-7929301')

@client.command()
async def ineedhelp(ctx):
    await ctx.send(f'SOTP iT get some help u n00b')

@client.command(aliases=['hentai'])
async def porn(ctx):
    await ctx.send(f'https://tenor.com/view/horny-jail-go-to-horny-jail-bonk-doge-cheems-gif-17582752')

@client.command(aliases=['rickroll'])
async def nevergonnagiveyouup(ctx):
    await ctx.send(f"Get TogetherForever'd")
    await ctx.send(f'https://youtu.be/yPYZpwSpKmA')

@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/meme') as resp:
            link = await resp.json()
            await ctx.send(f"Here's a random meme. Have fun laughing you redditer:")
            await ctx.send(link["image"])

@client.command()
async def uwu(ctx, *, message):
    await ctx.send(message.replace("r", "w"))

@client.command()
async def build(ctx):
    embed = discord.Embed(Title="Callisto Build", colour=discord.Colour.blue())
    embed.add_field(name="Build Version:", value="v1.0.0 (Stable)", inline=False)
    embed.add_field(name="In development from:", value="14th March 2021", inline=False)
    embed.add_field(name="Bot is still in development", value="Please DM me if any errors occure: `Mako#9999`", inline=False)
    embed.add_field(name="Upcoming:", value="Stock exchange for economy", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def metar(ctx, *, icao=None):
    if ctx.author.bot:
        return
    loadmsg = await ctx.send(f":mag_right: Getting information for `{icao}`...")
    if not icao:
        return await loadmsg.edit(content=":x: Please provide an valid ICAO code.")
    url = f"https://avwx.rest/api/metar/{icao}?airport=true&reporting=true&format=json"
    headers = {'Authorization': 'tiFfDlt2dNErWpHzBMRsWLvj6i8TmoYZU5KZDnjvm3w'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as r:
            res = await r.json()
    if "error" in res:
        return await loadmsg.edit(content=f":x: The ICAO you provided: `{icao}` is **invalid**.")

    embed = discord.Embed(title=f"METAR data", color=discord.Colour.blue(), timestamp=datetime.utcnow())
    embed.add_field(name="**Flight rules**", value=res['flight_rules'])
    embed.add_field(name="**METAR**", value=res['raw'])
    embed.add_field(name="**Altimeter**", value=f"{res['altimeter']['value']}{res['units']['altimeter']}")
    embed.add_field(name="**Visiblity**", value=f"{res['visibility']['value']}{res['units']['visibility']}")
    embed.add_field(name="**Wind direction**", value=res['wind_direction']['value'])
    embed.add_field(name="**Wind speed**", value=f"{res['wind_speed']['value']}{res['units']['wind_speed']}")
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text=f"Mako Bot - METAR")
    await loadmsg.edit(content=None, embed=embed)

@metar.error
async def metar_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+metar <ICAO code>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def penismusic(ctx):
    await ctx.send(f'https://tenor.com/view/penis-music-megamind-dancing-dance-gif-16168557')

@client.command()
async def windoge(ctx):
    await ctx.send(f'Windoge 10')
    time.sleep(1.5)
    await ctx.send(f'Much improve.')
    time.sleep(1.5)
    await ctx.send(f'So amaze.')
    time.sleep(1.5)
    await ctx.send(f'Wow.')
    time.sleep(1.5)
    await ctx.send(f'https://cdn.discordapp.com/attachments/820737057693499415/821016385060601917/3dcT-ZUL1gvo1gkI7rMNIhuV7db6N55IZRYtR636Jc0.jpg')

@client.command()
async def gamestop(ctx):
    await ctx.send(f'https://tenor.com/view/stonks-up-stongs-meme-stocks-gif-15715298')

@client.command(aliases=["dw"])
async def dontworry(ctx):
    await ctx.send(f'Dotn wory. Be hapy. I try make you hapy :smile:')

@client.command()
async def paypal(ctx):
    await ctx.send(f'**Fuck paypal. Worst payment provider**')
    await ctx.send(f'*psst dat bc mako has small pp and paypal stock fell down by 25% after he invested in it :rofl:*')


blue = discord.Colour.blue()
red = discord.Colour.red()


@client.command(aliases=["battle"])
async def fight(ctx, member : discord.Member):
    if ctx.author == member:
        await ctx.send(f"imagine willing to fight yourself you masochist {ctx.author.mention}")
    else:
        embed1 = discord.Embed(description=f"{ctx.author.mention} **VS** {member.mention}\n")
        intro = await ctx.send(embed=embed1)
        member_hp = 100
        author_hp = 100

        first_hit = random.choice(["author", "member"])
        embed2 = discord.Embed(
            description=f"\n{ctx.author.mention} health - **{author_hp}**\n{member.mention} health - **{member_hp}**")
        display = await ctx.send(embed=embed2)
        c = 0
        while True:

            if first_hit == "author":
                author_dmg = random.randint(8, 18)
                member_dmg = random.randint(8, 18)

                member_hp = member_hp - author_dmg
                await asyncio.sleep(1)
                if member_hp <= 0:
                    embed_d = discord.Embed(
                        description=f"🏆 **{ctx.author} won the fight!**\n{ctx.author.mention} health - **{author_hp}**\n{member.mention} health - **0**")
                    await display.edit(embed=embed_d)
                    break
                else:
                    author_hp = author_hp - member_dmg
                if author_hp <= 0:
                    embed_d = discord.Embed(
                        description=f"🏆 **{member} won the fight!**\n{ctx.author.mention} health - 0\n{member.mention} health - {member_hp}")
                    await display.edit(embed=embed_d)
                    break

            else:
                member_dmg = random.randint(8, 18)
                author_dmg = random.randint(8, 18)

                author_hp = author_hp - member_dmg
                await asyncio.sleep(1)
                if author_hp <= 0:
                    embed_d = discord.Embed(
                        description=f"🏆 **{member} won the fight!**\n{ctx.author.mention} health - 0\n{member.mention} health - {member_hp}")
                    await display.edit(embed=embed_d)
                    break
                else:
                    member_hp = member_hp - author_dmg
                if member_hp <= 0:
                    embed_d = discord.Embed(
                        description=f"🏆 **{ctx.author} won the fight!**\n{ctx.author.mention} health - {author_hp}\n{member.mention} health - 0")
                    await display.edit(embed=embed_d)
                    break
            c = c + 1
            if c % 2 == 0:

                embed_display = discord.Embed(colour=red,
                                              description=f":crossed_swords: **Fight In Progress!**\n{ctx.author.mention} health - {author_hp}\n{member.mention} health - {member_hp}")
            else:
                embed_display = discord.Embed(colour=blue,
                                              description=f":crossed_swords: **Fight In Progress!**\n{ctx.author.mention} health - {author_hp}\n{member.mention} health - {member_hp}")

            await display.edit(embed=embed_display)

@fight.error
async def fight_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+fight <user>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def invite(ctx):
    await ctx.send("Yes it's finally that time! Callisto bot is finally released! Use https://discord.com/api/oauth2/authorize?client_id=820570914831859712&permissions=67492929&scope=bot to invite it to your server!!!")

@client.command()
async def server(ctx):
    await ctx.send("Join our server https://discord.gg/CujFpKvaCd if you want to get support or just use bot commands and talk with other people!")

@client.command()
async def ban(ctx):
     await ctx.send(f'What the fuck do you want to do?! I’m not yet another 69 thousandth useless moderating bot. There are hundreds of them. All of them are useless. If you want to do the ban command, go to your beloved MEE6. I’m never going to be *just* another moderating bot. No no no. I’m the only of my kind, original, amazing, the best Callisto bot.')

@client.command()
async def amogus(ctx):
    await ctx.send(f'No way amogus!!11!1!! When the imposter is SUS!!!!!1!!!1!!!!1!')

@client.command()
async def woah(ctx):
    await ctx.send(f'https://tenor.com/view/mind-blown-gif-11131691')

@client.command()
async def reverse(ctx, *, reversed):
    if "@<" in reversed or "ereh@" in reversed or "enoyreve@" in reversed:
        await ctx.send("imagine trying to exploit bugs, couldn't be mako smh.")
    else:
        reverses = reversed[::-1]
        await ctx.send(reverses)

@client.command(aliases=['hi'])
async def hello(ctx):
    await ctx.send(f"*cringy youtube intro* Now hey guys, welcome back to another video! Today I am going to show you the most amazing, the best, greatest bot that was ever made! The bot's name is Mako Bot.")

@client.command()
async def areyougreat(ctx):
    await ctx.send(f"Am I great? I am the most amazing of the most amazing, the best of the best, the greatest of the greatest!")

@client.command(aliases=["w"])
async def weather(ctx, *, varos):
    if not ctx.message.author.bot:
        try:
            api_key = "59c47d609f10c901151a1a13d8794465"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = varos
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            async with aiohttp.ClientSession() as session:
                async with session.get(complete_url) as r:
                    response = await r.json()
            x = response
            if x["cod"] != "404":
                import pytemperature
                y = x["main"]
                z = x["weather"]
                t = x["sys"]
                w = x["wind"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                country = t["country"]
                wind = w["speed"]
                direc = w["deg"]
                weather_description = z[0]["description"]
                celsius = pytemperature.k2c(current_temperature)
                embed = discord.Embed(title=f"Weather information for {varos}, {country}", color=0x00FFFF, timestamp=datetime.utcnow())
                embed.add_field(name="**Temperature**", value=f"{int(celsius)}°C")
                embed.add_field(name="**Pressure**", value=f"{current_pressure}hPa")
                embed.add_field(name="**Humidity**", value=f"{current_humidity}%")
                embed.add_field(name="**Wind**", value=f"{wind}mph at {direc}°")
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send(":x: Cannot find this **city**!")
        except Exception as e:
            await ctx.send(str(e))
            await ctx.send(f":x: Couldn't retrieve data for {varos}!")

@weather.error
async def weather_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+weather <place>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def feedback(ctx, *, reportmsg=None):
    if reportmsg is None:
        error = discord.Embed(color=discord.Colour.from_rgb(199, 39, 14))
        error.add_field(name=f"❌  Please provide an argument", value="Correct command form: +feedback `your feedback`")
        await ctx.send(embed=error)
    else:
        utc14 = datetime.utcnow().strftime("%H:%M UTC")
        embed = discord.Embed(description=f"`{reportmsg}`", colour=discord.Colour.blue())
        embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name='Are you sure you want to submit your feedback?', value="To confirm - react with ✅, to cancel - react with ❌")
        conf = await ctx.send(embed=embed)
        await conf.add_reaction("✅")
        await conf.add_reaction("❌")

        def check(reaction, user):
            return user == ctx.author

        reaction, user = await client.wait_for('reaction_add', check=check)
        if str(reaction.emoji) == '✅':
            confedit1 = discord.Embed(colour=discord.Color.green(), title=f"Thank you for submitting your feedback!", description=f"`{reportmsg}`")
            await conf.edit(embed=confedit1)
            embed = discord.Embed(title=f"{ctx.author} has sumbitted feedback:", description=f"`{reportmsg}`", colour=discord.Colour.green())
            embed.set_footer(text=f"Today at {utc14} ✦ Callisto Feedback")
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            server = client.get_guild(820737057143259147)
            for channel in server.channels:
                if channel.id == 820737592080465960:
                    feedbackchannelid = channel.id
                    feedbackchannel = await client.fetch_channel(feedbackchannelid)
                    await feedbackchannel.send(embed=embed)
        if str(reaction.emoji) == '❌':
            confedit2 = discord.Embed(description=f"❌ {ctx.author.mention} Your feedback has not been submitted! ", colour=discord.Color.from_rgb(199, 39, 14))
            await conf.edit(embed=confedit2)
        else:
            return

@client.command(aliases=["hit"])
async def slap(ctx, member:discord.Member, *, reason):
    await ctx.send(f"{ctx.author.display_name} slapped {member.mention} for {reason}!")

@slap.error
async def slap_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+slap <user> <reason>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@slap.error
async def slap_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+slap <user> <reason>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def nitro(ctx, choice = None):
    if choice == "boost":
        code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        await ctx.send(f"Here's a random discord nitro boost: https://discord.gift/{code}")
    if choice == "classic":
        code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        await ctx.send(f"Here's a random discord nitro classic: https://discord.gift/{code}")
    if choice == None:
        await ctx.send("Choose from nitro classic or boost!")

@client.command(aliases=["cs","ci","channelinfo"])
async def channelstats(ctx, channel: discord.TextChannel = None):
    if channel == None:
        channel = ctx.channel

    embed = discord.Embed(title=f"I doxxed the channel **#{channel.name}** (is it even possible to doxx a channel?)", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=discord.Colour.blue())
    embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=True)
    embed.add_field(name="Channel Id", value=channel.id, inline=True)
    embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic'}", inline=True)
    embed.add_field(name="Channel created at:", value=f'{channel.created_at.strftime("%H:%M, %Y.%m.%d")} (~{(datetime.utcnow() - channel.created_at).days} days)', inline=True)
    embed.add_field(name="Channel Position", value=channel.position, inline=True)
    embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=True)
    embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=True)
    embed.add_field(name="Channel is news?", value=channel.is_news(), inline=True)
    embed.add_field(name="Permissions Synced",value=channel.permissions_synced,inline=True)

    await ctx.send(embed=embed)

@channelstats.error
async def channelstats_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+channelstats <channel>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def facttest(ctx):
    fact = requests.get("https://some-random-api.ml/facts/fox").json()["fact"]
    await ctx.send(str(fact))

@client.command()
async def whymathisuseless(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/820737057693499415/821843647547965510/WhatsApp_Image_2021-03-17_at_14.44.52.jpeg")

@client.command()
async def imagine(ctx):
    await ctx.send("Imagine imagining about imagining")

@client.command()
async def why(ctx):
    await ctx.send("Because.")

@client.command()
async def whynot(ctx):
    await ctx.send("Because not.")

@client.command()
async def doyoureallyloveme(ctx):
    await ctx.send("I really love you! :heart:")

@client.command(aliases=["iambored"])
async def bored(ctx):
    await ctx.send("I was made to make people entertained. I am made especially for bored people, just like you! Check out +guide comamnd for me to guide you about myself!")

@client.command()
async def fun(ctx):
    await ctx.send("I hope you'll have a lot of fun with me!")

@client.command()
async def bestbot(ctx):
    await ctx.send("Yes, I am the best bot")

@client.command()
async def whysomanyfuncommands(ctx):
    await ctx.send("'Because I was bored' - Mako")

@client.command()
async def dogfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/dog') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command(aliases=["kotfact"])
async def catfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/cat') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command(aliases=["birbfact"])
async def birdfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/bird') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command()
async def foxfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/fox') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command()
async def pandafact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/panda') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command()
async def koalafact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/facts/koala') as resp:
            link = await resp.json()
            await ctx.send(link["fact"])

@client.command(aliases=['dogimg','doggoimg','doggoimage','dogpic','dogpicture'])
async def dogimage(ctx):
    await ctx.send(f"Here's a cute doggo pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/dog') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['catimg','kotimg','kotimage','catpic','catpicture'])
async def catimage(ctx):
    await ctx.send(f"Here's a cute cat pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/cat') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['koalaimg','koalapic','koalapicture','koala'])
async def koalaimage(ctx):
    await ctx.send(f"Here's a cute koala pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/koala') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['foximg','foxpic','foxpicture','fox'])
async def foximage(ctx):
    await ctx.send(f"Here's a cute fox pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/fox') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['birdimg','birdpic','birdpicture','bird','birb'])
async def birdimage(ctx):
    await ctx.send(f"Here's a cute bird pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/birb') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['pandaimg','pandapic','pandapicture','panda'])
async def pandaimage(ctx):
    await ctx.send(f"Here's a cute panda pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/panda') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['redpandaimg','redpandapic','redpandapicture','redpanda'])
async def redpandaimage(ctx):
    await ctx.send(f"Here's a cute panda pic :star_struck::")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://some-random-api.ml/img/redpanda') as resp:
            link = await resp.json()
            await ctx.send(link["link"])

@client.command(aliases=['encodebinary','numberencode','binaryencode'])
async def encode(ctx, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://some-random-api.ml/binary?encode={message}') as resp:
            link = await resp.json()
            await ctx.send(link["text"])
    embed=discord.Embed(title=f"Here's {message} in binary:", description=link, color=discord.Colour.blue())
    await ctx.send(embed=embed)

@client.command(aliases=['decodebinary','numberdecode','binarydecode'])
async def decode(ctx, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://some-random-api.ml/binary?decode={message}') as resp:
            link = await resp.json()
            await ctx.send(link["text"])
    embed=discord.Embed(title=f"Here's your binary decoded:", description=link, color=discord.Colour.blue())
    await ctx.send(embed=embed)

@client.command(aliases=['funny','haha','hahaha','kidding','laugh'])
async def joke(ctx):
    joke = requests.get("https://some-random-api.ml/joke").json()["joke"]
    await ctx.send(joke)

@client.event
async def on_message(message):
    key = "LWzMcJszfsy7n5CbM8aPexSK3"
    if message.author == client.user:
        return
    if "fuck you" in message.content or "gtfo" in message.content or "fuck u" in message.content or "get the fuck off" in message.content or "shut up" in message.content or "shut the fuck up" in message.content or "stfu" in message.content or "shut the up" in message.content:
        await message.channel.send('no u')
    if message.channel.id == 824907272496480286:
        response = requests.get(f"https://some-random-api.ml/chatbot?message={message}&key={key}").json()["response"]
        await message.channel.send(response)

    try:

        if message.mentions[0] == client.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(message.guild.id)]

            await message.channel.send(f"My prefix for this server is {pre}")

    except:
        pass

    if "blurjay" in message.content or "Blurjay" in message.content:
        await message.channel.send('**BLUEJAY** you fuck')

    await client.process_commands(message)

@client.command()
async def thanks(ctx):
    await ctx.send("Special thanks to Chanakan5591#1370 and Qlaudie#9999 for always helping me in developing the bot")

@client.command(aliases=["bal", "balance", "prof"])
async def profile(ctx, member:discord.Member = None):

    if member == None:
        member = ctx.author

    discorduserid = member.id
    await open_account(member)

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]
    bank_amt = doc["bank"]
    bag = doc["bag"]
    multis = doc["multis"]
    checkc = doc["company"]

    embed = discord.Embed(title=f"{member}'s Economy Profile", description=f"This command includes everything about {member}'s economy profile.", color=discord.Colour.blue())
    embed.add_field(name=f"🏦 Bank Balance", value=f"◉ `{bank_amt} coins`")
    embed.add_field(name=f"👛 Wallet Balance", value=f"◉ `{wallet_amt} coins`", inline=True)
    embed.add_field(name="🎒 Item Bag", value=f"More info about {member}'s bag can be accessed using `+bag` command", inline=False)
    embed.add_field(name="Bag contains:", value=f"`{bag}`", inline=False)
    embed.add_field(name="Multipliers:", value=f"`{multis}`", inline=False)
    if checkc == 0:
        company = "User isn't an employee/owner of any company!"
    else:
        company = checkc
    embed.add_field(name="Company:", value=f"{company}")
    embed.set_footer(text="Callisto Economy Profile")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def cheat(ctx, cheatedcoins, user:discord.Member = None):
    cheatedcoins = int(cheatedcoins)
    if ctx.author.id == 414829561621118977:
        if user == None:
            user = ctx.author
        await update_bank(user, cheatedcoins)
        await ctx.send(f'Successifully cheated ◉ {cheatedcoins} coins for {user}, my greatest leader {ctx.author.mention}')
    else:
        await ctx.send(f'Lmao ur not owner of me, i wont let you cheat smh')

@client.command()
@cooldown(1, 300, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    earning = random.randint(1, 101)

    possible_responses = [
        f"◉ {earning} coins just popped out of nowhere!",
        f"◉ {earning} coins fell from the sky!",
        f"God gave you ◉ {earning} coins.",
        f"Random woman walking gave you ◉ {earning} coins.",
        f"There has just been a bank robbery! Thefts stole so much that they couldn't run with it, so they dropped you ◉ {earning} coins!",
        f"Here's ◉ {earning} coins, beggar.",
        f"Stop begging, get to work, lazy ass. Here's ◉ {earning} coins to start over.",
        f"Poor, homeless beggar, here's ◉ {earning} coins. Hope this helps you!",
        f"A man just passed by and dropped ◉ {earning} coins from his pocket accidentally. You pick them up. Shhh, he may be mad you stole them!"]

    embed = discord.Embed(title="Begging", description=f"{random.choice(possible_responses)}")
    embed.set_footer(text=f"Multipliers granted you a total of % boost!")
    await ctx.send(embed=embed)

    await update_bank(ctx.author, earning, "wallet")

@client.command()
async def company(ctx, name):
    doc = enter.find_one({"name": name.lower()})
    revenue = doc["revenue"]
    trevenue = doc["totalrevenue"]
    eam = doc["employees"]
    id = doc["userid"]
    embed = discord.Embed(title=f"{name} Company Stats", description=f"These are the statistics of <@!{id}>'s company {name}!", colour=discord.Colour.random())
    embed.add_field(name="Owner:", value=f"<@!{id}>")
    embed.add_field(name="Total Revenue:", value=f"◉ {trevenue} coins")
    embed.add_field(name="Money:", value=f"◉ {revenue} coins")
    embed.add_field(name="Total employees:", value=f"{eam} users")
    embed.set_footer(text="Create your own company for 25m using +createcompany! Join a company using +job!")
    await ctx.send(embed=embed)

@client.command(aliases=["rolldice"])
async def dice(ctx, amount, number1, number2 = None, number3 = None):
    amount = int(amount)
    number1 = int(number1)
    number2 = int(number2)
    number3 = int(number3)
    await open_account(ctx.author)

    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]
    bank_amt = doc["bank"]

    if amount<wallet_amt:

        if number2 == None and number3 == None:
            dice = random.randint(1, 6)
            await ctx.send(f"I rolled the dice. The result is: {dice} 🎲")
            if number1 == dice:
                await ctx.send(f"You won! Here's ◉ {6*amount} coins as your reward!")
                await update_bank(ctx.author, 6*amount)
            else:
                await ctx.send(f"The numbers didn't match, so you lost ◉ {amount} coins :(")
                await update_bank(ctx.author, -1*amount)

        elif number3 == None:
            dice = random.randint(1, 6)
            await ctx.send(f"I rolled the dice. The result is: {dice} 🎲")
            if number1 == dice or number2 == dice:
                await ctx.send(f"You won! Here's ◉ {3*amount} coins as your reward!")
                await update_bank(ctx.author, 3*amount)
            else:
                await ctx.send(f"The numbers didn't match, so you lost ◉ {amount} coins :(")
                await update_bank(ctx.author, -1*amount)

        else:
            dice = random.randint(1, 6)
            await ctx.send(f"I rolled the dice. The result is: {dice} 🎲")
            if number1 == dice or number2 == dice or number3 == dice:
                await ctx.send(f"You won! Here's ◉ {2*amount} coins as your reward!")
                await update_bank(ctx.author, 2*amount)
            else:
                await ctx.send(f"The numbers didn't match, so you lost ◉ {amount} coins :(")
                await update_bank(ctx.author, -1*amount)
    else:
        await ctx.send("You are too poor to bet this much!")

@dice.error
async def dice_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+dice <amount> <number 1> <number 2> <number 3>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    bank_amt = doc["bank"]

    if amount == None:
        await ctx.send("Enter the amount smh. I won't let you withdraw nothing.")
        return

    if amount == "all":
        amount = bank_amt

    amount = int(amount)
    if amount>bank_amt:
        await ctx.send("You are too poor to do that!")
        return
    if amount<0:
        await ctx.send("If you wanted to try if this would take money away from your bank account as this number is negative as a bug, then no, it won't. Go away, bughunter.")
        return

    await update_bank(ctx.author,amount, "wallet")
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You withdrew ◉ {amount} coins!")

@withdraw.error
async def withdraw_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+withdraw <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]

    if amount == None:
        await ctx.send("Enter the amount smh. I won't let you deposit nothing.")
        return

    if amount == "all":
        amount = wallet_amt

    amount = int(amount)
    if amount>wallet_amt:
        await ctx.send("You are too poor to do that!")
        return
    if amount<0:
        await ctx.send("If you wanted to try if this would give you money to your balance, as this number is negative, as a bug, then no, it won't. Go away, bughunter.")
        return

    await update_bank(ctx.author,-1*amount, "wallet")
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You deposited ◉ {amount} coins!")

@deposit.error
async def deposit_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+deposit <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command(aliases=['sd'])
async def send(ctx,member:discord.User,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    bank_amt = doc["bank"]

    if amount == None:
        await ctx.send("Enter the amount smh. I won't let you deposit nothing.")
        return
    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bank_amt

    amount = int(amount)
    if amount>bank_amt:
        await ctx.send("You are too poor to do that!")
        return
    if amount<0:
        await ctx.send("If you wanted to try if this would give you money to your balance, as this number is negative, as a bug, then no, it won't. Go away, bughunter.")
        return

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    await ctx.send(f"You sent ◉ {amount} coins to {member}!")

    embed = discord.Embed(title="Calisto Economy", colour=discord.Colour.blue())
    embed.add_field(name=f"You just recieved ◉ {amount} coins!", value=f"{ctx.author} just sent you ◉ {amount} coins!", inline=False)
    await member.send(embed=embed)

@send.error
async def send_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+send <user> <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))

@client.command(aliases=["bet"])
async def horsebet(ctx, user:discord.User, amount = None):
    await open_account(ctx.author)
    await open_account(user)
    amount = int(amount)
    bal = await update_bank(user)
    bal1 = await update_bank(ctx.author)
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]

    memberid = user.id

    doc1 = mainbank.find_one({"userid": memberid})
    wallet_amt1 = doc1["wallet"]
    if ctx.author == user:
        await ctx.send(f"imagine willing to place horse bet against yourself {ctx.author.mention}")
        return
    elif amount == None:
        await ctx.send("Enter the amount smh, I won't let you bet nothing")
        return
    else:
        if wallet_amt1>amount:
            if wallet_amt>amount:
                embed = discord.Embed(title="🏇 Horse Betting", description=f"{user.mention}, would you like to accept the {ctx.author}'s bet for {amount} coins?")
                embed.set_footer(text="Reply with `yes` to accept the bet, `no` will cancel the bet.")
                await ctx.send(embed=embed)
                msg = await client.wait_for("message", timeout=50)
                if msg.content == "yes" and msg.author == user:
                    member_hp = 0
                    author_hp = 0

                    first_hit = random.choice(["author", "member"])
                    em = discord.Embed(title="🏇 Horse Betting",
                                       description=f"{ctx.author.mention}'s horse vs {user.mention}'s horse!")
                    em.add_field(name=f"🏇{ctx.author}'s Horse Distance: {author_hp}m", value="-=-=-=-=-", inline=False)
                    em.add_field(name=f"🏇{user}'s Horse Distance: {member_hp}m", value="-=-=-=-=-", inline=False)
                    display = await ctx.send(embed=em)
                    c = 0
                    while True:

                        if first_hit == "author":
                            author_dmg = random.randint(8, 18)
                            member_dmg = random.randint(8, 18)

                            member_hp = member_hp + author_dmg
                            await asyncio.sleep(1)
                            if member_hp >= 100:
                                embed_d = discord.Embed(
                                    description=f"🏆 {user}'s horse won the bet! They just won ◉ {amount} coins! Congrats!")
                                embed_d.set_footer(text=f"{ctx.author} lost and had to pay ◉ {amount} to the winner!")
                                await display.edit(embed=embed_d)
                                await update_bank(user, amount)
                                await update_bank(ctx.author, -1*amount)
                                break
                            else:
                                author_hp = author_hp + member_dmg
                            if author_hp >= 100:
                                embed_d = discord.Embed(
                                    description=f"🏆 {ctx.author}'s horse won the bet! They just won ◉ {amount} coins! Congrats!")
                                embed_d.set_footer(text=f"{user} lost and had to pay ◉ {amount} to the winner!")
                                await display.edit(embed=embed_d)
                                await update_bank(ctx.author, amount)
                                await update_bank(user, -1*amount)
                                break

                        else:
                            member_dmg = random.randint(8, 18)
                            author_dmg = random.randint(8, 18)

                            author_hp = author_hp + member_dmg
                            await asyncio.sleep(1)
                            if member_hp >= 100:
                                embed_d = discord.Embed(
                                    description=f"🏆 {user}'s horse won the bet! They just won ◉ {amount} coins! Congrats!")
                                embed_d.set_footer(text=f"{ctx.author} lost and had to pay ◉ {amount} to the winner!")
                                await display.edit(embed=embed_d)
                                await update_bank(ctx.author, -1*amount)
                                await update_bank(user, amount)
                                break
                            else:
                                member_hp = member_hp + author_dmg
                            if author_hp >= 100:
                                embed_d = discord.Embed(
                                    description=f"🏆 {ctx.author}'s horse won the bet! They just won ◉ {amount} coins! Congrats!")
                                embed_d.set_footer(text=f"{user} lost and had to pay ◉ {amount} to the winner!")
                                await display.edit(embed=embed_d)
                                await update_bank(user, -1*amount)
                                await update_bank(ctx.author, amount)
                                break
                        c = c + 1
                        if c % 2 == 0:

                            embed_display = discord.Embed(title="🏇 Horse Betting",
                                                          description=f"{ctx.author.mention}'s horse vs {user.mention}'s horse!")
                            embed_display.add_field(name=f"🏇{ctx.author}'s Horse Distance: {author_hp}m",
                                                    value="-=-=-=-=-", inline=False)
                            embed_display.add_field(name=f"🏇{user}'s Horse Distance: {member_hp}m", value="-=-=-=-=-",
                                                    inline=False)
                        else:
                            embed_display = discord.Embed(title="🏇 Horse Betting",
                                                          description=f"{ctx.author.mention}'s horse vs {user.mention}'s horse!")
                            embed_display.add_field(name=f"🏇{ctx.author}'s Horse Distance: {author_hp}m",
                                                    value="-=-=-=-=-", inline=False)
                            embed_display.add_field(name=f"🏇{user}'s Horse Distance: {member_hp}m", value="-=-=-=-=-",
                                                    inline=False)

                        await display.edit(embed=embed_display)

                if msg.content == "no" and msg.author == user:
                    await ctx.send("Bet cancelled")
                    return
            else:
                await ctx.send(f"You are too poor to do that, {ctx.author.mention}")
                return
        else:
            await ctx.send(f"{user.mention} is too poor to do that!")
            return

@horsebet.error
async def horsebet_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+horsebet <user> <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command(aliases=['slot'])
async def slots(ctx, amount = None):
    await open_account(ctx.author)

    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]

    if amount == None:
        await ctx.send("Enter the amount smh. I won't let you bet nothing.")
        return

    amount = int(amount)
    if amount > wallet_amt:
        await ctx.send("You are too poor to do that!")
        return
    if amount < 0:
        await ctx.send(
            "If you wanted to try if this would give you money to your balance, as this number is negative, as a bug, then no, it won't. Go away, bughunter.")
        return

    final = []
    for i in range(3):
        a = random.choice(["🍓", "🍋", "🍑", "🍍"])


        final.append(a)

    m1=await ctx.send(f"['🍓', '🍋', '🍑']")
    time.sleep(1)
    await m1.edit(content="['🍓', '🍍', '🍓']")
    time.sleep(1)
    await m1.edit(content="['🍋', '🍑', '🍍']")
    time.sleep(1)
    await m1.edit(content=(str(final)))

    if final[0] == final[1] == final[2]:
        await update_bank(ctx.author, 5*amount, "wallet")
        await ctx.send(f"JACKPOT 💰!!!")
    elif final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount, "wallet")
        await ctx.send("You won!")
    else:
        await update_bank(ctx.author,-1*amount, "wallet")
        await ctx.send("You lost!")

@slots.error
async def slots_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+slots <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def rob(ctx,user:discord.User,amount = None):
    await open_account(ctx.author)
    await open_account(user)

    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]

    if amount == "all":
        amount = wallet_amt

    if wallet_amt<100:
        await ctx.send("it's not worth the risk robbing less than 100 coins lmao")
        ctx.command.reset_cooldown(ctx)
        return

    r = random.randrange(1, 10)
    if r>=5:
        earnings = amount

        await update_bank(ctx.author,earnings)
        await update_bank(user,-1*earnings)

        await ctx.send(f"💰You've just stolen ◉ {amount} coins from {user}. Such a bad thief. Go better get a job or sth, stealing other member's money is a dick move.")
    if r<=6:
        await update_bank(ctx.author,-1000)
        await ctx.send(f"You've been fined 1000 coins for stealing. Don't do that next time, asshole robber!")

@rob.error
async def rob_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+rob <user> <amount>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await update_bank(ctx.author, 300)
    await ctx.send("You just claimed your daily free ◉ 300 coins!")

@client.command()
@commands.cooldown(1, 648000, commands.BucketType.user)
async def weekly(ctx):
    await update_bank(ctx.author, 800)
    await ctx.send("You just claimed your weekly free ◉ 800 coins!")

@client.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def post(ctx):
    h1 = [
        "r/AskReddit",
          "r/IAmA",
          "r/bestof",
          "r/fatpeoplestories",
          "r/prettyrevenge",
          "r/TalesFromRetail",
          "r/DoesAnybodyElse",
          "r/CrazyIdeas",
          "r/WTF",
          "r/aww",
          "r/cringepics",
          "r/cringe",
          "r/rage",
          "r/creepy",
          "r/nosleep",
          "r/nostalgia",
          "r/creepyPMs",
          "r/gaming",
          "r/leagueoflegends",
          "r/pokemon",
          "r/Minecraft",
          "r/starcraft",
          "r/Games"
    ]
    h2 = [
        "r/DotA2",
          "r/skyrim",
          "r/tf2",
          "r/magicTCG",
          "r/wow",
          "r/KerbalSpaceProgram",
          "r/mindcrack",
          "r/Fallout",
          "r/roosterteeth",
          "r/Planetside",
          "r/gamegrumps",
          "r/battlefield3",
          "r/zelda",
          "r/darksouls",
          "r/masseffect",
          "r/arrestdevelopment",
          "r/gameofthrones",
          "r/doctorwho",
          "r/mylittleponny",
          "r/community",
          "r/breakingbad",
          "r/adventuretime",
          "r/startrek",
          "r/TheSimpsons"
    ]
    h3 = [
        "r/futurama",
          "r/HIMYM",
          "r/DunderMifflin",
          "r/Music",
          "r/Movies",
          "r/harrypotter",
          "r/StarWars",
          "r/hiphopheads",
          "r/anime",
          "r/comicbooks",
          "r/geek",
          "r/batman",
          "r/TheLastAirbender",
          "r/Naruto",
          "r/FanTheories",
          "r/funny",
          "r/AdviceAnimals",
          "r/4chan",
          "r/ImGoingToHellForThis",
          "r/circlejerk",
          "r/facepalm",
          "r/jokes",
          "r/comics",
          "r/britishproblems",
          "r/pics",
          "r/wallstreetbets"
    ]
    embed = discord.Embed(title="Where would you like to post your meme?", description="See how many likes does it recieve!", colour=discord.Colour.random())
    alist = []
    rand1 = random.choice(h1)
    rand2 = random.choice(h2)
    rand3 = random.choice(h3)
    alist.append(rand1)
    alist.append(rand2)
    alist.append(rand3)
    embed.add_field(name=f"1. {rand1}", value="** **", inline=False)
    embed.add_field(name=f"2. {rand2}", value="** **", inline=False)
    embed.add_field(name=f"3. {rand3}", value="** **", inline=False)
    embed.set_footer(text="Reply to this message with the subreddit on which you want to post!")
    await ctx.send(embed=embed)
    msg = await client.wait_for("message")
    if msg.content in alist:
        num = random.randint(1, 5)
        if num == 1:
            num1 = random.randint(1, 10000)
        else:
            num1 = random.randint(1, 1000)
        num2 = random.randint(1, 500)
        countit = num1/num2
        if countit < 1:
            em = discord.Embed(title="Your post is being bullied on reddit!", description="** **", colour=discord.Colour.red())
            em.add_field(name=f"👍 {num1} | 👎 {num2}", value="No coins for you!")
            await ctx.send(embed=em)
        else:
            if num1 < 500:
                em = discord.Embed(title="Your post went average", description="** **", colour=discord.Colour.random())
                em.add_field(name=f"👍 {num1} | 👎 {num2}", value="You just gained ◉ 50 coins!")
                await update_bank(ctx.author, 50)
                await ctx.send(embed=em)
            elif num1 >= 500 and num1 < 1000:
                em = discord.Embed(title="Your post went great!", description="** **", colour=discord.Colour.random())
                em.add_field(name=f"👍 {num1} | 👎 {num2}", value="You just gained ◉ 100 coins!")
                await update_bank(ctx.author, 100)
                await ctx.send(embed=em)
            elif num1 >= 1000:
                em = discord.Embed(title="Your post went viral!!!", description="** **", colour=discord.Colour.random())
                em.add_field(name=f"👍 {num1} | 👎 {num2}", value="You just gained ◉ 500 coins!")
                await ctx.send(embed=em)
    else:
        await ctx.send("You sent a meme to...Nowhere! smh specify the right place next time")
        ctx.commands.reset_cooldown(ctx)

@client.command()
async def shop(ctx):
    em = discord.Embed(title="🛒 Callisto Shop", description="*Here, you can buy literally everything! Buy an item to work, buy a vegetable to feed your pet (coming soon!) or get a custom role (coming soon!)*", colour=0x0FFFF)

    for item in themainshop:
        name = item["displayname"]
        price = item["price"]
        desc = item["description"]
        thename = item["name"]
        em.add_field(name = f"{name} -- ◉ {price}, `+buy {thename}`", value = f"*{desc}*", inline=False)

    await ctx.send(embed = em)

@client.command()
async def buy(ctx, item, amount = 1):
    amount = int(amount)
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("Thingy you wanna buy isn't in our shop. go to your walmart smh")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough coins in your wallet to buy {item}. Go work or beg or sth.")
            return


    await ctx.send(f"You just bought {item}")

@buy.error
async def buy_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+buy <item>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    amount = int(amount)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("Thingy you wanna sell isn't in our shop. go to your walmart smh")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough {item} in your bag to sell {item}s. Go get them first lol.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag. Go get it first lmao.")
            return

    await ctx.send(f"You just sold {item}!")

@sell.error
async def sell_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+sell <item>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def bag(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author

    discorduserid = user.id

    await open_account(user)

    doc = mainbank.find_one({"userid": discorduserid})

    bag = doc["bag"]

    em = discord.Embed(title=f"🎒 {user}'s Item Bag", description="If no items are shown, this means the bag is empty.", colour=0x0FFFF)
    name = bag
    if "toilet_paper" in name:
        displayname = "🧻 Toilet Paper"
        desc = "Work as Toilet Paper Handler!"
        workcommand = "+work Toilet Paper"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "vacuum" in name:
        displayname = "🧹 Vacuum"
        desc = "Work as house cleaner!"
        workcommand = "+work Cleaner"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "lawn_mower" in name:
        displayname = "🏡 Lawn Mower"
        desc = "Work as gardener!"
        workcommand = "+work Gardener"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "PC" in name:
        displayname = "🖥️ PC"
        desc = "Unlock more work possibilities!"
        workcommand = "play fortnite pc!"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "car_mechanic" in name:
        displayname = "🚗 Car Mechanic Degree"
        desc = "Work on fixing cars!"
        workcommand = "+work Car Mechanic"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "keyboard" in name:
        displayname = "⌨️ Keyboard"
        desc = "Work as copywriter! Caution: PC needed."
        workcommand = "+work Copywriter"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "mouse" in name:
        displayname = "🖱️ Mouse"
        desc = "Work on survey completing! Caution: PC needed."
        workcommand = "+work Survey"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "game" in name:
        displayname = "🎮 Game"
        desc = "Work as pro gamer! Caution: PC needed."
        workcommand = "+work Gamer"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "website" in name:
        displayname = "*www.* Website"
        desc = "Work as blogger! Caution: PC needed."
        workcommand = "+work Blogger"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "shopify" in name:
        displayname = "🛍️ Shopify"
        desc = "Work as dropshipper! Caution: PC and website needed."
        workcommand = "+work Dropshipper"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "pilot_license" in name:
        displayname = "✈️ Pilot License"
        desc = "Work as a pilot!."
        workcommand = "+work Pilot"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "lawyer" in name:
        displayname = "⚖️ Lawyer Degree"
        desc = "Work as lawyer!"
        workcommand = "+work Lawyer"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "doctor" in name:
        displayname = "🩺 Doctor Certificate"
        desc = "Work as doctor!"
        workcommand = "+work Doctor"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    if "finance" in name:
        displayname = "📈 Financial Analytic"
        desc = "Work as financial analytic!"
        workcommand = "+work Finance"
        em.add_field(name=displayname, value=f'{desc} `{workcommand}`')
    print(name)

    await ctx.send(embed=em)

@client.command(aliases = ["elb"])
async def economyleaderboard(ctx,x = 10):
    leader_board = {}
    total = []
    for user in leader_board:
        doc = mainbank.find_one({"userid": user.id})
        name = int(user)
        total_amount = doc["wallet"] + doc["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Fat Cats" , description = "Top richest People in the whole Callisto world.",color = discord.Color(0xfa43ee))
    em.set_footer(text="This is decided on the basis of raw money in the bank and wallet")
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
async def bankrob(ctx, user:discord.User):
    discorduserid = ctx.author.id
    doc = mainbank.find_one({"userid": discorduserid})

    multiplie = doc["multis"]
    if "spider" in multiplie:
        discorduserid = user.id
        doc = mainbank.find_one({"userid": discorduserid})
        multiplie = doc["multis"]
        if "butterfly" in multiplie:
            await ctx.send("Rob failed! User has butterfly pet!")
        else:
            num = random.randint(1, 5)
            if num == 1:
                discorduserid = user.id
                doc = mainbank.find_one({"userid": discorduserid})
                bank_amt = doc["bank"]
                brm = 0.1 * float(bank_amt)
                brm = int(brm)
                await update_bank(user, -1 * brm)
                await update_bank(ctx.author, brm)
                embed = discord.Embed(title=f"Successfully bankrobbed {user}!", description=f"The user {user} has been successfully bankrobbed! They lost 10% of their bank balance: ◉ {brm} coins!", colour=discord.Colour.random())
                embed.set_footer(text="Butterfly pet prevents you from getting bankrobbed! | You can bankrob someone once every 12 hours!")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=f"Rob failed!", description=f"Failed to rob {user}. Try next time, sorry!", colour=discord.Colour.red())
                embed.set_footer(text="Butterfly pet prevents you from getting bankrobbed! | You can bankrob someone once every 12 hours!")
                await ctx.send(embed=embed)
    else:
        await ctx.send("Can't use bankrob! You don't have the spider pet!")
        ctx.command.reset_cooldown(ctx)

@client.command()
@commands.cooldown(1, 2400, commands.BucketType.user)
async def hunt(ctx):
    num = random.randint(1, 10000)
    em = discord.Embed(title="You just went on a hunt!", description="** **", colour=discord.Colour.random())
    em.set_footer(text="Access your multipliers with +multipliers command! • You have a 20% chance of getting a multiplier!")
    print(num)

    if 1 <= num <= 400:
        await get_multiplier(ctx.author, "fly")
        em.add_field(name="Common catch!", value="You just got a fly!")
        await ctx.send(embed=em)
    elif 401 <= num <= 800:
        await get_multiplier(ctx.author, "mosquito")
        em.add_field(name="Common catch!", value="You just got a mosquito!")
        await ctx.send(embed=em)
    elif 1201 <= num <= 1600:
        await get_multiplier(ctx.author, "ladybird")
        em.add_field(name="Common catch!", value="You just got a ladybird!")
        await ctx.send(embed=em)
    elif 1601 <= num <= 1700:
        await get_multiplier(ctx.author, "spider")
        em.add_field(name="Rare catch!", value="You just got a spider!")
        await ctx.send(embed=em)
    elif 801 <= num <= 1200:
        await get_multiplier(ctx.author, "mouse")
        em.add_field(name="Uncommon catch!", value="You just got a mouse!")
        await ctx.send(embed=em)
    elif 1701 <= num <= 1900:
        await get_multiplier(ctx.author, "salmon")
        em.add_field(name="Uncommon catch!", value="You just got a salmon!")
        await ctx.send(embed=em)
    elif 1901 <= num <= 1999:
        await get_multiplier(ctx.author, "butterfly")
        em.add_field(name="Uncommon catch!", value="You just got a butterfly!")
        await ctx.send(embed=em)
    elif num == 10000:
        await get_multiplier(ctx.author, "newton")
        em.add_field(name="MYTHIC CATCH!", value="You just THE CUTEST MYTHIC YORKIE NEWTON!!!")
        await ctx.send(embed=em)
    else:
        em.add_field(name="Catch!", value="You just got a stinky shoe. What will you even do with it?!")
        await ctx.send(embed=em)

@client.command()
@commands.cooldown(1, 2400, commands.BucketType.user)
async def fish(ctx):
    discorduserid = ctx.author.id
    doc = mainbank.find_one({"userid": discorduserid})

    multiplie = doc["multis"]
    if "salmon" in multiplie:
        num = random.randint(1, 100)
        em = discord.Embed(title="You just went on a fishing!", description="", colour=discord.Colour.blue())
        em.set_footer(text="Chance of fishing a cod is 1%, but of a trout - 9%!")
        if num == 1:
            await update_bank(ctx.author, 1000)
            em.add_field(name="Great catch!", value="You just caught a cod! • ◉ +1000 coins")
        if 2 <= num <= 10:
            await update_bank(ctx.author, 500)
            em.add_field(name="Nice catch!", value="You just caught a trout! • ◉ +500 coins")
        else:
            await update_bank(ctx.author, 100)
            em.add_field(name="Normal catch!", value="You just caught a herring! • ◉ +100 coins")

        await ctx.send(embed=em)
    else:
        await ctx.send("You don't have salmon! To fish, you need to have the salmon pet, which is obtainable using the +hunt command.")

@client.command(aliases=["scout"])
@cooldown(1, 2400, commands.BucketType.user)
async def search(ctx):
    await open_account(ctx.author)
    search1 = [
        'shoe',
        'pot',
        'cup',
        'teacup',
        'PC',
        'old piano',
        'desk',
        'table',
        'fridge',
        'dishwasher',
        'old guitar',
        'attic',
        'wardrobe',
        'sink',
        'pillow',
        'under the bed',
        'bag'
    ]

    search2 = [
        'basement',
        'inside your dirty iPhone 15 C Pro Max SE 2 Limited Edition (RED)TM',
        'washbasin',
        'shower',
        'lamp',
        'flower',
        'guitar',
        'aquarium',
        'pool',
        'trash bin',
        'jacket',
        'tracksuit',
        't-shirt',
        'boots',
        'high heels',
        "mum's bag",
        "mum's wallet (find out how rich your mommy is(psst and steal something to buy $19 fortnite card))"
    ]

    search3 = [
        'lipstick',
        'toothpaste',
        'car',
        'motorbike',
        'bike',
        'worksuit',
        'swimsuit',
        'laptop',
        'headphones',
        'microphone',
        'calculator',
        'clock',
        'old clock',
        'pencilcase',
        'bookcase',
        'old book'
    ]

    await ctx.send(f"Mr. Free Money Seeker, where do you want to search? `{random.choice(search1)}, {random.choice(search2)}, {random.choice(search3)}` (Send the choice to the chat!)")
    msg = await client.wait_for("message")
    any1 = [
        'lipstick',
        'toothpaste',
        'car',
        'motorbike',
        'bike',
        'worksuit',
        'swimsuit',
        'laptop',
        'headphones',
        'microphone',
        'calculator',
        'clock',
        'old clock',
        'pencilcase',
        'bookcase',
        'old book',
        'basement',
        'inside your dirty iPhone 15 C Pro Max SE 2 Limited Edition (RED)TM',
        'washbasin',
        'shower',
        'lamp',
        'flower',
        'guitar',
        'aquarium',
        'pool',
        'trash bin',
        'jacket',
        'tracksuit',
        't-shirt',
        'boots',
        'high heels',
        "mum's bag",
        "mum's wallet",
        'shoe',
        'pot',
        'cup',
        'teacup',
        'PC',
        'old piano',
        'desk',
        'table',
        'fridge',
        'dishwasher',
        'old guitar',
        'attic',
        'wardrobe',
        'sink',
        'pillow',
        'under the bed',
        'bag']
    earnings = random.randrange(20, 300)
    if msg.content in any1:
        xd = await multipliery(ctx.author)
        lol = 1 + xd
        earning = lol * float(earnings)
        earning = int(earning)
        embed = discord.Embed(title="Search", description=f"You searched {msg.content} and found ◉ {earning} coins!", colour=discord.Colour.blue())
        embed.set_footer(text=f"Multipliers granted you a total of {100*xd:,.0f}% boost!")
        await update_bank(ctx.author, earning)
        await ctx.send(embed=embed)
        return
    else:
        await ctx.send("You searched the wrong place! I told you what to search...try again next time!")
        ctx.command.reset_cooldown(ctx)
        return

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx, *, worktype):
    user = ctx.author
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})
    bag = doc["bag"]

    xd = await multipliery(ctx.author)
    lol = 1+xd
    print(lol)
    compa = await checkifcompany(ctx.author)

    if worktype.lower() == "toilet paper" or worktype.lower() == "toilet paper handler" or worktype.lower() == "toilet handler":
        earnings = random.randint(300, 350)
        earning = lol * float(earnings)
        if "toilet_paper" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!", description=f"You just handled a toilet paper for a random person pooping. What an awful job! He gave you ◉ {earning:,.0f} coins though.", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100*xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You don't have toilet paper! To work, you need to buy it first, what, you thought you would be able to handle toilet paper without toilet paper? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "house cleaner" or worktype.lower() == "cleaner" or worktype.lower() == "home cleaner":
        earnings = random.randint(1000, 1400)
        earning = lol * float(earnings)
        if "vacuum" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!", description=f"You just cleaned a house. Kinda boring, right? Owners gave you ◉ {earning:,.0f} coins tho.", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You don't have vacuum! To work, you need to buy it first, what, you thought you would be able to clean houses without a vacuum? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    if worktype.lower() == "lawn mower" or worktype.lower() == "gardener" or worktype.lower() == "home cleaner":
        earnings = random.randrange(1000, 1400)
        earning = lol * float(earnings)
        if "lawn_mower" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just mowed a lawn. Very tiring job. You earned ◉ {earning:,.0f} coins tho.",
                                  colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send(
                "You don't have lawn mower! To work, you need to buy it first, what, you thought you would be able to mowe a lawn using your fingers? This would take countless hours lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "car mechanic" or worktype.lower() == "car_mechanic" or worktype.lower() == "carmechanic":
        earnings = random.randrange(3000, 4500)
        earning = lol * float(earnings)
        if "car_mechanic" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just fixed a car. You got paid ◉ {earning:,.0f} coins for that",
                                  colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send(
                "You don't have car mechanic degree! To work, you need to buy it first, what, you thought you would be able to fix a car without a degree? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "copywriter" or worktype.lower() == "writer" or worktype.lower() == "keyboard":
        earnings = random.randrange(5000, 8000)
        earning = lol * float(earnings)
        if "keyboard" in bag:
            if "pc" in bag:
                earning = int(earning)
                await revenue(user, earning)
                if compa is False:
                    earning = earning * 1.2
                await update_bank(ctx.author, earning)
                xd = await multipliery(ctx.author)
                embed = discord.Embed(title="You just worked!",
                                      description=f"You just wrote an article. You got paid ◉ {earning:,.0f} coins for that",
                                      colour=discord.Colour.blue())
                embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
                await ctx.send(embed=embed)
                return
            else:
                await ctx.send(
                    "You don't have PC. To work as copywriter, you need to have PC. What, you thought you would be able to copywrite without a pc? Lmao")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.send(
                "You don't have keyboard. To work as copywriter, you need to have PC. What, you thought you would be able to copywrite without a mouse? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "survey" or worktype.lower() == "survey filler" or worktype.lower() == "survey filling":
        earnings = random.randrange(5000, 8000)
        earning = lol * float(earnings)
        if "mouse" in bag:
            if "pc" in bag:
                earning = int(earning)
                await revenue(user, earning)
                if compa is False:
                    earning = earning * 1.2
                await update_bank(ctx.author, earning)
                xd = await multipliery(ctx.author)
                embed = discord.Embed(title="You just worked!",
                                      description=f"You just filled a survey. You got paid ◉ {earning:,.0f} coins for that",
                                      colour=discord.Colour.blue())
                embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
                await ctx.send(embed=embed)
                return
            else:
                await ctx.send(
                    "You don't have PC. To work as survey filler, you need to have PC. What, you thought you would be able to fill surveys without a pc? Lmao")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.send(
                "You don't have mouse. To work as survey filler, you need to have PC. What, you thought you would be able to fill surveys without a mouse? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "gamer" or worktype.lower() == "gaming" or worktype.lower() == "game":
        earnings = random.randrange(20000, 28000)
        earning = lol * float(earnings)
        if "game" in bag:
            if "pc" in bag:
                earning = int(earning)
                await revenue(user, earning)
                if compa is False:
                    earning = earning * 1.2
                await update_bank(ctx.author, earning)
                xd = await multipliery(ctx.author)
                embed = discord.Embed(title="You just worked!",
                                      description=f"You just played a game on a competition. You got paid ◉ {earning:,.0f} coins for that",
                                      colour=discord.Colour.blue())
                embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
                await ctx.send(embed=embed)
                return
            else:
                await ctx.send(
                    "You don't have PC. To work as gamer, you need to have PC. What, you thought you would be able to play games without a pc? Lmao")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.send(
                "You don't have game. To work as gamer, you need to have a game. What, you thought you would be able to play games without games? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "blogger" or worktype.lower() == "blog" or worktype.lower() == "blogging":
        earnings = random.randrange(20000, 28000)
        earning = lol * float(earnings)
        if "website" in bag:
            if "pc" in bag:
                earning = int(earning)
                await revenue(user, earning)
                if compa is False:
                    earning = earning * 1.2
                await update_bank(ctx.author, earning)
                xd = await multipliery(ctx.author)
                embed = discord.Embed(title="You just worked!",
                                      description=f"You just wrote an article for a blog. You got paid ◉ {earning:,.0f} coins for that",
                                      colour=discord.Colour.blue())
                embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
                await ctx.send(embed=embed)
                return
            else:
                await ctx.send(
                    "You don't have PC. To work as blogger, you need to have PC. What, you thought you would be able to write blog articles without a pc? Yes, you could with mac, but they're overpriced so we don't keep them in our shop. Lmao")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.send(
                "You don't have website. To work as blogger, you need to have a blog. What, you thought you would be able to write blog articles without a website? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "shopily" or worktype.lower() == "dropshipper" or worktype.lower() == "dropshipping":
        earnings = random.randrange(100000, 140000)
        earning = lol * float(earnings)
        if "shopily" in bag:
            if "pc" in bag:
                if "website" in bag:
                    earning = int(earning)
                    await revenue(user, earning)
                    if compa is False:
                        earning = earning * 1.2
                    await update_bank(ctx.author, earning)
                    xd = await multipliery(ctx.author)
                    embed = discord.Embed(title="You just worked!",
                                          description=f"You just fixed a car. You got paid ◉ {earning:,.0f} coins for that",
                                          colour=discord.Colour.blue())
                    embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
                    await ctx.send(embed=embed)
                    return
                else:
                    await ctx.send(
                        "You don't have a website. To work as dropshipper, you need to have website. What, you thought you would be able to dropship without a website? Lmao")
                    ctx.command.reset_cooldown(ctx)
                    return
            else:
                await ctx.send(
                    "You don't have PC. To work as dropshipper, you need to have PC. What, you thought you would be able to dropship without a pc? Lmao")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.send(
                "You don't have shopily. To work as dropshipper, you need to have shopily. What, you thought you would be able to dropship without shopily? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "pilot" or worktype.lower() == "plane" or worktype.lower() == "plane pilot":
        earnings = random.randint(200000, 280000)
        earning = lol * float(earnings)
        if "pilot_license" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just flew an airplane. This must be so pog, right? You even earned ◉ {earning:,.0f} coins!", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You don't have pilot license! To work, you need to get it first, what, you thought you would be able to fly planes without a pilot license? Crash guaranteed lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "lawyer" or worktype.lower() == "law" or worktype.lower()== "court":
        earnings = random.randint(200000, 280000)
        earning = lol * float(earnings)
        if "lawyer" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just defended someone. He paid you ◉ {earning:,.0f} coins.", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You don't have lawyer degree! To work as a lawyer, you need to buy it first, what, you thought you would be able to defend someone in a court without a lawyer degree? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "doctor" or worktype.lower() == "curing" or worktype.lower() == "hospital":
        earnings = random.randint(200000, 280000)
        earning = lol * float(earnings)
        if "doctor" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just cured someone. What a great job, saving other's life. You earned ◉ {earning:,.0f} coins.", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100 * xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You ain't a doctor! To work, you need to be doctor, what, you thought you would be able to cure people without being a doctor? Lmao")
            ctx.command.reset_cooldown(ctx)
            return

    elif worktype.lower() == "finance" or worktype.lower() == "finances" or worktype.lower() == "financial analytic":
        earnings = random.randint(1000000, 1400000)
        earning = lol * float(earnings)
        if "finance" in bag:
            earning = int(earning)
            await revenue(user, earning)
            if compa is False:
                earning = earning * 1.2
            await update_bank(ctx.author, earning)
            xd = await multipliery(ctx.author)
            embed = discord.Embed(title="You just worked!",
                                  description=f"You just analyzed the market. Very money-ish job. You got paid ◉ {earning:,.0f} coins for that.", colour=discord.Colour.blue())
            embed.set_footer(text=f"Multipliers granted you a total of {100*xd:,.0f}% boost!")
            await ctx.send(embed=embed)
            return
        else:
            await ctx.send("You aren't a financial analytic! To work, you need to become a financial analytic first, what, you thought you would be able to analyze the market without being a financial analytic? Yes, you could, but your advice would be just like the Bikini Botton fire department - completly useless.")
            ctx.command.reset_cooldown(ctx)
            return

    else:
        await ctx.send("Specify the right work type!")
        ctx.command.reset_cooldown(ctx)
        return

@work.error
async def work_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+work <type>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
        ctx.command.reset_cooldown(ctx)

@client.command(aliases=["multi"])
async def multipliers(ctx, user:discord.Member = None):

    if user == None:
        user = ctx.author
    await open_account(user)

    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})

    name = doc["multis"]

    embed = discord.Embed(title=f"{user}'s Multipliers:", description="", colour=0x0FFFF)

    if "fly" in name:
        embed.add_field(name=f"Fly -- Common", value=f"Fly helps you with working, giving you a 1% boost!", inline=False)
    if "mosquito" in name:
        embed.add_field(name=f"Mosquito -- Common", value=f"Mosquito gives you a 1 in 7 chance to get a 7% boost!", inline=False)
    if "ladybird" in name:
        embed.add_field(name=f"Ladybird -- Common", value=f"Ladybird is very kind, and gives you a 5% boost for begging!", inline=False)
    if "mouse" in name:
        embed.add_field(name=f"Mouse -- Uncommon", value=f"Mouse helps you with carrying stuff, so you can work 20% faster!", inline=False)
    if "salmon" in name:
        embed.add_field(name=f"Salmon -- Unommon", value=f"Salmon catches you fish, so you get access to `+fish` command!", inline=False)
    if "spider" in name:
        embed.add_field(name=f"Spider -- Rare", value=f"Spider scares you, but it can fit everywhere, so it can rob a bank! Gives you access to `+bankrob` command, where you can rob 10% of somebody's bank!", inline=False)
    if "butterfly" in name:
        embed.add_field(name=f"Butterfly - Rare", value=f"Butterfly defends you from Spider, and it protects you from `+bankrob` command usage!", inline=False)
    if "newton" in name:
        embed.add_field(name=f"NEWTON -- LEGENDARY", value=f"His unbelieveable cuteness gives you 100% boost on everything!", inline=False)

    embed.set_footer(text="Hunt for multipliers with `+hunt` command! | If none are shown, this means the list is empty!")

    await ctx.send(embed=embed)

@client.command(aliases=["multiplierlist"])
async def petlist(ctx):
    embed = discord.Embed(title=f"All possible pets:", description="", colour=discord.Colour.random())

    embed.add_field(name=f"Fly -- Common", value=f"Fly helps you with working, giving you a 1% boost!", inline=False)
    embed.add_field(name=f"Mosquito -- Common", value=f"Mosquito gives you a 1 in 7 chance to get a 7% boost!", inline=False)
    embed.add_field(name=f"Ladybird -- Common", value=f"Ladybird is very kind, and gives you a 5% boost for begging!", inline=False)
    embed.add_field(name=f"Mouse -- Uncommon", value=f"Mouse helps you with carrying stuff, so you can work 20% faster!", inline=False)
    embed.add_field(name=f"Salmon -- Unommon", value=f"Salmon catches you fish, so you get access to `+fish` command!", inline=False)
    embed.add_field(name=f"Spider -- Rare", value=f"Spider scares you, but it can fit everywhere, so it can rob a bank! Gives you access to `+bankrob` command, where you can rob 10% of somebody's bank!", inline=False)
    embed.add_field(name=f"Butterfly - Rare", value=f"Butterfly defends you from Spider, and it protects you from `+bankrob` command usage!", inline=False)
    embed.add_field(name=f"NEWTON -- LEGENDARY", value=f"His unbelieveable cuteness gives you 100% boost on everything!", inline=False)
    embed.set_footer(text="Hunt for pets with `+hunt` command!")

    await ctx.send(embed=embed)

@client.command()
async def roulette(ctx, amount, *, type):
    num = random.randint(1, 37)
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    stt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ndt = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    rdt = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    amount = int(amount)
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]
    if wallet_amt >= amount:
        if type == "0":
            if num == 37:
                amount = amount*35
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: 0. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "even":
            if num != 37 and (num % 2) == 0:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "odd":
            if num != 37 and (num % 2) == 0:
                await update_bank(ctx.author, -1*amount, "wallet")
                await ctx.send(f"Rolled: {num}. You lost ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled {num}. You won ◉ {amount} coins!")
        if type == "red":
            if num in red:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "black":
            if num in black:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "1-18" or type == "first half" or type == "1 to 18" or type == "low":
            if num <= 18:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "19-36" or type == "second half" or type == "19 to 36" or type == "high":
            if num >= 19 and num != 37:
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "1st 12" or type == "first 12" or type == "first dozen":
            if num in stt:
                amount = amount * 2
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "2nd 12" or type == "second 12" or type == "second dozen":
            if num in ndt:
                amount = amount * 2
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        if type == "3rd 12" or type == "third 12" or type == "third dozen":
            if num in rdt:
                amount = amount * 2
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1 * amount, "wallet")
                await ctx.send(f"Rolled {num}. You lost ◉ {amount} coins!")
        else:
            if type == num and num != 37:
                amount = amount * 35
                await update_bank(ctx.author, amount, "wallet")
                await ctx.send(f"Rolled: {num}. You won ◉ {amount} coins!")
            else:
                await update_bank(ctx.author, -1*amount, "wallet")
                await ctx.send(f"Rolled: {num}. You lost ◉ {amount} coins!")
    else:
        await ctx.send(f"You have insufficent funds in your wallet to place a bet of ◉ {amount} coins!")

@client.command()
async def bean(ctx, user:discord.Member, *, reason):
    embed = discord.Embed(title=f"Successfully **Beaned** {user.display_name}", description=f"The user {user.mention} has been successfully **Beaned**")
    embed.add_field(name="Minimod:", value=ctx.author)
    embed.add_field(name="Reason:", value=reason)
    await ctx.send(embed=embed)

@bean.error
async def bean_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        commandformat = "+bean <user> <reason>"
        possible_responses = [
            f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command: **{commandformat}**",
            f"Imagine being such a noob and using the wrong command format: **{commandformat}**",
            f"Lol. Stop using wrong command format u n00b: **{commandformat}**",
            f"smh. use it right: **{commandformat}**",
            f"Only true pros use the right command format. Be one yourself: **{commandformat}**",
            f"Real gamers use commands right: **{commandformat}**",
            f"LMAO Look what a noob uses wrong format!!1!1!!: **{commandformat}**"
        ]
        await ctx.send(random.choice(possible_responses))
    else:
        await ctx.send(error)

@client.command()
async def aeroboy(ctx, user:discord.Member, *, reason):
    if ctx.author.id == 599759136493797377:
        embed = discord.Embed(title=f"Successfully **Aeroboy'd** {user.display_name}", description=f"The user {user.mention} has been successfully **Aeroboy'd**")
        embed.add_field(name="Offender:", value=ctx.author)
        embed.add_field(name="Reason:", value=reason)
        embed.set_image(url="https://cdn.discordapp.com/attachments/820737057693499415/826359543046209576/aeroboy.jpg")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"This command has been reserved for the King Aeroboy! Fuck off you shit!")

@client.command()
async def createcompany(ctx, name):
    discorduserid = ctx.author.id

    doc = enter.find_one({"id": discorduserid})

    await ctx.send(f"Creating a company. Are you sure to create a company with the name {name}? If yes, reply with `yes`, if you wish to cancel the command, reply with `no`. 25.000.000 coins will be charged from your bank.")

    msg = await client.wait_for("message")

    if "yes" in msg.content:

        doc1 = mainbank.find_one({"userid": discorduserid})
        bank_amt = doc1["bank"]
        print(bank_amt)

        ccheck = await checkifcompany(ctx.author)

        if ccheck is True:
            if bank_amt >= 25000000:
                if doc != None:
                    print(doc)
                else:
                    await update_bank(ctx.author, -1*25000000)
                    print(doc)
                    name = name.lower()
                    new_entry = ({"userid": discorduserid, "name": name, "revenue": 0, "employees": [], "totalrevenue": 0})
                    enter.insert_one(new_entry)
                    mainbank.update({"userid": discorduserid}, {"$set": {"company": name}})
                    await ctx.send(f"Successfully created a company `{name}`!")
            else:
                await ctx.send("You don't have enough money in your bank to create a company!")

        else:
            await ctx.send(f"{ctx.author.mention}, you are already in a company! Quit it first!")

    else:
        await ctx.send("Cancelled the command.")

@client.command()
async def employ(ctx, user:discord.User):
    check = await checkifcompany(user)
    userid = ctx.author.id
    if check is True:
        dc = crequests.find_one({"id": user.id})
        if dc == None:
            doc = enter.find_one({"userid": userid})
            print(doc)
            if doc == None:
                await ctx.send("Can't employ user, you're not an owner of a company!")
            else:
                newentry = {"id": user.id, "employerid": userid}
                crequests.insert_one(newentry)
                await ctx.send(f"Successfully sent a job offer to the user {user}!")
                revenue = doc["revenue"]
                trevenue = doc["totalrevenue"]
                eam = doc["employees"]
                id = doc["userid"]
                name = doc["name"]
                embed = discord.Embed(title=f"<@!{id}> sent you a job offer!", description=f"These are the statistics of <@!{id}>'s company {name}!", colour=discord.Colour.random())
                embed.add_field(name="Owner:", value=f"<@!{id}>")
                embed.add_field(name="Total Revenue:", value=f"◉ {trevenue} coins")
                embed.add_field(name="Money:", value=f"◉ {revenue} coins")
                embed.add_field(name="Total employees:", value=f"{eam} users")
                embed.set_footer(text=f"Do +request accept {id} (employer id) to accept the request! +request reject {id} to reject it! +request view to view all offers")
                await user.send(embed=embed)
        else:
            await ctx.send(f"Already sent a request to {user}!")
    else:
        await ctx.send("Can't employ user! They are already in a company!")

@client.command()
async def request(ctx, typeh, id=None):
    aid = ctx.author.id
    if typeh == "accept":
        id = int(id)
        dc = crequests.find_one({"employerid": id})
        if dc == None:
            await ctx.send("Couldn't find a request with that ID! Make sure you specified the right ID!")
        else:
            doc = enter.find_one({"userid": id})
            employeecount = doc["employees"]
            count = employeecount + 1
            enter.update({"userid": id}, {"employees": count})
            name = doc["name"]
            mainbank.update({"userid": aid}, {"$set": {"company": name}})
            await ctx.send(f"Successfully joined <@!{id}>'s company!")
            crequests.delete_many({"id": aid})
    if typeh == "reject":
        dc = crequests.find_one({"employerid": id})
        if dc == None:
            await ctx.send("Couldn't find a request with that ID! Make sure you specified the right ID!")
        else:
            crequests.delete_one({"employerid": id})
            await ctx.send(f"Successfully deleted <@!{id}>'s request!")
    if typeh == "rejectall":
        crequests.delete_many({"id": aid})

@client.command()
async def requests(ctx):
    aid = ctx.author.id
    embed = discord.Embed(title="Your job offers", description="Type +request accept <id> to accept the request, +request reject <id> to reject it, and +request rejectall to reject every request.")
    dc = crequests.find_one({"id": aid})
    if dc == None:
        await ctx.send("You don't have any job offers!")
    else:
        froms = dc["employerid"]
        doc = enter.find_one({"userid": froms})
        cname = doc["name"]
        embed.add_field(name=f"<@!{froms}>'s job offer", value=f"Join the company {cname}!")
        embed.set_footer(text="No more than 10 offers will be shown")
        await ctx.send(embed=embed)

@client.command()
async def cwithdraw(ctx, amount):
    check = await checkifcompany(ctx.author)
    amount = int(amount)

    if check is False:
        userid = ctx.author.id
        doc = enter.find_one({"userid": userid})
        rev = doc["revenue"]
        print(rev)
        rev = int(rev)
        if amount <= rev:
            erev = rev - amount
            erev = int(erev)
            await update_bank(ctx.author, amount)
            enter.update({"userid": ctx.author.id}, {"$set": {"revenue": erev}})
            await ctx.send(f"Successfully withdrawn ◉ {amount} coins from company's money!")
        else:
            await ctx.send("Your company doesn't have enough money to withdraw this much!")

    else:
        await ctx.send("Can't withdraw company's money! You aren't in a company!")
        return

@client.command()
async def stock(ctx):
    await ctx.send("Stock market will soon be available!")

async def buy_this(user:discord.User, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in themainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]

    bag = doc["bag"]

    if wallet_amt<cost:
        return [False,2]

    if item_name not in bag:
        mainbank.update({"userid": discorduserid}, {"$push": {"bag":item_name}})
    else:
        return

    await update_bank(user, cost * -1, "wallet")

    return [True, "worked"]

async def sell_this(user:discord.User, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in themainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = 0,8*item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})

    bag = doc["bag"]

    if item_name not in bag:
        mainbank.update({"userid": discorduserid}, {"$push": {"bag": item_name}})
    else:
        return

    await update_bank(user, price, "wallet")

    return [True, "worked"]

async def checkifcompany(user:discord.User):
    discorduserid = user.id
    doc = mainbank.find_one({"userid": discorduserid})
    company = doc["company"]
    print(company)
    if company == 0:
        return True
    else:
        return False

async def revenue(user:discord.User, amount):
    checkc = await checkifcompany(user)
    if checkc is False:
        doc = mainbank.find_one({"userid": user.id})
        ncompany = doc["company"]
        ent = enter.find_one({"name": ncompany})
        rev = ent["revenue"]
        trev = ent["totalrevenue"]
        updt = 0.2 * float(amount)
        updt = int(updt)
        erev = updt + rev
        etrev = updt + trev
        enter.update({"name": ncompany}, {"$set": {"revenue": erev}})
        enter.update({"name": ncompany}, {"$set": {"totalrevenue": etrev}})
    else:
        return

async def open_account(user:discord.User):
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})

    if doc != None:
        print(doc)
    else:
        print(doc)
        new_entry = ({"userid":discorduserid, "wallet":0, "bank":0, "bag":[], "multis":[], "company":0})
        mainbank.insert_one(new_entry)

async def update_bank(user: discord.User, change=0, mode=None):
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})
    wallet_amt = doc["wallet"]
    bank_amt = doc["bank"]

    if mode == None:
        mode = "bank"
        change = bank_amt + change
    elif mode == "wallet":
        mode = "wallet"
        change = wallet_amt + change
    elif mode == "bank":
        mode = "bank"
        change = bank_amt + change
    else:
        mode = "bank"
        change = bank_amt + change

    new = {"$set": {mode:change}}

    mainbank.update_one(doc, new)

    bal = wallet_amt + bank_amt

    return bal

@client.command()
async def mtestg(ctx):
    discorduserid = ctx.author.id

    doc = mainbank.find_one({"userid": discorduserid})

    try:
        multis = doc["multis"]
    except:
        multis = []

    print(multis)

async def get_multiplier(user:discord.User, name):
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})

    multis = doc["multis"]

    if name not in multis:
        mainbank.update({"userid": discorduserid}, {"$push": {"multis":name}})
        return True
    else:
        return

async def multipliery(user:discord.User):
    discorduserid = user.id

    doc = mainbank.find_one({"userid": discorduserid})

    multiplie = doc["multis"]

    multis = []

    if "fly" in multiplie:
        multis.append(0.01)
    if "mosquito" in multiplie:
        ra = random.randint(1, 7)
        if ra == 1:
            multis.append(0.07)
    if "mouse" in multiplie:
        multis.append(0.01)
    if "newton" in multiplie:
        multis.append(1)

    print(multiplie)

    hhh = sum(multis)

    print(hhh)

    return float(hhh)

async def missingargument(command):
    em = discord.Embed(title="Command Error!", description="A required argument is missing.")
    em.add_field(name="Proper usage of command:", value=f"`{command}`")
    possible_responses = [
        f"Hey, you. Yes you. Don't you want to join the pro gang, always saying the right command?",
        f"Imagine being such a noob and using the wrong command format.",
        f"Lol. Stop using wrong command format u n00b.",
        f"smh. use it right.",
        f"Only true pros use the right command format. Be one yourself.",
        f"Real gamers use commands right.*",
        f"LMAO Look what a noob uses wrong format!!1!1!!"
    ]
    em.set_footer(text=f"{random.choice(possible_responses)}")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/829673561400016917/831804057265766410/BREUH1.png")
    return em

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(TOKEN)
