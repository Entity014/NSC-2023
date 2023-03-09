import numpy as np
import pandas as pd
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

    for i, x in enumerate(objR):
        for j, y in enumerate(pinP):
            for k, z in enumerate(node):
                if (z[0] in x and z[1] in y):
                    if ((x[2] + x[4]) > y[2]) and (x[2] < y[2] and mode == "High"):
                        if (y[1] > x[1]):
                            pinObjList.append([x[5], y[5] + "R"])
                            # print(x[5], y[5], "R")
                        elif (y[1] < x[1]):
                            pinObjList.append([x[5], y[5] + "L"])
                            # print(x[5], y[5], "L")
                        positionList.append([y[5], y[1]])
                    if ((x[2] + (x[4] * 2.5) > y[2]) and (x[2] + x[4] < y[2])and mode == "Low"):
                        # print(y[5], (x[2] + (x[4] * 2)), (x[2] + x[4]), y[2])
                        if (y[1] > x[1]):
                            pinObjList.append([x[5], y[5] + "R"])
                            # print(x[5], y[5], "R")
                        elif (y[1] < x[1]):
                            pinObjList.append([x[5], y[5] + "L"])
                            # print(x[5], y[5], "L")
                        positionList.append([y[5], y[1]])
                    # print(y[5], (x[2] + x[4]), (x[2]), y[2])

    countX = []
    notFound = False
    for i in range(len(pinObjList)):
        countX.append(pinObjList[i][0])
    df = pd.value_counts(np.array(countX))
    # print(df.values)
    if (df.values).all is not 2:
        notFound = True
        # print(df.values, notFound)

    connectPin = []
    for i, x in enumerate(positionList):
        for j, y in enumerate(positionList):
            if (x[1] - x[1] * 0.03 < y[1]) and (x[1] + x[1] * 0.03 > y[1]) and (x != y):
                if ([x[0], y[0]] not in connectPin):
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
            if (y[0] + "L" in x) or (y[0] + "R" in x) or (y[1] + "L" in x) or (y[1] + "R" in x):
                # print(x, y, i, j, len(connectPin))
                # print(x, y)
                # if (int(y[0][1:]) > len(connectPin)) and ([x[0], int(y[0][1:])] not in connectPinX):
                if (int(y[0][1:]) > len(connectPin)) and ([x[0], y[0]] not in connectPinX):
                    # connectPinX.append([x[0], int(y[0][1:]) - 1])#y[0]])
                    connectPinX.append([x[0], y[0][0] + str(int(y[0][1:]) - 1) + x[1][-1]])
                else:
                    # if ([x[0], int(y[0][1:])] not in connectPinX):
                    if ([x[0], y[0]] not in connectPinX):
                        connectPinX.append([x[0], y[0] + x[1][-1]])#y[0]])
            # Not Found Pin
            else:
                # print(x, 1)
                # if ([x[0], int(x[1][1:])] not in connectPinX):
                if ([x[0], x[1]] not in connectPinX) and (notFound):
                    connectPinX.append([x[0], x[1]])#x[1]])
    # print(connectPinX)

    netlist = []
    maxPin = max(pinObjList)[1][1:2]
    # print(maxPin)
    for i, x in enumerate(connectPinX):
        for j, y in enumerate(connectPinX):
            if (x[0] in y) and (x != y):
                # print(x, y)
                dummy = [i + 1, x[0]]
                if ("L" in x[1][2:]):
                    # dummy.insert(3, x[1])
                    dummy.insert(3, int(x[1][1:2]))
                elif ("L" in y[1][2:]):
                    # dummy.insert(3, y[1])
                    dummy.insert(3, int(y[1][1:2]))
                if ("R" in x[1][2:]):
                    # dummy.insert(4, x[1])
                    dummy.insert(4, int(x[1][1:2]))
                elif ("R" in y[1][2:]):
                    # dummy.insert(4, x[1])
                    dummy.insert(4, int(y[1][1:2]))
                # print(dummy)
                netlist.append(dummy)
                connectPinX.remove(x)
                connectPinX.remove(y)
    
    # Not Found Pin
    if (notFound):
        for i, x in enumerate(connectPinX):
            for j, y in enumerate(connectPinX):
                if (x[0] in y):
                    dummy = [i + 1, x[0]]
                    if ([i + 1, x[0], x[1], y[1]] not in netlist):
                        if ("L" in x[1][2:]):
                            # dummy.insert(3, x[1])
                            dummy.insert(3, int(x[1][1:2]))
                            dummy.insert(4, int(maxPin) + i + 1)
                        elif ("L" in y[1][2:]):
                            # dummy.insert(3, y[1])
                            dummy.insert(3, int(y[1][1:2]))
                            dummy.insert(4, int(maxPin) + i + 1)
                        if ("R" in x[1][2:]):
                            # dummy.insert(4, x[1])
                            dummy.insert(3, int(maxPin) + i + 1)
                            dummy.insert(4, int(x[1][1:2]))
                        elif ("R" in y[1][2:]):
                            # dummy.insert(4, x[1])
                            dummy.insert(3, int(maxPin) + i + 1)
                            dummy.insert(4, int(y[1][1:2]))
                        # print(dummy)
                        netlist.append(dummy)
                    # print(x, y)

    # netlist = [[1, "R1", 1, 2], [2, "R2", 1, 3], [3, "R3", 3, 4], [4, "C4", 5, 4], [5, "C5", 6, 5], [6, "D6", 2, 6]]
    
    print("connectPin :", connectPin)
    print("connectPinX :",connectPinX)
    # print(netlist)
    # print(positionList)
    print("pinObjList :",pinObjList)
    return netlist

print(toNetlist())
