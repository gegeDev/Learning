liczby1 = {0, 1, 2, 3, 4} #deklaracja jak przy słownikach ale bez kluczy
slowa = set(["a", "b", "c"]) #tak się robi zbiór stringów

print(slowa)

liczby1.add(5) #inne metody niż w przypadku list

print(liczby1)

liczby1.pop() #usuwa pierwszy element zbioru (tak samo przy listach itd.)
print(liczby1)
liczby1.add(5) #nic się nie staje, elementy nie mogą się powtarzać
print(liczby1)
print(1 in liczby1) #podobne do any() 
print(i % 2 == 0 for i in liczby1) #próba, zwraca generator, trzeba dać any()

liczby2 = {4, 5, 6, 7, 8, 9}

print(liczby1 | liczby2) #zwraca sumę zbiorów jak w matematyce wartości nadal się nie powtarzają
print(liczby1 & liczby2) #zwraca iloczyn zbiorów
print(liczby1 - liczby2) #zwraca różnicę zbiorów
print(liczby1 ^ liczby2) #różnica symetryczna (suma \ iloczyn zbiorów)
