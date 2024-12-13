def kravo(pocetKrav, t, pocetNaPrezitie, kravaList):
    if pocetKrav < pocetNaPrezitie:
        return -1
    vBezepeci = 0
    prekazkyList = []
    canifPrekazkyNieList = []
    for item in kravaList:
        print(int(item[0])/int(item[1]))
        if int(item[0])/int(item[1]) <= t and len(prekazkyList) < 1:
            vBezepeci += 1
        elif int(item[0])/int(item[1]) <= t and len(prekazkyList) >= 1:
            canifPrekazkyNieList.append((len(prekazkyList), item))
        else:
            prekazkyList.append(item)
    x = pocetNaPrezitie - vBezepeci
    print("canifPrekazkyNieList", canifPrekazkyNieList)
    print("prekazkyList", prekazkyList)
    canifPrekazkyNieList = [item for item in canifPrekazkyNieList if item not in prekazkyList]
    print("canifPrekazkyNieList", canifPrekazkyNieList)
    res = 0
    if len (canifPrekazkyNieList) < x:
        return -1
    else:
        for z in range(x):
            res += int(canifPrekazkyNieList[z][0])
    return res


inp = input().split()
n, t, p = int(inp[0]), int(inp[1]), int(inp[2])
print(n, t, p)
kravy = []
for i in range(n):
    kravy.append(input().split())
print(kravy)

print(kravo(n, t, p, kravy))