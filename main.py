import os
import discord
import random
import requests
import json
import time
import keep_alive
import asyncio
from discord.ext import commands


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!grass', intents=intents)


@bot.event
async def on_connect():
  print("your bot is online!")


@bot.command()
async def kick(ctx):
  await ctx.reply("GrassBot says kick joe")

@bot.command()
async def ban(ctx):
  await ctx.reply("GrassBot says ban joe")

@bot.command()
async def add(ctx, num1, num2):
  numTot = int(num1) + int(num2)
  numTot = str(numTot)
  await ctx.reply(num1 + "+" + num2 + "=" + numTot)

@bot.command()
async def pic(ctx):
  piclist=["https://img.youtube.com/vi/q33drZUXSzY/0.jpg", "https://townsquare.media/site/16/files/2012/02/ScreenHunter_18-Feb.-07-14.07.jpg?w=980&q=75"]
  await ctx.reply(random.choice(piclist))
  await ctx.reply("please ban joe")

@bot.command()
async def coinflip(ctx):
  coinsides=["heads","tails"]
  await ctx.reply("it landed on " + random.choice(coinsides) + ", then " + random.choice(coinsides) + ", then " + random.choice(coinsides))
  await ctx.reply("also can we please ban joe")

@bot.command()
async def roll(ctx, num):
  username = ctx.message.author.name
  outOf = int(num)
  
  nums=random.randint(0,outOf)
  await ctx.reply(username + " rolled " + str(nums))

@bot.command()
async def joke(ctx):
  url = "https://official-joke-api.appspot.com/random_joke"
  req = requests.get(url)
  data = req.json()
  setup = data["setup"]
  await ctx.send(setup)
  punchline = data["punchline"]
  await asyncio.sleep(2)
  await ctx.send(punchline)

@bot.command()
async def weather(ctx):
  my_secret_weather = os.environ['WEATHER_API_KEY']

  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" + my_secret_weather 

  req = requests.get(url)
  data = req.json()
  desc = data ["weather"][0]["description"]
  
  
  #setup = data["setup"]
  await ctx.send(desc)

@bot.command()
async def RPC(ctx):
  word = 0
  word1 = 0


@bot.command()
async def IPinfo(ctx, ip):
  url = "https://ipinfo.io/" + ip + "/geo"

  req = requests.get(url)

  data = req.json()

  city = data["city"]
  region = data["region"]
  country = data["country"]
  timezone = data["timezone"]

  await ctx.reply("City: " + city + "\nState: " + region + "\nCountry: " +
                  country + "\nTimezone: " + timezone + ".")


@bot.command()
async def blur(ctx):
  printlist=["a", "b", "c", "d", "e","f", "g", "h", "i", "j","k", "l", "m", "n", "o","p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z", "-", "/", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ":"]
  message = ctx.message
  for attachment in message.attachments:
    img = attachment.url
  url = "https://api.apilayer.com/face_pixelizer/url?url=" + img

  payload = {}
  headers = {"apikey":"Sz8div64BU43dql72fPmqcxMkGbJWQRJ"}

  response = requests.request("GET", url, headers=headers, data=payload)
  result = response.text
  result2=""
  for char in result:
    if char in printlist:
      result2 += char
  await ctx.reply(result2[7:])

  
  
  
keep_alive.keep_alive()
my_secret = os.environ['BOT_TOKEN']
bot.run(my_secret)
