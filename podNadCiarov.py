stxt = input("text: ")
def podNad(txt, idx):
    nad = 1
    val = idx
    str1 = ""
    ciarky = ""
    str2 = ""
    for ch in txt:
        if nad == idx:
            str1 += ch
            str2 += " "
            idx += val
        else:
            str2 += ch
            str1 += " "
        ciarky += "-"
        nad += 1
    print(str1)
    print(ciarky)
    print(str2)
podNad(stxt, int(input("Enter index: ")))


