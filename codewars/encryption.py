def decrypt(text, n):
    x = len(text) // 2
    for i in range(n):
        a = text[:x]
        b = text[x:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(x + 1))
        #funkcja join() - do tablicy dodajemy sumę TABLIC jak w sum()
    return text

def encrypt(text, n):
    for i in range(n): text = text[1::2] + text[::2]
    return text 

print(decrypt("hsi  etTi sats!", 1))
