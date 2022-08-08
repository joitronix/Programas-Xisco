import os
paths = []
for root, dirs, files in os.walk("c:\\"):
    for file in files:
        if ".ib" in file or ".IB" in file:
            paths.append(os.path.join(root, file))
for a in paths:
    print(a)
