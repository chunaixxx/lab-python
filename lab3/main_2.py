from math import (sqrt, fabs)
from random import *

try:
	R = float(input('Введите радиус: '))
	a = float(input('Введите ширину прямоугольника: '))
	b = float(input('Введите высоту прямоугольника: '))

	def f(x, y):
		if (x <= 0 and y <= 0 and x * x + y * y <= R * R and y >= -b/2)\
		or (x <= a/2 and y <= b/2 and x > 0 and y > 0 and x * x + y * y >= R * R):
			return 'Yes'
		else:
			return 'No'

	# Вывод входных данных
	print('')
	print('=================================')
	print('R = {0:.1f}, a = {1:.1f}, b = {2:.1f}'.format(R, a, b))
	print('=================================')
	print('')

	print('╔===========╗==========╔===========╗')
	print('║     X     ║     Y    ║    Res    ║')
	print('║===========║==========║===========║')
	for n in range(10):
		x = uniform(-b - 5, b + 5)
		y = uniform(-a - 5, a + 5)
		print('║    {0:.1f}    ║    {1:.1f}    ║    {2:.3s}    ║'.format(x, y, f(x, y)))
	print('╚==================================╝')

except ValueError:
    print('Введите корректное число.')