from random import *
SIZE = 19
def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
num = []
for i in range(SIZE):
    num.append(randint(1, 1000))
shellSort(num, SIZE)
print('Sorted Array in Ascending Order:')
print(num)