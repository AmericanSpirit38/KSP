def kravo(pocetKrav, t, pocetNaPrezitie, kravaList):
    if pocetKrav < pocetNaPrezitie:
        return -1
    vBezepeci = 0
    prekazkyList = []
    canifPrekazkyNieList = []
    for item in kravaList:

        if int(item[0])/int(item[1]) <= t:
            if len(prekazkyList) < 1:
                vBezepeci += 1
            elif len(prekazkyList) >= 1:
                canifPrekazkyNieList.append((len(prekazkyList), item))
        else:
            prekazkyList.append(item)
    x = pocetNaPrezitie - vBezepeci


    res = 0
    if len (canifPrekazkyNieList) < x:
        return -1
    else:
        for z in range(x):
            res += int(canifPrekazkyNieList[z][0])
    return res


inp = input().split()
n, t, p = int(inp[0]), int(inp[1]), int(inp[2])

kravy = []
for i in range(n):
    kravy.append(input().split())


print(kravo(n, t, p, kravy))