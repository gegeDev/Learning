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
    
def refactored(value):
    a = str(value)
    nvalue = sum(int(i) ** len(a) for i in a) #funkcja sum jest genialna
    return nvalue == value #zapamiętaj to
