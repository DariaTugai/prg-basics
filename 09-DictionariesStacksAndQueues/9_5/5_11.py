import json
with open('voting.json','r+', encoding='utf-8') as file:
    contents=json.load(file)
    diction={}
    person_name = input('Name of the person you are voting for:')
    if person_name in diction:
        diction[person_name]+=1
    else:
        diction[person_name]=1
    json.dump(diction,file)
    

# Save voting data to json file
...