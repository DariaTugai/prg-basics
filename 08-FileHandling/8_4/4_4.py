with open('it_company.csv','r') as it:
    content= it.read().splitlines()
    x=0
    y=5
    for line in content[x:y]:
        print(line)
    
    while True:
        ok='j'
        ok=input('Press enter key to continue.')
        if y<=len(content):
            if ok=='':
                x+=5
                y+=5
                for line in content[x:y]:
                     print(line)
        else:
            print('end of document')
            break
