def kravo(pocetKrav, t, pocetNaPrezitie, kravaList):
    if pocetKrav < pocetNaPrezitie: # keď je počet kráv menej ako počet kráv na prežitie
        return -1 # vráti -1
    vBezepeci = 0 # nastavíme premennú vBezepeci na 0
    prekazkyList = [] # vytvoríme prázdny zoznam pre prekážky(kravy ktore sa hybu prilis pomaly)
    canifPrekazkyNieList = [] # vytvoríme prázdny zoznam pre kravy ktore by sa dostali do bezpečia ak by nemali pred sebou prekazku
    for item in kravaList: # pre každú kravu v zozname kravaList

        if int(item[0])/int(item[1]) <= t: # ak je cas zo ktory sa krava dostane do bezpecia menšia alebo rovná ako t
            if len(prekazkyList) < 1: # ak nema pred sebou žiadnu prekážku
                vBezepeci += 1 # pridáme 1 do počtu kráv v bezpečí
            elif len(prekazkyList) >= 1: # ak má pred sebou prekážku
                canifPrekazkyNieList.append((len(prekazkyList), item)) # pridáme do zoznamu canifPrekazkyNieList tuple s poctom prekazok pred sebou a kravou
        else: # ak je cas zo ktory sa krava dostane do bezpecia väčšia ako t
            prekazkyList.append(item) # pridáme kravu do zoznamu prekazkyList
    x = pocetNaPrezitie - vBezepeci # vypočítame koľko kráv nám chýba do požadovaného počtu kráv v bezpečí


    res = 0 # nastavíme premennú res na 0
    if len (canifPrekazkyNieList) < x: # ak je počet kráv ktoré by sa dostali do bezpečia ak by nemali pred sebou prekazku mensi ako potrebny pocet
        return -1 # vrátime -1
    else: # ak je počet kráv ktoré by sa dostali do bezpečia ak by nemali pred sebou prekazku väčší ako potrebny pocet
        for z in range(x): # pre každú kravu ktorá by sa dostala do bezpečia ak by nemala pred sebou prekazku
            res += int(canifPrekazkyNieList[z][0]) # pridáme počet prekážok pred kravou do výsledku
    return res # vrátime výsledok


inp = input().split() # načítame vstup
n, t, p = int(inp[0]), int(inp[1]), int(inp[2]) # rozdelíme vstup na n, t, p

kravy = [] # vytvoríme prázdny zoznam pre kravy
for i in range(n): # pre každú kravu
    kravy.append(input().split()) # pridáme kravu do zoznamu kravy


print(kravo(n, t, p, kravy))    # vypíšeme výsledok funkcie kravo