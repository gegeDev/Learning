slownik = {1: "Poniedziałek", 2: "Wtorek", 3: "Środa"}
print(slownik[1]) #wypisuje wartość przy kluczu 1
slownik[4] = "Czwartek" #dodaje zapis 4: "czwartek", jeśli podany klucz istnieje to zamienia jego wartość
print(slownik) #wypisuje wszystkie wartości wraz z kluczami
slownik[5] = False
slownik["a"] = 3 #wartości i klucze słownika mogą mieć różne typy
print(slownik.get(8, "dupa")) #wypisze wartość przy kluczu 8 jeśli istnieje a jeśli nie istnieje to wypisze dupa

for i in slownik: #iteruje po kluczach
    print(i)
    print(slownik[i])

for x in slownik.values(): #iteruje po wartościach
    print(x)
