from random import *

def Selection_sort(numbers):
   for i in range(len(numbers)):
       min = i
       for j in range(i + 1, len(numbers)):
           if numbers[j] < numbers[min]:
               min = j
       if min != i:
           numbers[i] , numbers[min] = numbers[min] , numbers[i]
num = []
for i in range(5):
    n = randint(1,100)
    num.insert(1,n)
Selection_sort(num)

print(num)
