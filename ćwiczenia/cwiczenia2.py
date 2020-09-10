lista1 = list(range(10))
a = 0
for i in lista1: a += i
print(a)
fib = [1, 1]
while len(fib) < 20: fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
print(fib)
