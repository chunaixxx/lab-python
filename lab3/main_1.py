from math import (sqrt, fabs)

try:
	xStart = float(input('Введите первую границу: '))
	xEnd   = float(input('Введите вторую границу: '))
	dx	   = float(input('Введите интвервал (dx): '))

	if (dx <= 0):
		raise ValueError	

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


	# Вывод входных данных
	print('')
	print('=====================================')
	print('xStart = {0:.1f}, xEnd = {1:.1f}, dx = {2:.1f}'.format(xStart, xEnd, dx))
	print('=====================================')
	print('')

	print('╔======================╗')
	print('║     X     ║     Y    ║')
	print('║======================║')
	
	# Вывод таблицы с аргументом и результатом функции
	x = xStart
	while (x < xEnd):
		print('║   {0:.1f}    ║    {1:.1f}   ║'.format(x, f(x)))
		x += dx

	print('╚======================╝')

except ValueError:
    print('Введите корректное число.')
