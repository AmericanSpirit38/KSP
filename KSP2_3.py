def kravo(pocetKrav, t, pocetNaPrezitie, kravaList):
    if pocetKrav < pocetNaPrezitie:
        return -1
    vBezepeci = 0
    prekazkyList = []
    canifPrekazkyNieList = []
    for item in kravaList:
        if int(item[0])/int(item[1]) <= t and prekazkyList.count(item) < 1:
            vBezepeci += 1
        elif int(item[0])/int(item[1]) <= t:

        else:
            prekazkyList.append(item)





inp = input().split()
n, t, p = int(inp[0]), int(inp[1]), int(inp[2])
print(n, t, p)
kravy = []
for i in range(n):
    kravy.append(input().split())
print(kravy)

print(kravo(n, t, p, kravy))