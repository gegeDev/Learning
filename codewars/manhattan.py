import unittest
import math
def manhattan_distance(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

class Testy(unittest.TestCase):
    def test_manhattan(test):
        test.assertEqual(manhattan_distance([1,1],[1,1]), 0)
        test.assertEqual(manhattan_distance([5,4],[3,2]), 4)
        test.assertEqual(manhattan_distance([1,1],[0,3]), 3)

unittest.main()
