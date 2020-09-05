import random
def arr():
	n = []
	x = 0
	d = "0123456789"
	while x < 10:
		num = ""
		y = 0
		while y < 10:
			num += d[random.randint(0,9)]
			y += 1
		n.append(num)
		x += 1
	return n

def sortuj(tablica):
    d="0123456789"
    x = 9
    temp = []
    while x >= 0:#kolejne miejsca cyfr w liczbie
        y = 0
        while y < 10:#kolejne cyfry
            z = 0
            while z < 10:#kolejne liczby
                if tablica[z][x] == y:
                    temp.append(tablica[z])
                z += 1
            y += 1
        x -= 1

