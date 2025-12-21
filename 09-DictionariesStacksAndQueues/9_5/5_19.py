import json
with open('reservations.json', 'r', encoding='utf-8') as file:
    data=json.load(file)
    print((data))

def room_num(content):
    rooms=len(content['reservations'])
    return rooms

print(room_num(data))
        
def paid(content):
    total=0
    for dict in content['reservations']:
        if dict["paid"]== True:
            total+=1
    return total
print(paid(data))

def value(content):
    total=0
    for dict in content['reservations']:
        if dict["paid"]== True:
            total+=dict[ "price_per_night"]
        # for k,v in dict.items():



        
       


        

