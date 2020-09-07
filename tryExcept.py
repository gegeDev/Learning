a = 0
b = 23
c = "!"

try:
    print(b + c) #po przechwyceniu pierwszego wyjątku reszta instrukcji w try się nie wykona
    print(b / a) #wykonuje się tylko pierwszy przechwycony wyjątek w try
except ZeroDivisionError:
    print("pamiętaj selero nie dziel przez zero")
except TypeError:
    print("Dodawanie dwoch roznych typow zmiennych")

try:
    print(b + c)
    print(b / a)
    print("nie wykonam się") #wykonają się instrukcje do momentu wychwycenia wszystkich błędów w except
except (ZeroDivisionError, TypeError):  #obsługiwanie kilku wyjątków jednocześnie
    print("Dodawanie roznych typow zmiennych i dzielenie przez zero")

#IndexError - wyjątek gdy wybieramy nieistniejący ineks tablicy
tab = []
try:
    print(tab[3])
except: #wykona się po wychwyceniu dowolnego błędu w try
    print("cos sie popsulo")
finally: #nie jest wymagany
    print("wykonam się niezależnie czy wystąpił błąd")
