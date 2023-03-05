import numpy as np
def toNetlist():
    mode = "High"
    # mode = "Low"
    f = open("1.txt", "r")
    arr = []
    for i, x in enumerate(f):
        arr.append([float(i) for i in x.split(' ')])

    for i in range(len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] = arr[i][j] * 100

    pinP = []  # index 5 is order
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
    indP = np.lexsort((pinXY[:, 1], pinXY[:, 0]))
    indO = np.lexsort((objXY[:, 1], objXY[:, 0]))

    for i, x in enumerate(pinP):
        for j, y in enumerate(pinXY[indP]):
            if (y[0] in x) and (y[1] in x) and (x[0] == 4):
                x.append("P%s" % j)
        print(x)

    for i, a in enumerate(objR):
        for j, b in enumerate(objXY[indO]):
            if (b[0] in a) and (b[1] in a) and (a[0] == 5):
                a.append("R%s" % j)
        print(a)

    # 1 > 2, 3
    # 0 > 0, 1
    # 2 > 4
    # * 10%
    node = []  # [R ตัวไหน, คาดว่ามี Pin ไหน]
    pinObjList = []
    positionList = []
    connectPinX = []
    for i, x in enumerate(objR):
        for j, y in enumerate(pinP):
            if ((x[1] - (x[1] * 0.1)) < y[1]) and (x[1] > y[1]):
                node.append([x[5], y[5]])
                # print((x[1] - (x[1] * 0.1)), x[1], y[5], x[5])
                # print(y[1], y[5], x[5])
            if ((x[1] + (x[1] * 0.1)) > y[1]) and (x[1] < y[1]):
                node.append([x[5], y[5]])
                # print((x[1] - (x[1] * 0.1)), x[1], y[5], x[5])
                # print(y[1], y[5], x[5])
    # print(node)
    #มุมสูงเท่านั้น
    for i, x in enumerate(objR):
        for j, y in enumerate(pinP):
            for k, z in enumerate(node):
                if (z[0] in x and z[1] in y):
                    if ((x[2] + x[4]) > y[2]) and (x[2] < y[2] and mode == "High"):
                        pinObjList.append([x[5], y[5]])
                        positionList.append([y[5], y[1]])
                    if ((x[2] + (x[4] * 2.5) > y[2]) and (x[2] + x[4] < y[2])and mode == "Low"):
                        # print(y[5], (x[2] + (x[4] * 2)), (x[2] + x[4]), y[2])
                        pinObjList.append([x[5], y[5]])
                        positionList.append([y[5], y[1]])
                    # print(y[5], (x[2] + (x[4] * 2)), (x[2] + x[4]), y[2])

    connectPin = []
    for i, x in enumerate(positionList):
        for j, y in enumerate(positionList):
            if (x[1] - x[1] * 0.03 < y[1]) and (x[1] + x[1] * 0.03 > y[1]) and (x != y):
                connectPin.append([x[0], y[0]])
                # print(x[0], y[0])
                # print(x[0], y[0], x[1] - x[1] * 0.03, x[1] + x[1] * 0.03, y[1])

    # เคลียร์ตัวที่ซ้ำ
    for i, x in enumerate(connectPin):
        for j, y in enumerate(connectPin):
            if x[0] in y and x[1] in y and x != y:
                # connectPin.pop(i)
                # print(connectPin)
                connectPin.remove(y)
                # print(x, y)

    for i, x in enumerate(pinObjList):
        for j, y in enumerate(connectPin):
            if (y[0] in x) or (y[1] in x):
                # print(x, y, i, j, len(connectPin))
                if (int(y[0][1:]) > len(connectPin)) and ([x[0], int(y[0][1:])] not in connectPinX):
                    connectPinX.append([x[0], int(y[0][1:]) - 1])#y[0]])
                else:
                    if ([x[0], int(y[0][1:])] not in connectPinX):
                        connectPinX.append([x[0], int(y[0][1:])])#y[0]])
            # Not Found Pin
            else:
                # print(x, 1)
                if ([x[0], int(x[1][1:])] not in connectPinX):
                    connectPinX.append([x[0], int(x[1][1:])])#x[1]])

    netlist = []
    for i, x in enumerate(connectPinX):
        for j, y in enumerate(connectPinX):
            if (x[0] in y) and (x != y):
                print(x, y)
                netlist.append([i + 1, x[0], x[1], y[1]])
                connectPinX.remove(x)
                connectPinX.remove(y)
    
    # Not Found Pin
    for i, x in enumerate(connectPinX):
        for j, y in enumerate(connectPinX):
            if (x[0] in y):
                if ([i + 1, x[0], x[1], y[1]] not in netlist):
                    netlist.append([i + 1, x[0], x[1], 999])
                # print(x, y)

    # netlist = [[1, "R1", 1, 2], [2, "R2", 1, 3], [3, "R3", 3, 4], [4, "C4", 5, 4], [5, "C5", 6, 5], [6, "D6", 2, 6]]
    ready = True
    for i, x in enumerate(netlist):
        if 999 in x:
            ready = False
    
    print("connectPin :", connectPin)
    print("connectPinX :",connectPinX)
    # print(netlist)
    # print(positionList)
    # print("pinObjList :",pinObjList)
    return ready, netlist

print(toNetlist())
