a = 'QBCDEHFG'
b = []
for i in a:
    b.append(i)
# a.sort()
# print(sorted(a[1:]))
b = [b[0]] + sorted(b[1:])
print(b)