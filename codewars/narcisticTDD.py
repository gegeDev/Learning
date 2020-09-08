import unittest #trzeba to zaimportować
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

class TestFunctions(unittest.TestCase): #trzeba zrobić taką klasę
    def test_first(test): #deklaracje testów, nazwa obiektu jest dowolna
        test.assertEqual(narcissistic(371), True) #testy
        test.assertEqual(narcissistic(123), False)#po oblaniu pierwszego testu reszta już się nie sprawdza, program zwraca tylko pierwszy nieudany test
        test.assertEqual(narcissistic(4887), False)
    def test_Second(self):
        self.assertEqual(narcissistic(371), True)
        self.assertEqual(narcissistic(123), False)
        self.assertEqual(narcissistic(4887), False)
        
unittest.main()
