data={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
data2=list(filter(lambda x: data[x]>0,data))
print(data2)