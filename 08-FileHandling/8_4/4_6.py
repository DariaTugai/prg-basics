name=input('enter file name: ')
with open(name,'r') as file:
    content=file.read().splitlines()
    numlines=len(content)
    numchar=0
    numwor=0
    for line in content:
        words= line.split()
        numwor+=len(words)
        for word in words:
            numchar+=len(word)
print(numlines)
print(numchar)
print(f'words: {numwor}')