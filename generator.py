import io, json, random
import json

dictd = {}

with open('db.json', "r", encoding="utf-8") as file:
    jsonfile = file.read()
    dictd = json.loads(jsonfile)
    print("Profiles database is succefully parsed")
    # print(dictd)
    # for key in dictd.keys():
    #     values = dictd[key].split('.')
    #     val = random.choice(values)
    #     print(f'{key} : {val}')



# def randomize_bunker():
#     string = ''
#     area = random.choice(50, 300)
#     food_water = random.choice(dictd["Еда и питье"].split('.'))
#     area = random.choice(50, 300)
#     need_time = random.choice(dictd["Время нахождения в убежище"].split('.'))
    
#     key = 'Карты'
#     val = random.choice(dictd[key].split('.'))
#     string = string + f'{key}: {val}\n'
#     # print(string)
#     return string
def randomize_profile():
    string = 'Вот твои хараеткристики:\n'
    string += randomize_profession()
    string += randomize_bio()
    string += randomize_health()
    string += randomize_mind()
    string += randomize_hobby()
    string += randomize_phobies()
    string += randomize_bagage()
    string += randomize_skill()
    string += randomize_card()
    string += randomize_card()
    
    return string

def randomize_card():
    key = 'ACTIONCARDS'
    items = dictd[key]
    val = random.choice(items)
    string =f'Карта действия: {val}\n'
    return string

def randomize_profession():
    key = 'PROF'
    items = dictd[key]
    val = random.choice(items)
    string = f'Профессия: {val}\n'
    return string

def randomize_bagage():
    key = 'INV'
    items = dictd[key]
    val = random.choice(items)
    string = f'Багаж: {val}\n'
    return string

def randomize_health():
    key = 'HEALTH'
    items = dictd[key]
    val = random.choice(items)
    string = f'Здоровье: {val}\n'
    return string

def randomize_mind():
    key = 'CHARACTER'
    items = dictd[key]
    val = random.choice(items)
    string = f'Характер: {val}\n'
    return string

def randomize_hobby():
    key = 'HOBBIES'
    items = dictd[key]
    val = random.choice(items)
    string = f'Хобби: {val}\n'
    return string

def randomize_phobies():
    key = 'PHOBIES'
    items = dictd[key]
    val = random.choice(items)
    string = f'Фобия: {val}\n'
    return string

def randomize_skill():
    key = 'SKILLS'
    items = dictd[key]
    val = random.choice(items)
    string = f'Умение: {val}\n'
    return string

def randomize_bio():
    PLAYERINFO = dictd['PLAYERINFO']
    sex = random.choice(PLAYERINFO['GENDER'])
    age = random.choice(PLAYERINFO['AGE'])
    plod = random.choice(PLAYERINFO['SEX'])
    string = f'Пол: {sex}, Возраст : {age}, Плодовитость : {plod}.\n'
    return string

def randomize_apocalypse():
    string = random.choice(dictd['APOCALYPSES'])
    return string

def create_profiles(count):
    profiles = []
    for index in range(count):
        profiles.append(randomize_profile())

    return profiles


# test
# new = randomize_apocalypse()
# print(new + '\n')

# new = randomize_profile()
# print(new)
