from math import (sqrt, fabs)

try:
	x = float(input('Введите x: '))
	
	def f(x):
		if x <= -6:
			D = 16 - 4 * (x + 8)**2

			y1 = (4 - sqrt(D))/2
			y2 = (4 + sqrt(D))/2

			if (y1 < 0 or y1 > 2):
				return y2
			else: 
				return y1

		if x >= -6 and x <= -4:
			return 2

		if x >= -4 and x <= 2:
			if x == 0:
				y = fabs(-3 * x/6)
			else:
				y = -3 * x/6

			return y

		if x >= 2:
			return x - 3

	print('x = {0:.5f}, y = {1:.5f}'.format(x, f(x)))

except ValueError:
    print('Введите корректное число.')
