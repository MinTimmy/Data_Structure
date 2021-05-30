import random

MAX = 100
TOTAL_NUMBER = 10
def Counting_Sort(array):

    output = [0 for i in range(len(array))]
    count = [ 0 for i in range(MAX)]

    for i in range(TOTAL_NUMBER):
        count[array[i]] += 1
               
    for i in range(MAX):
        count[i] += count[i-1]

    for i in range(TOTAL_NUMBER):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    for i in output:
        print(i, end = ' ')
arr = []
for i in range(TOTAL_NUMBER):
    n = random.randint(0,100)
    arr.append(n)

Counting_Sort(arr)
