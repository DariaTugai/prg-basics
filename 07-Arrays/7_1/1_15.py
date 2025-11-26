car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]###
# Bubble sort
#
def bubble_sort(arr):

   for i in range(len(arr)):
      swapped = False
      for j in range(len(arr)-i-1):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped = True
      if swapped == False:
         break
   return arr
# def quickSort(arr):
#    left = []
#    right = []
#    pivot = len(arr)//2
#    if len(arr) <=1:
#       return arr
#    for x in range(len(arr)):
#       if x == pivot:
#          continue
#       if arr[pivot]>arr[x]:
#          right.append(arr[x])
#       else:
#          left.append(arr[x])
#    return quickSort(left)+[arr[pivot]]+quickSort(right)

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions) 
print(sorted_bank_transactions)