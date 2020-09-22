def dig_pow(n, p):
    x = str(n)
    y = sum(int(x[i]) ** (p + i) for i in range(len(x)))
    if y % n == 0: return y / n
    return -1
