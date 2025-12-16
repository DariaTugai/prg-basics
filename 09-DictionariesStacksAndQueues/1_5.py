import random
listc=['Poland','Germany','Italy','Cyprus','UK']
arr=[{'country':country, 'population':random.randint(40,90)} for country in listc]
print('COUNTRY  POPULATION')
for dict in arr:
    print(dict['country'],dict['population'])
    # for y in dict.values():
        # print(y,end=' ')
  