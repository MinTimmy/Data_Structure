from random import *

def seletion_sort(nums):
   for i in range(len(nums)):
       min = i
       for j in range(i + 1, len(nums)):
           if nums[j] < nums[min]:
               min = j
       if min != i:
           nums[i] , nums[min] = nums[min] , nums[i]
num = []
for i in range(5):
    n = randint(1,100)
    num.insert(1,n)
seletion_sort(num)

print(num)
