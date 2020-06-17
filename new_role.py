import io, json, random
import json

with open('db.json', "r", encoding="utf-8") as file:
    jsonfile = file.read()
    dictd = json.loads(jsonfile)
    # print(dictd)
    for key in dictd.keys():
        values = dictd[key].split('.')
        val = random.choice(values)
        print(f'{key} : {val}')
