import os
for i in range(0, 51):
    os.system(f"python detect.py --weights nsc3.pt --conf 0.2 --img-size 640 --source circuit/New/IMG_{2632 + i}.jpeg --view-img --no-trace --save-txt")