def liczby(ile): #zwykła funkcja, da się to zrobić lepiej ale ma być yield
    for i in range(ile): yield i + 1

def pierwsze(liczba): #funkcja sprawdza czy liczba jest pierwsza
    if liczba == 1: return False
    return not any([liczba % (i + 2) == 0 for i in range(liczba - 2)]) #return not (bool) zwraca przeciwieństwo
def filtruj(arr):
    return filter(pierwsze, arr) #funkcja filter, filtruje tylko liczby pierwsze do zwracanej tablicy

arr = (list(filtruj(list(liczby(250)))))
print(arr)

arr = map(lambda x: x+1, arr)
print(list(arr))
