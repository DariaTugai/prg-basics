arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest=''
for i in arr:
    if len(i)>len(longest):
        longest=i
print(longest)