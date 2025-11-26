arr=[4,36,12,28,9,44,5]
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
print(bubblesort(arr))

