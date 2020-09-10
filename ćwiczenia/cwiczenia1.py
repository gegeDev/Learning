from random import randint

print("1. Zgadywanka")
print("2. Tabela wyników")
a = input("Wybierz opcję: ")

def wybor(x):
    assert x == "1" or x == "2"
    if x == "1": zgadywanka()
    if x == "2": tabela()

def zgadywanka():
    num = randint(1, 1000)
    p = 0
    g = 1001
    while(g != num):
        g = int(input("Zgadnij liczbę: "))
        p += 1
        if(g > num): print("Za dużo")
        elif(g < num): print("Za mało")
    print("Zgadłeś! Liczba to: " + str(num) + " potrzebowałeś " + str(p) + " prób")
    imie = input("Podaj imię: ")
    plik = open("wyniki.txt", "a")
    plik.write(imie + " " + str(p) + "\n")
    plik.close()

def tabela():
    plik = open("wyniki.txt", "r")
    print(plik.read())
    plik.close()

try: wybor(a)
except: print("Podałeś zły wybór")
