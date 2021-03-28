import os

#print(os.getcwd()) #輸出目前的工作路径

#fp = open("//home//timmy//myCode//Data_Structure//Demo1//card.txt", "r")
fp = open("access_test.log", "r")
lines = fp.readlines()

count = 0
num = []
tmp = []
for l in lines:
    for i in range(len(l)):
        if count == 2:
            i += 1
            for j in range(3):
                tmp.append(int(l[i+j]))
            num.append(100 * tmp[0] + 10 * tmp[1] + tmp[2])
            count = 0
            tmp.clear()
            break
        if l[i] == '"':
            count += 1

print(num)
"""
while line:
    #print(line)
    line = fp.readline()
""" 
fp.close()
