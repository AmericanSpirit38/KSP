import math
stxt = input("text: ")
def cezaroveCisla(txt):
    if len(txt) % 2 != 0:
        return txt[::-1], txt[math.ceil(len(txt)/2):] + list(txt)[math.ceil(len(txt)//2)] + txt[:(len(txt)//2)]
    return txt[::-1], txt[math.ceil(len(txt)/2):] + txt[:(len(txt)//2)]
print(cezaroveCisla(stxt))