import re
with open('files.txt','r') as file:
    cont=file.read().splitlines()
    lines=[]
    for line in cont:
        regex='\.[a-z]{4}'
        wer=re.search(regex,line)
        if wer:
            lines.append(line)
print('\n'.join(lines))