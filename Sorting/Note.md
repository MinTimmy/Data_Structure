###### tags: 'Data_Structure'

# Sorting

## Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

```pseudocode
bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort
```
```python=
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
```
## Counting Sort

### How Counting Sort Works?
1. Find out the maximum element (let it be max) from the given array. 
![](https://i.imgur.com/INgyljf.png)

2. Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array. 
![](https://i.imgur.com/2INcRBX.png)

3. Store the count of each element at their respective index in count array

    For example: if the count of element 3 is 2 then, 2 is stored in the 3rd position of count array. If element "5" is not present in the array, then 0 is stored in 5th position. 
![](https://i.imgur.com/C36oREz.png)

4. Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array. 
![](https://i.imgur.com/bfuOcze.png)

5. Find the index of each element of the original array in the count array. This gives the cumulative count. Place the element at the index calculated as shown in figure below. 
![](https://i.imgur.com/LpdYFoN.png)

6. After placing each element at its correct position, decrease its count by one.

```pseudocode
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and 
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
```
```python=
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

```
## Selection Sort

### How Selection Sort Works?
1. Set the first element as minimum. 
![](https://i.imgur.com/hBQI5HG.png)
2. Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.

Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element. 

![](https://i.imgur.com/iPKRx0Y.png)
3. After each iteration, minimum is placed in the front of the unsorted list. 

![](https://i.imgur.com/YHKd6wk.png)
4. For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions. 

![](https://i.imgur.com/OJrXmVm.png)
![](https://i.imgur.com/ugOgnF4.png)
![](https://i.imgur.com/prUYnn7.png)
![](https://i.imgur.com/6KyrL29.png)

```pseudocode
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
```
```python=
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

```
## Shell Sort

### How Shell Sort Works?
1. Suppose, we need to sort the following array. 
![](https://i.imgur.com/ZBuLyxj.png)
2. We are using the shell's original sequence (N/2, N/4, ...1) as intervals in our algorithm.

    In the first loop, if the array size is N = 8 then, the elements lying at the interval of N/2 = 4 are compared and swapped if they are not in order.

    1. The 0th element is compared with the 4th element.
    2. If the 0th element is greater than the 4th one then, the 4th element is first stored in temp variable and the 0th element (ie. greater element) is stored in the 4th position and the element stored in temp is stored in the 0th position.
![](https://i.imgur.com/RebPZcc.png)
 This process goes on for all the remaining elements. 
![](https://i.imgur.com/huWheCT.png)
3. In the second loop, an interval of N/4 = 8/4 = 2 is taken and again the elements lying at these intervals are sorted. 
![](https://i.imgur.com/mc9dXFO.png)
 You might get confused at this point. 
![](https://i.imgur.com/Z860dhc.png)
The elements at 4th and 2nd position are compared. The elements at 2nd and 0th position are also compared. All the elements in the array lying at the current interval are compared.
4. The same process goes on for remaining elements. 
![](https://i.imgur.com/AEy3UgW.png)
5. Finally, when the interval is N/8 = 8/8 =1 then the array elements lying at the interval of 1 are sorted. The array is now completely sorted. 
![](https://i.imgur.com/gg8LOHD.png)
pseudocode
```pseudocode
shellSort(array, size)
  for interval i <- size/2n down to 1
    for each interval "i" in array
        sort all the elements at interval "i"
end shellSort
```
```python=
from random import *
SIZE = 10
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
    num.append(randint(1, 10))
shellSort(num, SIZE)
print('Sorted Array in Ascending Order:')
print(num)
```
## Straight Radix Sort

