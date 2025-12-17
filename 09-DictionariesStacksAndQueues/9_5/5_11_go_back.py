import json
try:
    with open('voting.json', 'r', encoding='utf-8') as js:
        diction = json.load(js)
except (FileNotFoundError, json.JSONDecodeError):
    diction = {}


with open('voting.json','w', encoding='utf-8') as js:
    person_name = input('Name of the person you are voting for:')
    if person_name in diction:
        diction[person_name]+=1
    else:
        diction[person_name]=1
    json.dump(diction,js)
