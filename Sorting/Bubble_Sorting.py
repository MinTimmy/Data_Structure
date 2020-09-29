from random import *
def bubble_sort(nums):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

num = []
for i in range(5):
    n = randint(1,100)
    num.insert(1,n)
bubble_sort(num)

print(num)

