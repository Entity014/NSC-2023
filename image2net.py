import numpy as np
f = open("1.txt", "r")
arr = []
for i, x in enumerate(f):
    arr.append([float(i) for i in x.split(' ')])

for i in range(len(arr)):
    for j in range(1, len(arr[i])):
        arr[i][j] = arr[i][j] * 100

pinP = [] # index 5 is order
objR = []
pinXY = []
objXY = []
for x in arr:
    if (x[0] == 4):
        pinP.append(x)
        pinXY.append([x[1], x[2]])
    else:
        objR.append(x)
        objXY.append([x[1], x[2]])
    
pinXY = np.array(pinXY)
objXY = np.array(objXY)
indP = np.lexsort((pinXY[:,1],pinXY[:,0]))   
indO = np.lexsort((objXY[:,1],objXY[:,0]))

for i, x in enumerate(pinP):
    for j, y in enumerate(pinXY[indP]):
        if (y[0] in x) and (y[1] in x):
            x.append(j)
    # print(x)

for i, a in enumerate(objR):
    for j, b in enumerate(objXY[indO]):
        if (b[0] in a) and (b[1] in a):
            a.append(j)
    # print(a)
# print(pinP[4])
# print(pinP[2])
# print(objR[1])

# 1 > 2, 3
# 0 > 0, 1
# 2 > 4
# * 10%
node = []
dummy = []
for i, x in enumerate(objR):
    for j, y in enumerate(pinP):
        if ((x[2] - (x[2] * 0.1)) < y[2]) and (x[2] > y[2]):
            node.append([x[5], y[5]])
            # print(y[2], y[5], x[5])
        if ((x[2] + (x[2] * 0.1)) > y[2]) and (x[2] < y[2]):
            node.append([x[5], y[5]])
            # print(y[2], y[5], x[5])
    print(node)