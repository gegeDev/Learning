import unittest
def max_sequence(arr):
    if len(arr) == 0: return 0
    out = []
    for i in range(len(arr)): #iterowanie początków substringów
        for x in range(len(arr)): #iterowanie końców substringów
            out.append(sum(a for a in arr[i:x+1])) #koniec tablicy + 1 bo koniec wycinku jest wyłącznie
    return max(out)

def refactored(arr):
    maks, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > maks: maks = curr
    return maks

class Testy(unittest.TestCase):
    def test_first(test):
        test.assertEqual(refactored([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        test.assertEqual(refactored([]), 0)

unittest.main()
