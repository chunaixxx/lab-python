from math import (sqrt, fabs)

try:
	x = float(input('Введите x: '))
	y = float(input('Введите y: '))
	R = float(input('Введите радиус: '))
	a = float(input('Введите ширину прямоугольника: '))/2
	b = float(input('Введите высоту прямоугольника: '))/2

	def f():
		if (x <= 0 and y <= 0 and x * x + y * y <= R * R and y >= -b)\
		or (x <= a and y <= b and x > 0 and y > 0 and x * x + y * y >= R * R):
			return 'Попадает'
		else:
			return 'Не попадает'

	print(f())

except ValueError:
    print('Введите корректное число.')