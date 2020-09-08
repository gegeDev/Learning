krotka = (2, 4, 8, 16, 32, 64, 128)
print(krotka[0])
print(krotka)
#w tupli nie można zmieniać wartości przypisanych indeksów
print(len(krotka))

#WYCINKI
print(krotka[0])
print(krotka[0:3]) #wyświetlenie elementów z indeksami 0,1,2 (od 0 do 3 wyłącznie)
print(krotka[0:10000]) #nie zwróci błędu, poda wszystko zawiera się w wycinku
print(krotka[-4:-2]) #zwróci wycinek (wartości liczymy od tyłu nie od 0 tylko od 1)
print(krotka[0:7:2]) #początek, koniec i skok, czyli inkrement
print(krotka[0::2]) #od początku do końca co dwa
print(krotka[3:]) #od 3 do końca
print(krotka[:4]) #od początku do 3
