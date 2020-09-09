def funkcja(f, a, b): return f(a, b)

print(funkcja(lambda x, y: y ** x, 2, 3)) #lambda tworzy funkcję od razu przy podawaniu jej jako argument do innej funkcji. Lambda musi wykonywać się w jednej linijce i może przyjmować kilka argumentów jak powyżej

def kwadrat(x): return x ** 2
print(kwadrat(12))

wyn = lambda c: c ** 2 #deklaracja funkcji lambda, wyn przejmuję działanie funkcji
print(wyn(3)) #tak się ją wywołuje

wyn = lambda (d: d ** 2)(5) #przypisanie do zmiennej wyn wartości funkcji lambda dla 5 a nie całej funkcji
print(wyn)
