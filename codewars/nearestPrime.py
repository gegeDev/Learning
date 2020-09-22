def solve(n):
    def prime(x):
        if x < 2: return False
        for i in range(x - 2):
            if x % (i + 2) == 0: return False
        return True
    o = 0
    while prime(n) == False:
        if prime(n - o) == True: return n - o
        if prime(n + o) == True: return n - o
        o += 1

print(solve(110))
print(solve(3000))
