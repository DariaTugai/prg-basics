import csv
dict_prov={}
total={}
with open('province.csv','r', encoding='utf-8', errors='replace') as prov:
    provinces=csv.reader(prov)
    next(provinces)
    for i in provinces:
        dict_prov[i[0]]=i[1]


with open('vehicle.txt','r') as vehicle:
    content=vehicle.read().splitlines()
    for line in content:
        if dict_prov[line[0]] in total:
            total[dict_prov[line[0]]]+=1
        else:
            total[dict_prov[line[0]]]=1

print(total)
       



