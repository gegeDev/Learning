def narcissistic(value):
    b = 0
    arr = []
    while(value / 10 ** b >= 1):
        arr.append(int(value / 10 ** b % 10))
        b += 1
    a = 0
    for i in arr: a += i ** b
    if a == value: return True
    else: return False
    
print(narcissistic(124))

