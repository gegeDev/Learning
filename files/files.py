plik = open("tekst.txt", "a") #"w" - writeable "r" - readable "a" - appendable
if plik.writable():
    plik.write(input("Wprowadź tekst: " + "\n"))# + "\n" - tworzy pustą linię pod napisem
plik.close()

plik = open("tekst.txt", "r")
if plik.readable():
    for x in plik: #read() - wypisuje treść pliku readlines() - wypisuje treść pliku jako listę
        print(x)
plik.close() #zaaaaaawsze pamiętaj
