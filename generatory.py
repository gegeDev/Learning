def gen():
    i = 0
    while i < 5:
        yield i #prawie jak return ale nie przerywa funkcji
        i += 1

for i in gen(): print(i) #iteruje po wszystkim co jest w yield

print(list(gen())) #tworzenie listy z generatora

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0: yield i
        i += 1

print(list(parzyste(14)))
