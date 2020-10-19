from random import *
def bubble_sort(num):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                swapped = True

num = []
for i in range(5):
    n = randint(1,100)
    num.insert(1,n)
bubble_sort(num)

print(num)

