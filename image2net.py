import numpy as np
import pandas as pd
def toNetlist(mode:str):
    # x, y, width, height
    f = open("runs\detect\exp\labels\IMG_2067.txt", "r")
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
        # print(x)

    for i, a in enumerate(objR):
        for j, b in enumerate(objXY[indO]):
            if (b[0] in a) and (b[1] in a) and (a[0] == 5):
                a.append("R%s" % j)
            elif (b[0] in a) and (b[1] in a) and (a[0] == 0):
                a.append("C%s" % j)
            elif (b[0] in a) and (b[1] in a) and (a[0] == 1):
                a.append("C%s" % j)
            elif (b[0] in a) and (b[1] in a) and (a[0] == 2):
                a.append("D%s" % j)
            elif (b[0] in a) and (b[1] in a) and (a[0] == 3):
                a.append("D%s" % j)
            elif (b[0] in a) and (b[1] in a) and (a[0] == 6):
                a.append("R%s" % j)
        # print(a)

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
            if ((x[1] + (x[1] * 0.2)) > y[1]) and (x[1] < y[1]):
                node.append([x[5], y[5]])
                # print((x[1] - (x[1] * 0.1)), x[1], y[5], x[5])
                # print(y[1], y[5], x[5])
    print(node)

    tempNode = []
    # tempNodeX = []
    overNode = False
    for i in range(len(node)):
        tempNode.append(node[i][0])
    dfNode = pd.value_counts(np.array(tempNode))
    for i, x in enumerate(tempNode):
        if dfNode.loc[x] > 2:
            # tempNodeX.append(x)
            overNode = True
    # print(overNode)

    for i, x in enumerate(objR):
        for j, y in enumerate(pinP):
            for k, z in enumerate(node):
                if (z[0] in x and z[1] in y):
                    if (mode == "High"):
                        # print(x[1] - (x[4] * 0.65), x[1] + (x[3] * 1.4), x[2] + (x[4] * 2), x[2], x[5])
                        # print(y[1], y[2], y[1] + y[3], y[2] + y[4], y[0], y[5])
                        # if (x[1] - (x[4] * 0.65) < y[1] and x[1] + (x[3] * 1.4) > y[1]) and (x[2] < y[2] and x[2] + (x[4] * 2) > y[2]):
                        #     if (x[1] - (x[4] * 0.65) < y[1] + y[3] and x[1] + (x[3] * 1.4) > y[1] + y[3]) and (x[2] < y[2] + y[4] and x[2] + (x[4] * 2) > y[2] + y[4]):
                        #         # print(x[1] - (x[4] * 0.65), x[1] + (x[3] * 1.4), x[2] + (x[4] * 2), x[2], x[5])
                        #         # print(y[1], y[2], y[1] + y[3], y[2] + y[4], y[0], y[5])
                        #         if (y[1] > x[1]):
                        #             pinObjList.append([x[5], y[5] + "R"])
                        #         elif (y[1] < x[1]):
                        #             pinObjList.append([x[5], y[5] + "L"])
                        #         positionList.append([y[5], y[1]])
                        # print("--------------------")
                        if ((x[2] + x[4]) > y[2]) and (x[2] < y[2]):
                            if (y[1] > x[1]):
                                pinObjList.append([x[5], y[5] + "R"])
                                # for a, q in enumerate(node):
                                #     if (y[5] in q):
                                #         node.remove(q)
                                # print(x[5], y[5], "R")
                            elif (y[1] < x[1]):
                                pinObjList.append([x[5], y[5] + "L"])
                                # print(x[5], y[5], "L")
                            positionList.append([y[5], y[1]])
                    elif (mode == "Low"):
                        if (((x[1] - (x[3] ** 1.0) < y[1]) and (x[1] + (x[3] ** 1.2) > y[1])) and ((x[2] < y[2]) and (x[2] + (x[3]**1.4) > y[2]))):
                            if (((x[1] - (x[3] ** 1.0) < y[1] + y[3]) and (x[1] + (x[3] ** 1.2) > y[1] + y[3])) and ((x[2] < y[2] + y[4]) and (x[2] + (x[3]**1.4) > y[2] + y[4]))):
                                if (x[2] + (x[4] ** 1.12) < y[2] and x[2] + (x[4] ** 1.12) < y[2] + y[4]) and overNode:
                                    # print(x[1] - (x[3] ** 1.0), x[1] + (x[3] ** 1.1), x[2], x[2] + (x[3]**1.4), x[5])
                                    # print(y[1] , y[2], y[1] + y[3], y[2] + y[4], y[5])
                                    # print(x[1], x[1] + (x[3] ** 1.1), x[2], x[2] + (x[4] ** 1.3), x[5])
                                    if (y[1] > x[1]):
                                        pinObjList.append([x[5], y[5] + "R"])
                                        # print(x[5], y[5], "R")
                                    elif (y[1] < x[1]):
                                        pinObjList.append([x[5], y[5] + "L"])
                                        # print(x[5], y[5], "L")
                                    positionList.append([y[5], y[1]])
                                elif not overNode:
                                    if (y[1] > x[1]):
                                        pinObjList.append([x[5], y[5] + "R"])
                                        # print(x[5], y[5], "R")
                                    elif (y[1] < x[1]):
                                        pinObjList.append([x[5], y[5] + "L"])
                                        # print(x[5], y[5], "L")
                                    positionList.append([y[5], y[1]])
                        # print("-----------------------------")
    # print(pinObjList)

    countX = []
    tempCountX = []
    notFound = False
    for i in range(len(pinObjList)):
        countX.append(pinObjList[i][0])
    df = pd.value_counts(np.array(countX))
    for i, x in enumerate(countX):
        if df.loc[x] == 1:
            tempCountX.append(x)
    # if (df.values[0]) != 2 or (df.values[1] != 2) or (df.values[2] != 2):
    #     notFound = True
        # print(df.values, notFound)

    connectPin = []
    notConnectPin = False
    for i, x in enumerate(positionList):
        for j, y in enumerate(positionList):
            if (x[1] - x[1] * 0.03 < y[1]) and (x[1] + x[1] * 0.03 > y[1]) and (x != y):
                if ([x[0], y[0]] not in connectPin):
                    connectPin.append([x[0], y[0]])
                    # print(x[0], y[0], x[1] - x[1] * 0.03, x[1] + x[1] * 0.03, y[1])
    # print(positionList)

    if (len(connectPin) == 0):
        notConnectPin = True

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
                # if (int(y[0][1:]) > len(connectPin)) and ([x[0], int(y[0][1:])] not in connectPinX):
                if (int(y[0][1:]) > len(connectPin)) and ([x[0], y[0]] not in connectPinX):
                    # connectPinX.append([x[0], int(y[0][1:]) - 1])#y[0]])
                    # connectPinX.append([x[0], y[0][0] + str(int(y[0][1:]) - 1) + x[1][-1]])
                    pinObjList[i] = [x[0], y[0][0] + str(int(y[0][1:]) - 1) + x[1][-1]]
                else:
                    if ([x[0], y[0]] not in connectPinX):
                        # connectPinX.append([x[0], y[0] + x[1][-1]])#y[0]])
                        pinObjList[i] = [x[0], y[0] + x[1][-1]]
            # Not Found Pin
            # else:
            #     # print(x, 1)
            #     # if ([x[0], int(x[1][1:])] not in connectPinX):
            #     if ([x[0], x[1]] not in connectPinX) and (notFound):
            #         # connectPinX.append([x[0], x[1]])#x[1]])
            #         pinObjList[i] = [x[0], x[1]]
    # print(pinObjList)

    netlist = []
    tempArr = []
    maxPin = max(pinObjList)[1][1]
    if (not notConnectPin):
        for i, x in enumerate(pinObjList):
            for j, y in enumerate(pinObjList):
                for k, z in enumerate(df.values):
                    if (x[0] in y) and (x != y) and z == 2:
                        # print(x, y)
                        dummy = [x[0]]
                        if ("L" in x[1][2]):
                            # dummy.insert(3, x[1])
                            dummy.insert(2, int(x[1][1]))
                        elif ("L" in y[1][2]):
                            # dummy.insert(3, y[1])
                            dummy.insert(2, int(y[1][1]))
                        if ("R" in x[1][2]):
                            # dummy.insert(4, x[1])
                            dummy.insert(3, int(x[1][1]))
                        elif ("R" in y[1][2]):
                            # dummy.insert(4, x[1])
                            dummy.insert(3, int(y[1][1]))
                        if ([dummy[0], dummy[1], dummy[2]] not in tempArr):
                            tempArr.append(dummy)
                    for a, b in enumerate(tempCountX):
                        if (x[0] not in y and x != y) and z != 2 and x[0] in b:
                            dummy = [x[0]]
                            if ("L" in x[1][2]):
                                # dummy.insert(3, x[1])
                                dummy.insert(2, int(x[1][1]))
                                dummy.insert(3, int(maxPin) + a + 1)
                            elif ("R" in x[1][2]):
                                # dummy.insert(4, x[1])
                                dummy.insert(2, int(maxPin) + a + 1)
                                dummy.insert(3, int(x[1][1]))
                            # print(dummy)
                            if ([dummy[0], dummy[1], dummy[2]] not in tempArr):
                                tempArr.append(dummy)

        for i, x in enumerate(tempArr):
            netlist.append([i + 1, x[0], x[1], x[2]])

    nPin = []
    if (notConnectPin):
        for i, x in enumerate(pinObjList):
            for j, y in enumerate(pinObjList):
                dummy = [x[0]]
                if (x[0] == y[0] and x != y):
                    if ("L" in x[1][2]):
                        dummy.insert(2, int(x[1][1]))
                    elif ("L" in y[1][2]):
                        dummy.insert(2, int(y[1][1]))
                    if ("R" in x[1][2]):
                        dummy.insert(3, int(x[1][1]))
                    elif ("R" in y[1][2]):
                        dummy.insert(3, int(y[1][1]))
                if (len(dummy) == 3):
                    # print([dummy[0], dummy[1], dummy[2]])
                    if ([dummy[0], dummy[1], dummy[2]] not in nPin):
                        nPin.append(dummy)
        dummyE = []
        for i, x in enumerate(nPin):
            for j, y in enumerate(pinObjList):
                if x[0] in y:
                    dummyE.append(y)
        
        for i, x in enumerate(dummyE):
            pinObjList.remove(x)
        
        tempInt = 0
        for i, x in enumerate(pinObjList):
            dummy = [i + 1, x[0]]
            if ("L" in x[1][2]):
                dummy.insert(3, int(x[1][1]))
                dummy.insert(4, int(maxPin) + i + 1)
            if ("R" in x[1][2]):
                dummy.insert(3, int(maxPin) + i + 1)
                dummy.insert(4, int(x[1][1]))
            netlist.append(dummy)
            tempInt = i
            
        for i, x in enumerate(nPin):
            x.insert(0, tempInt + i + 2)
            netlist.insert(tempInt + i + 1, x)
    
    print("connectPin :", connectPin)
    # print("connectPinX :",connectPinX)
    # print(netlist)
    # print(positionList)
    # print(notConnectPin)
    print("pinObjList :",pinObjList)
    return netlist

print(toNetlist("High"))
