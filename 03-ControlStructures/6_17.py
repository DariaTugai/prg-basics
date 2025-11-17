four=(input('enter time in 24-hour format (hh:mm): '))
apm=''
if int(four[0:2])>=0 and int(four[0:2])<12:
    apm='am'
    firsttwo=int(four[0:2])
else:
    apm='pm'
    firsttwo=int(four[0:2])-12
print (f'In 12-hour format it\'s {firsttwo}:{four[3:5]} {apm}.')