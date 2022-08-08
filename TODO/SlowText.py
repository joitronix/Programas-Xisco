import os
with open('1.txt') as f:
    lines = f.readlines()
for a in lines:
    print(a)
os.system("pause")