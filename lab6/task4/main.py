from math import (ceil)
arr = []

try:
	fileInput = open('input.txt', 'r')
	
	linesInput = fileInput.readlines()

	if (len(linesInput) < 2):
		raise ValueError()

	strInput = linesInput[1]

	arr = strInput.split(' ')
	arr = [int(item) for item in arr]

	fileInput.close()

	# Функция возвращающая минимальное число в массиве
	def minArr(arr):
		min = abs(arr[0])

		for i in range(len(arr)):
			if (abs(arr[i]) < min):
				min = arr[i]

		return min

	# Сумма модулей элементов после нуля
	def sumAfterZero(arr):
		firtZeroIndex = -1
		sum = 0

		# Находим индекс первого элемента равного нулю
		for i in range(len(arr)):
			if arr[i] == 0:
				firtZeroIndex = i
				break;

		# Находим сумму модулей элементов расположенных после firtZeroIndex
		for i in range(firtZeroIndex, len(arr)):
			sum += abs(arr[i])

		return sum

	# Преобразовывает массив таким образом, что первая половина элементов
	# массива стоит на четных позициях, а вторая на нечетных
	def changeArr(arr):
		newArr = [0] * len(arr)
		indexEven = 0
		indexOdd = 1

		firstHalf = ceil(len(arr)/2)

		arrFirst = arr[:firstHalf]
		arrSecond = arr[firstHalf:]

		for i in range(len(arrFirst)):
			newArr[indexEven] = arrFirst[i]
			indexEven += 2
		
		for i in range(len(arrSecond)):
			newArr[indexOdd] = arrSecond[i]
			indexOdd += 2

		return newArr
	
	fileOutput = open('output.txt', 'w', encoding="utf-8")

	fileOutput.write('Исходный массив: {}\n'.format(arr))
	fileOutput.write('_________________________________\n')
	fileOutput.write('Минимальное по модулю число: {}\n'.format(minArr(arr)))
	fileOutput.write('Сумма модулей элементов после нуля: {}\n'.format(sumAfterZero(arr)))
	fileOutput.write('Преобразованный массив: {}\n'.format(changeArr(arr)))

	fileOutput.close()

except ValueError:
    print('Введите корректное число.')


