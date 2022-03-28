import os
from contextvars import Context
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
from Game import getQuestion


load_dotenv(dotenv_path="config")



bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)



@bot.command()
async def square(ctx, arg): 
    print(arg)
    await ctx.send(int(arg) ** 2) 

@bot.command()
async def test(ctx):
    q0,q1,q2,q3,q4=getQuestion(1)
    await ctx.send(q0)

@bot.command()
async def launch(ctx):

    await ctx.send("**Lancement du jeu...**")
    i =1
    while(i != 16):
        q0,q1,q2,q3,q4,verif=getQuestion(i)
        await ctx.send(q0)
        await ctx.send(q1)
        await ctx.send(q2)
        await ctx.send(q3)
        await ctx.send(q4)

        check = lambda m: m.author == ctx.author and m.channel == ctx.channel
        try:
            confirm = await bot.wait_for("message", check=check, timeout=20)
        except asyncio.TimeoutError:
            print("ERROR 404")
            return

        if confirm.content == str(verif):
            await ctx.send("Bonne reponse !")
            i+=1
        else:
            await ctx.send(f'Mauvaise réponse ! Vous avez atteint le palier numéro {i}')
            await ctx.send("|| spoiler N'hésite pas à mettre une étoile au projet : https://github.com/s1o0/QuiVeutGagnerDesMillions ||")
            break
            

@bot.command()
async def infos(ctx):   
    i1 = "**Bienvenue sur Qui Veut Gagner des Millions ! **"
    i2 = "Pour pouvoir voir le classement du bot : !leaderboard"
    i3 = "Pour pouvoir lancer une partie : !launch"
    i4 = "Pour faire apparaître une question au hasard : !questionR"
    await ctx.send(i1)
    await ctx.send(i2)
    await ctx.send(i3)
    await ctx.send(i4)
    

bot.run(os.getenv("TOKEN"))
