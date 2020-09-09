print("".join(["a", "b", "c"]))
print("Hello World!".replace("Hello", "Witaj")) #zamienia pierwszy podany w metodzie string na drugi
print("To jest zdanie".startswith("To")) #sprawdza czy string zaczyna się od podanego stringa zwraca bool
print("To jest zdanie".endswith(".")) #analogicznie do startswith
print("ja" in "Dupa biskupa") #sprawdza czy pierwszy string zawiera się w drugim
print("Jebać pis".upper()) #zmienia wszystkie litery na wielkie
print("Jebać pis".lower()) #zmienia wszystkie litery na małe

lista = [12, 24, 36, 48, 60]
if all([i % 2 == 0 for i in lista]): print("wszystko parzyste") #for sprawdza czy wszystkie elementy listy spełniają podany na początku warunek
print(all([i % 2 == 0 for i in lista]))

if any([i % 9 == 0 for i in lista]): print("Są tu liczby podzielne przez 9")

for i in enumerate(lista): print(i) #wypisuje tablicę jako tuplę z indeksami i elementami listy
