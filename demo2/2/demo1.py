i1 = "A"
i2 = "A B 7,B C 10"

items = ""

items += i1

first = True
temp = []
n = ""
i2 += ','
for i in i2:
    if ord(i) >= 65 and ord(i) <= 90:
        same = False
        for j in range(len(items)):
            if i == items[j]:
                same = True
        if not same:
            items += i
        for j in range(len(items)):
            if first:
                if i == items[j]:
                    temp.append([j,-1,-1])
                    first = False
                    break
            else:
                if i == items[j]:
                    temp[len(temp)-1][1] = j
                    first = True
                    break
    if ord(i) >= 48 and ord(i) <= 57:
        n += i
    elif i == ',':
        temp[len(temp)-1][2] = int(n)
        n = ""   

print(temp)
print(items)

    

    