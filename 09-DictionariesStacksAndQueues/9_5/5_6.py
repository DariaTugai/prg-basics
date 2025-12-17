basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}
person={}
for i,x in basic_data.items():
    person[i]=x
for y,z in advanced_data.items():
    person[y]=z
print(person)