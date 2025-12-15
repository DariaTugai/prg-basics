import csv 
pr=[]
with open('clothing.csv','r') as file:
    context=csv.reader(file)
    next(context)
    for line in context:
        if float(line[5])<60 and float(line[6])<40:
            pr.append(line)
    for x in pr:
        print(''.join(x[1]))