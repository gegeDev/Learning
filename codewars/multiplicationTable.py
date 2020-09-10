def multiplication_table(size):
    arr = []
    for i in range(size): arr.append(list(range(i+1, (i+1) * size + 1, i +1)))
    return arr

def refactored(size): return [[(i +1) * (j + 1) for i in range(size)]for j in range(size)]
print(refactored(5))
