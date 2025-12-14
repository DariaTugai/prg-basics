name=input('enter file name: ')
with open(name,'r') as file:
    content=file.read().splitlines()
    numlines=len(content)
    numchar=0
    for line in content:
        numchar+=len(line)
print(numlines)
print(numchar)