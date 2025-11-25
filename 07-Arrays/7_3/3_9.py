ar=[9,7,8]  
arr= [9,7,0]    
def compare(arr1,arr2):
    for i in range(0,len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True
print(compare(ar,arr))
