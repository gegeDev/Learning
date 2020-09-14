import math

class Punkt:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.distance = math.sqrt(x ** 2 + y ** 2)
    def __add__(self, drugi): #tak samo __sub__ __div__ __mul__ itd.
        return Punkt(self.x + drugi.x, self.y + drugi.y)
    def __lt__(self, drugi): #lt - less than le - less or equal gt - greater than ge - greater or equal
        return self.distance < drugi.distance
    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y 
    def __len__(self):
        return int(round(self.distance, 0))

p1 = Punkt(5, 4)
p2 = Punkt(3, 4)
p3 = p1 + p2
print(p3.distance)
print(p1 < p2)
print(p1 == p2)
print(len(p2))
