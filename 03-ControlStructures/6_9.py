name=input('Enter a name: ')
if name[len(name)-1]=="a":
    print(f'{name.capitalize()} -- Polish female name')
else:
    print(f'{name.capitalize()} -- not Polish female name')