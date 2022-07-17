hola = []
for a in range(4):
    hola.append([])
    for b in range(4):
        hola[a].append([])
        for c in range(4):
            hola[a][b].append(["a"])

for a in hola:
    print(a)