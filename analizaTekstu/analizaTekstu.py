plik = open("lorem.txt", "r")
tekst = plik.read()
plik.close()

def policz(txt, znak): return sum(1 for i in txt if i == znak) #liczy ile razy wystąpiła literka l

def policzProsciej(txt, znak): #prostsza wersja funkcji policz
    licznik = 0
    for i in txt:
        if i == znak:
            licznik += 1
    return licznik

def literki(txt): #Zrobione w jednej linijce niżej, tu łatwiejsza wersja
    for i in "abcdefghijklmnoprstuwxyz":
        licznik = 0
        for l in txt:
            if l == i: licznik += 1
        procent = licznik * 100 / len(txt)
        print("{0} - {1} - {2}%".format(i, licznik, round(procent, 2))) #drugi argument w funkcji round mówi ile miejsc po przecinku w zaokrągleniu

print(policz(tekst, "L"))
print(policz(tekst.lower(), "l")) #liczy małe l
print(policzProsciej(tekst, "l"))

#for z in "abcdefghijklmnopestuwxyz": print(z + " " + str(sum(1 for i in tekst if i == z))) #można to zrobić używając funkcji policz albo policzProsciej
literki(tekst)
