import json
with open('reservations.json', 'r', encoding='utf-8') as file:
    data=json.load(file)

def room_num(content):
    rooms=len(content['reservations'])
    return rooms

print(room_num(data))
        
        

