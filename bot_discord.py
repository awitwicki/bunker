import datetime
import traceback

from discord.ext import commands

from config import TOKEN
from generator import *
from utils import is_author_game_creator, is_author_bunker_admin, filter_players_not_in_room, \
    convert_mentions_to_user_ids

bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'

room = {}

general_text_channel_id = 798563385927139381


# # # Info


@bot.event
async def on_connect():
    msg = f'{bot.user.name} has connected!'
    await bot.get_channel(general_text_channel_id).send(msg)
    print(msg)


@bot.event
async def on_ready():
    msg = f'{bot.user.name} is ready!'
    await bot.get_channel(general_text_channel_id).send(msg)
    print(msg)


@bot.event
async def on_resume():
    msg = f'{bot.user.name} was resumed!'
    await bot.get_channel(general_text_channel_id).send(msg)
    print(msg)


@bot.event
async def on_disconnect():
    msg = f'{bot.user.name} has disconnected!'
    await bot.get_channel(general_text_channel_id).send(msg)
    print(msg)


@bot.event
async def on_error(event, *args, **kwargs):
    exception_str = traceback.format_exc()
    msg = f'{bot.user.name} encountered an error ' \
          f'at {datetime.datetime.now()} ' \
          f'while handling {event} event ' \
          f'with args {args} ' \
          f'and kwargs {kwargs} ' \
          f':\n' \
          f'{exception_str}'
    await bot.get_channel(general_text_channel_id).send(msg)
    print(msg)

    with open('err.log', 'a') as f:
        f.write(msg)


# # # Game commands


@bot.command(name='start', help='Начать набор в игру.')
@commands.check(is_author_bunker_admin)
async def start(context):
    room[context.author.id] = context.author

    response = build_register_message()
    message = await context.send(response)

    await message.add_reaction("☢️")
    await context.message.delete()


@bot.command(name='go', help='Начать игру.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
async def go(context):
    apocalypse = randomize_apocalypse()
    message = await context.send(apocalypse)

    for user_id in room:
        user = await bot.fetch_user(user_id)
        message = 'Вот твои хараеткристики:\n' \
                  f'{randomize_profile()}'
        await user.send(message)
    await context.message.delete()


@bot.command(name='finish', help='Закончить игру.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
async def finish(context):
    global room
    room = {}

    message = await context.send(
        f"{'='*50}\n"
        "Игра окончена, все умерли.\n"
        f"{'='*50}"
    )

    await message.add_reaction("😀")
    await message.add_reaction("☹️")
    await context.message.delete()


@bot.command(name='newcard', help='Сгенерировать карту для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newcard(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твоя новая карта:\n'
        message += randomize_card()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newprofession', help='Сгенерировать профессию для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newprofession(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твоя новая Профессия:\n'
        message += randomize_profession()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newprofessions', help='Сгенерировать профессию для всех.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
async def go(context):
    for user_id in room:
        user = await bot.fetch_user(user_id)
        message = 'Вот твоя новая Профессия:\n'
        message += randomize_profession()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newbagage', help='Сгенерировать багаж для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newcard(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твой багаж:\n'
        message += randomize_bagage()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newhealth', help='Сгенерировать состояние здоровья для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newcard(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твое новое здоровье:\n'
        message += randomize_health()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newhobby', help='Сгенерировать хобби для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newcard(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твоё новое хобби:\n'
        message += randomize_hobby()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newhobbies', help='Сгенерировать хобби для всех.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
async def newhobbies(context):
    for user_id in room:
        user = await bot.fetch_user(user_id)
        message = 'Вот твое новое Хобби:\n'
        message += randomize_hobby()
        await user.send(message)

    await context.message.delete()


@bot.command(name='newbio', help='Сгенерировать полроствес для @пользователя.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
@filter_players_not_in_room(room=room)
@convert_mentions_to_user_ids
async def newcard(context, *args):
    for user_id in args:
        user = await bot.fetch_user(user_id)
        message = 'Вот твой новый полроствес:\n'
        message += randomize_bio()
        await user.send(message)
    await context.message.delete()


@bot.command(name='newapocalypse', help='Сгенерировать новую катастрофу.')
@commands.check(is_author_bunker_admin)
@commands.check(lambda context: is_author_game_creator(context, room))
async def newapocalypse(context, *args):  # создаем асинхронную фунцию бота
    apocalypse = randomize_apocalypse()
    message = await context.send(apocalypse)
    await context.message.delete()


@bot.event
async def on_reaction_add(reaction, user):
    if user.id != bot.user.id \
            and user.id not in room \
            and reaction.emoji == '☢️':

        room[user.id] = user
        await reaction.message.edit(content=build_register_message())


def build_register_message():
    confirmed_players = [user.mention for user in room.values()]

    response = "Ок, начинаем рагистрацию в группу, " \
               "все кто хочет учавствовать, нажмите на бомбу под этим сообщением.\n" \
               f"Зарегистрированые люди:{confirmed_players}" \
               "\n\n" \
               "Чтобы начать игру, создатель игры должен написать !go"

    return response


bot.run(TOKEN)
