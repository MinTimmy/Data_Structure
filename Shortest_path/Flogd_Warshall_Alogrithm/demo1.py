N = 5
INF = 10000
items = "ABCDEFG"
a = [
    [0,1,INF,INF,4],
    [1,0,5,1,INF],
    [INF, 5,0,2,INF],
    [INF, 1,2,0,1],
    [4,INF,INF,1,0]
]
p = [
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4]
]

def show():
    for i in range(N):
        for j in range(N):
            if a[i][j] == INF:
                print("I", end = '')
            else:
                print(a[i][j], end = '')
            print(items[p[i][j]], end = ' ')
        print("")
    print("\n---------------------------------------------------\n")
for j in range(N):
    for i in range(N):
        for k in range(N):
            if (i != j) and (j != k):
                if a[i][k] > a[i][j] + a[j][k]:
                    a[i][k] = a[i][j] + a[j][k]
                    p[i][k] = p[i][j]
    show()
for i in range(N):
    for j in range(N):
        if i != j:
            temp = i
            print(items[i] + "->", end = '')
            while p[temp][j] != j:
                print(items[p[temp][j]] + "->", end = '')
                temp = p[temp][j]
            print(items[p[temp][j]] + " = " + str(a[i][j]))
    