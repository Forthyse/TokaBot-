from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, has_permissions, MissingPermissions
import discord
import random 
import json
import os
import asyncio

bot = commands.Bot(command_prefix="t!")
bot.sniped_messages = {}
bot.remove_command("help")

roasts = [
    "Roses are red violets are blue, God made me pretty, what happened to you?",
    "You're so ugly when you looked in the mirror your reflection walked away.",
    "I would ask you how old you are but I know you can't count that high.",
    "The only way you'll ever get laid is if you crawl up a chicken's arse and wait.",
    "I'm busy right now. Can I ignore you some other time?",
    "I'd like to help you out. Which way did you come in?",
    "Your mums so fat not even Dora could explore her.",
    "Your face looks like a cat tried to crawl out of a melon :pleading_face:",
    "I hope your chooks turn into emus and kick your shithouse down.",
    "I may look like a failed abortion but I'm glad I don't look like you.",
    "I hope your balls turn into bicycle wheels and backpedal up your arse.",
    "Shut your trap ya floozy cunt.",
    "Sarcasm falls out of my mouth like stupidity falls out of yours.",
    "Take a diaper for the amount of shit that comes out of your mouth.",
    "If you ran like your mouth you'd be in good shape.",
    "Sorry for pushing your buttons I was looking for mute.",
    "You have the personality of a moldy cum sock.",
    "Some day you'll go far and I hope you stay there.",
    "Guys, let the retard speak.",
    "I'd agree with you but we'd both be wrong.",
    "Suck my big black chode.",
    "I can smell your moldy toes from here.",
    "Fuck yer mum.",
    "Put a dick in it ya degenerate skank.",
    "Quit fucking around with me and go back to your whorehouse.",
    "Quit your yapping and eat another burger ya yankee doodle fatarse.",
    "Mirrors can't talk. Lucky for you, they can't laugh either.",
    "Were you born on a highway? Cause that's where most accidents happen.",
    "I reckon you're the reason plastic surgery was created.",
    "I love shopping as much as the next guy but I would never buy your bullshit.",
    "I'm an acquired taste. If you don't like me, acquire some taste.",
    "Of course I'm talking like an idiot. How else would ya understand me?",
    "Don't come after me for my looks when you look like a deformed cockroach.",
    "Need some ranch for that baby carrot you call a donger?",
    "If I wanted a bitch, I would've bought a dog.",
    "Your maker must have been on LSD when you were created.",
    "I hope a paraplegic runs you over with their wheelchair.",
    "A pussycat has bigger balls than yours.",
]

flirts = [
    "Are you a school bus? Cause I wanna put my kids in ya :smirk:",
    "Are you a chicken farmer? Cause you're raisin these cocks.",
    "Age is just a number, so can I get yours? :pleading_face:",
    "If you were a Transformer you'd be Optimus Fine.",
    "Wanna blow my didgeridoo?", "I wanna get lost in your Outback :flushed:",
    "I got the 'std' in 'stud,' now I just need u :wink:",
    "Are you from Australia? Cause I'd like to visit ya down under <:hhh:803462048209960990>",
    "Is your name winter? Cause you'll be coming soon.",
    "Is it hot in here or is it just you?",
    "Roses are red. Violets are fine. You be the 6. I’ll be the 9 <:smug:805821907110068264>",
    "If you're feeling down, I can feel you up :smirk:",
    "Damn, you're so hot my zipper's falling for ya.",
    "You got any Australian in you? Do ya want some? :smirk:",
    "I’m not a weatherman, but you can expect a few more inches tonight.",
    "Tell me what it's like being so beautiful.",
    "You must be exhausted. You've been running through my mind all day.",
    "Can I have a band-aid? I scraped my knee falling for ya.",
    "What time do you get off? Can I watch? :flushed:",
    "Is your name Google? Because you have everything I’ve been searching for.",
    "I’m learning about important dates in history. Wanna be one of them?",
    "I put the 'laid' in 'Adelaide' <:hhh:803462048209960990>",
    "Are you a hot dog cause I wanna put this weiner between your buns <:hhh:803462048209960990>"
]

nbypass = [
    "n i g g e r", "nlg","n i g g a", "n1gger", "NIGGER", "NIGGA", "nigga", "Nigga", "nigg", "Nigg",
    "Ni6", "N1g", "Ni9", "N16,", "N19", "n1g", "ni6", "ni9", "n16", "n19",
    "n1993r", "Níggä", "Nïgger", "ni9"
]

