import json
d={'name':'Interstellar','year':'2002','hhhh':'uuuu','iii':90,'uii':00}
with open('favourite.json','w') as file:
    data=json.dump(d,file)