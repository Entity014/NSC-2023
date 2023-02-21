f = open("NSC-2023/runs/detect/exp3/labels/1.txt", "r")
arr = []
for i, x in enumerate(f):
    arr.append([float(i) for i in x.split(' ')])

for i in range(len(arr)):
    for j in range(1, len(arr[i])):
        arr[i][j] = arr[i][j] * 100

pinP = []
objR = []
for i, x in enumerate(arr):
    if (x[0] == 4):
        pinP.append(x)
    else:
        objR.append(x)

for i in range(len(pinP)):
    