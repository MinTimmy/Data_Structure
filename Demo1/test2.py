n = [[0  for i in range(10)] for j in range(3)]
m = [1  for i in range(10)]
#n[1][0] = 1
for i in range(10):
    n[1][i] = m[i]

print(n[0])