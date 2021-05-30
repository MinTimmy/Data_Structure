
num = [[1,0,1,0,1], [1,1,1,0,0],[1,1,0,0,0],[0,1,0,1,0],[0,0,1,1,1],[1,1,1,1,0]]

# the variable bit is the index of sublist. num[0] = [1,0,1,0,1], bit = 0, num[0][bit] = 0
def bits(n, bit, i):
    return n[bit]

def radix_exchange(left, right, bit):
    if left < right and bit < 5:
        i = left # the first one is num[0] = [1,0,1,0,1]
        j = right # the first one is num[5] = [1,1,1,1,0]
        while i != j:
            while (bits(num[i], bit, 1) == 0) and i < j: 
                i+=1
            while (bits(num[j], bit, 1) == 1) and i < j: 
                j-=1
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        if bits(num[right], bit, 1) == 0:
            j += 1
        radix_exchange(left, j-1, bit+1)
        radix_exchange(j, right, bit+1)
        
radix_exchange(0, 5, 0)

print(num)
# print(num[0][0])