import re
text=input('enter text: ')
quant=0
for word in text:
    regex='[aoyuie]+'
    isi=re.findall(regex,word)
    quant+=len(isi)
print(quant)