def decorator(func):
    def wrapper(): #deklaracja funkcji w funkcji, tak by funkcja decorator zwracała instrukcje funkcji wrapper
        print("-------------")
        func()
        print("-------------")
    return wrapper

def hello(): print("Hello world!")

hello = decorator(hello)
hello()

@decorator #przypisanie dekoratora domyślnie do funkcji
def witaj(): print("Witaj świecie!")
