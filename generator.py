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

def randomize_profile():
    string = ''
    keys = list(dictd.keys())

    sex = random.choice(dictd['Пол'].split('.'))
    age = random.choice(dictd['Возраст'].split('.'))
    plod = random.choice(dictd['Плодовитость'].split('.'))
    string = f'Пол: {sex}, Возраст : {age}, Плодовитость : {plod}.\n'

    for key in keys[4:]:
        values = dictd[key].split('.')
        val = random.choice(values)
        if key == list(dictd.keys())[-1]:
            val2 = random.choice(values)
            string = string + f'{key}: {val2}\n'
        string = string + f'{key}: {val}\n'
    # print(string)
    return string


def randomize_card():
    string = ''
    key = 'Карты'
    val = random.choice(dictd[key].split('.'))
    string = string + f'{key}: {val}\n'
    # print(string)
    return string

def randomize_profession():
    string = ''
    key = 'Профессия'
    val = random.choice(dictd[key].split('.'))
    string = string + f'{key}: {val}\n'
    # print(string)
    return string

def randomize_bagage():
    string = ''
    key = 'Багаж'
    val = random.choice(dictd[key].split('.'))
    string = string + f'{key}: {val}\n'
    # print(string)
    return string

def randomize_health():
    string = ''
    key = 'Состояние здоровья'
    val = random.choice(dictd[key].split('.'))
    string = string + f'{key}: {val}\n'
    # print(string)
    return string

def randomize_hobby():
    string = ''
    key = 'Хобби'
    val = random.choice(dictd[key].split('.'))
    string = string + f'{key}: {val}\n'
    # print(string)
    return string

def randomize_bio():
    string = ''
    sex = random.choice(dictd['Пол'].split('.'))
    age = random.choice(dictd['Возраст'].split('.'))
    plod = random.choice(dictd['Плодовитость'].split('.'))
    string = f'Пол: {sex}, Возраст : {age}, Плодовитость : {plod}.\n'
    return string

def randomize_apocalypse():
    string = random.choice(dictd['Катастрофа'].split(';'))
    return string

def create_profiles(count):
    profiles = []
    for index in range(count):
        profiles.append(randomize_profile())

    return profiles

# randomize_profile()