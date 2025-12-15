import csv
designers=[]
with open('it_company.csv') as file:
    content= csv.reader(file)
    for line in content:
        if line[2]=='Graphic Designer':
            designers.append(line)
print('GRAPHIC DESIGNERS')
print('=================')
for line in designers:
    print(f'{line[0]} {line[1]}, {line[3]}')