fbypass = [
    "f4g", "fag", "f@g", "f 4 g", "f a g", "f @ g", "Fag", "FAGGOT", "Faggot"
]

grabify = [
    "lovebird.guru", "trulove.guru", "dateing.club", "otherhalf.life",
    "shrekis.life", "headshot.monster", "gaming-at-my.best",
    "progaming.monster", "yourmy.monster", "screenshare.host",
    "imageshare.best", "screenshot.best", "gamingfun.me", "catsnthing.com",
    "mypic.icu", "catsnthings.fun", "curiouscat.club", "joinmy.site",
    "fortnitechat.site", "fortnight.space", "freegiftcards.co", "stopify.co",
    "leancoding.co", "grabify.link", "you.tube.com"
]

@bot.event
async def on_ready():
  print("This Bot is Up and Running!")
  await bot.change_presence(activity=discord.Game(
      name="t!help | Made by Toka#8008"))

# Snipe Command

@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author,
                                             message.channel.name,
                                             message.created_at)


@bot.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = bot.sniped_messages[
            ctx.guild.id]

    except:
        await ctx.channel.send("Nothing to snipe dummy.")
        return
    embed = discord.Embed(description=contents,
                          color=ctx.author.color,
                          timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}",
                     icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in #{channel_name}")

    await ctx.send(embed=embed)

# Ping Command

@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! `{round(bot.latency * 1000)}`ms")

# Roast Command

@bot.command(pass_context=True)
async def roast(ctx, member: discord.Member = None):
    rand = random.choice(roasts)
    if member is None:
        member = ctx.message.author
        await ctx.send(f"{rand}")
    else:
        await ctx.send(f"{rand} <@{member.id}>")

# Flirt Command

@bot.command()
async def flirt(ctx, member: discord.Member = None):
    rand = random.choice(flirts)
    if member is None:
        await ctx.send(f"{rand}")
    else:
        await ctx.send(f"{rand} <@{member.id}>")

# Warn Command

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@bot.command(pass_context = True)
@has_permissions(manage_messages=True, administrator=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await client.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await ctx.send(f"{user.name} has never been reported")  

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await ctx.send_message(ctx.message.channel, text)   

# Purge Command

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

# Anti Bypass
@bot.listen("on_message")
async def el_message(message):
    if message.author.id != 707426973370286171:
        if f"{bot.user.id}" in message.content:
            msg = await message.channel.send(
                "Don't ping TokaBot unless it's important.")
            await message.delete()
            await asyncio.sleep(4)
            await msg.delete()
        for word in grabify:
            if word in message.content:
                msg = await message.channel.send(
                    f"Nobody falls for those grabify links stupid. <@{message.author.id}>"
                )
                await message.delete()
        for nword in nbypass:
            if nword in message.content:
                role = discord.utils.get(message.guild.roles,
                                         name="N-word Pass")
                if role not in message.author.roles:
                    msg = await message.channel.send(
                        "Don't be racist you dumb fuck.")
                    await asyncio.sleep(0.01)
                    await message.delete()
                    await asyncio.sleep(4)
                    await msg.delete()
                elif role in message.author.roles:
                    pass
        for fword in fbypass:
            if fword.lower() in message.content or "Fag" in message.content or "fag" in message.content:
                role = discord.utils.get(message.guild.roles,
                                         name="F-slur Pass")
                if role not in message.author.roles:
                    msg = await message.channel.send(
                        "Don't be homophobic Dumbass.")
                    await asyncio.sleep(0.01)
                    await message.delete()
                    await asyncio.sleep(4)
                    await msg.delete()
                elif role in message.author.roles:
                    pass

# Help Command 

@bot.command()
async def help(ctx):
  author = ctx.message.author

  help_embed = discord.Embed(colour = discord.Colour.red()
  )
  help_embed.set_author(name="BOT PREFIX = t!")
  help_embed.add_field(name="Help",value="Displays this message!", inline=False)
  help_embed.add_field(name="Ping",value="Returns the amount of ping for the Bot!", inline=False)
  help_embed.add_field(name="Snipe",value="Tells you the last deleted message!", inline=False)
  help_embed.add_field(name="Roast",value="Roasts someone!", inline=False)
  help_embed.add_field(name="Flirt", value="Flirt with someone!", inline=False)
  help_embed.add_field(name="Warn", value="Warn a User for bad behavior!", inline=False)
  help_embed.add_field(name="Warnings", value="Check yours or another user's warnings!", inline=False)

  await ctx.send(embed=help_embed)

bot.run('[IINSERT YOUR BOT TOKEN HERE!]')
