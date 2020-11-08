from math import (cos, sin, tan, radians, pi)

try:
	fileInput = open('input.txt', 'r')

	linesInput = fileInput.readlines()

	if (len(linesInput) != 2):
		raise ValueError()

	aDeg = int(linesInput[1])
	a = radians(aDeg)

	fileInput.close()

	def y1(a):
		if (cos(a) - sin(a)) == 0:
			raise ZeroDivisionError()

		return ((cos(a) + sin(a))/(cos(a) - sin(a)))

	def y2(a):
		if cos(2 * a) == 0:
			raise ZeroDivisionError()

		return tan(2 * a) + 1/cos(2 * a)

	fileOutput = open('output.txt', 'w', encoding="utf-8")
	fileOutput.write('a = {0:.9f}, y1 = {1:.9f}, y2 = {2:.9f}'.format(a, y1(a), y2(a)))
	fileOutput.close()

except ZeroDivisionError:
	print('Программа не смогла посчитать данное выражение.')

except ValueError:
	print('Введите корректное число.')
