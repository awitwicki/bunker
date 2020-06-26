from config import TOKEN
import discord
from discord.ext import commands
from generator import *


bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'

room = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.command(name='start', help='Начать набор в игру.') #разрешаем передавать агрументы
async def start(context): #создаем асинхронную фунцию бота
    creator = context.author

    isCreatorCan = [ True if r.name == 'Bunker admin' else False for r in creator.guild.roles]
    if not any(isCreatorCan):
        message = await context.send("Только пользователь с ролью 'Bunker admin' может создавать игры.")
        return

    room[creator.id] = creator

    response = build_register_message()
    message = await context.send(response)

    await message.add_reaction("☢️")
    await context.message.delete()

@bot.command(name='go', help='Начать игру.') 
async def go(context): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    apocalypse = randomize_apocalypse()
    message = await context.send(apocalypse)

    for user_id in room:
        user = bot.get_user(user_id)
        message = 'Вот твои хараеткристики:\n'
        message += randomize_profile()
        await user.send(message)

    await context.message.delete()

@bot.command(name='finish', help='Закончить игру.') #разрешаем передавать агрументы
async def finish(context): #создаем асинхронную фунцию бота
    global room
    creator = context.author

    if creator.id is not list(room.keys())[0]:
        return

    room = {}

    rawno = '================================================================================================================='
    message = await context.send(rawno)
    message = await context.send("Игра окончена, все умерли.")
    message = await context.send(rawno)
    # message = await channel.send('hmm…')

    await message.add_reaction("😀")
    await message.add_reaction("☹️")
    await context.message.delete()

@bot.command(name='newcard', help='Сгенерировать карту для @пользователя.') 
async def newcard(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твоя новая карта:\n'
        message += randomize_card()
        await user.send(message)
    await context.message.delete()

@bot.command(name='newprofession', help='Сгенерировать профессию для @пользователя.') 
async def newprofession(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твоя новая Профессия:\n'
        message += randomize_profession()
        await user.send(message)
    await context.message.delete()

@bot.command(name='newbagage', help='Сгенерировать багаж для @пользователя.') 
async def newcard(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твой багаж:\n'
        message += randomize_bagage()
        await user.send(message)
    await context.message.delete()

@bot.command(name='newhealth', help='Сгенерировать состояние здоровья для @пользователя.') 
async def newcard(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твое новое здоровье:\n'
        message += randomize_health()
        await user.send(message)

    await context.message.delete()

@bot.command(name='newhobby', help='Сгенерировать хобби для @пользователя.') 
async def newcard(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твоё новое хобби:\n'
        message += randomize_hobby()
        await user.send(message)

    await context.message.delete()

@bot.command(name='newbio', help='Сгенерировать полроствес для @пользователя.') 
async def newcard(context, *args): #создаем асинхронную фунцию бота
    creator = context.author
    if creator.id is not list(room.keys())[0]:
        return

    for id_arg in args:
        user_id = int(id_arg.replace('<@!','').replace('>',''))
        if user_id not in list(room.keys()):
            message = await context.send("error, wrong user")

        user = bot.get_user(user_id)
        message = 'Вот твой новый полроствес:\n'
        message += randomize_bio()
        await user.send(message)

    await context.message.delete()

@bot.event
async def on_reaction_add(reaction, user):
    # add user
    #ignore bot reactions
    if user.id == bot.user.id:
        return

    if not user.id in room and reaction.emoji == '☢️':
        room[user.id] = user
        await reaction.message.edit(content=build_register_message())

    # await context.send(reaction.emoji)
    # if reaction.emoji == '\U0001F602':
    #     print("match")

def build_register_message():
    response = "Ок, начинаем рагистрацию в группу, все кто хочет учавствовать, нажмите на бомбу под этим сообщением.\nЗарегистрированые люди:"
    for user_id in room:
        response+=f'\n{room[user_id].mention}'
    
    response += '\n\nЧтобы начать игру, создатель игры должен написать !go'

    return response

# send tu user
# user = client.get_user(381870129706958858)
# await user.send('👀')

# or
# await message.author.send('👋')

bot.run(TOKEN)