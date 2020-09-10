liczby = [2, 10, 40, 20, 23, 4221, 21, 323]

def funkcja(x): #deklarowanie funkcji do map()
    return x * 2

wynik = map(funkcja, liczby) #funkcja map wykonuję funkcję na każdej liczbie z listy
print(list(wynik))

wynik2 = map(lambda x: x + 2, liczby) #to samo ale z funkcją anonimową
print(list(wynik2))

wynik3 = filter(lambda x: x % 2 == 0, liczby) #filtruje i zostawia tylko elementy spełniające warunek
print(list(wynik3))
