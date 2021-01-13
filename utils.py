def is_author_game_creator(context, room):
    author = context.author
    return author.id == list(room.keys())[0]


def is_author_bunker_admin(context):
    author = context.author
    return any(r.name == 'Bunker admin' for r in author.guild.roles)


def filter_players_not_in_room(room):
    def double_wrap(func):
        async def wrap(context, *args, **kwargs):
            users_in_room = []
            for user_mention in args:
                user_id = convert_mention_to_user_id(user_mention)
                if user_id in room:
                    users_in_room.append(user_mention)
                else:
                    await context.send(f"Error, {user_mention} not in room")
            return await func(context, *users_in_room, **kwargs)
        return wrap
    return double_wrap


def convert_mentions_to_user_ids(func):
    async def wrap(context, *args, **kwargs):
        user_ids = tuple(convert_mention_to_user_id(user_mention) for user_mention in args)
        return await func(context, *user_ids, **kwargs)
    return wrap


def convert_mention_to_user_id(mention):
    return int(mention.replace('<@!', '').replace('>', ''))