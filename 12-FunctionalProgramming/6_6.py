arr=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
tr=list(map(lambda x:x[0].upper(),arr))
print('\n'.join([f'{arr[i][0].upper()}, {arr[i][1]}' for i in range(len(arr))]))