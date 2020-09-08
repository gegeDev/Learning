lista = list(range(10)) #tak się to robi z range

nowa = [i * 2 for i in lista] #mnożenie wszystkich elementów listy razy dwa i stworzenie nowej listy
print(lista)
print(nowa)
nowa2 = [i + 2 for i in lista if i % 2 == 0] #do pętli w deklaracji można dopisać instrukcje warunkowe, elementy które nie spełniają instrukcji warunkowej nie zostaną wpisane do listy
lista = [i for i in range(10, 21, 2)] #tak też można, to wszystkie liczby parzyste od 10 do 20
print(lista)
print(nowa2)

#FORMATOWANIE STRINGÓW

argumenty = ["Grześ", 19]
tekst = "cześć jestem {0} i mam {1} lat.".format(argumenty[0], argumenty[1]) # argumentami funkcji format są kolejno 0 i 1 wpisane w tekst stringa
print(tekst)
