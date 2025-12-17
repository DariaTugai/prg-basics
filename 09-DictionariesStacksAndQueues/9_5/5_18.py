import json
with open('dogs.json','r',encoding='utf-8') as file:
    data=json.load(file)
    for item in data:
        if item['age']<5:
            for key,value in item.items():
                print(key,':',value)
            print()