from random import (randint)

# Возвращает двумерный массив Row x Col со случайными значениями
# в диапазоне от min до max
def makeRandomArr(row, col, min, max):
	arr = [[0] * col for i in range(row)]

	for Row in range(row):
		for Col in range(col):
			arr[Row][Col] = randint(min, max)

	return arr

# Выводит количество локальных минимумов
def findLocalMin(arr):
	rowLength = len(arr)
	colLength = len(arr[0])
	count = 0

	for Row in range(rowLength):
		for Col in range(colLength):
			# Текущий элемент который нужно проверить
			el = arr[Row][Col]

			# Проверка первой строки
			if (Row == 0):
				if (Col == 0):
					# Проверка элемента в левом верехнем углу
					if  (el < arr[Row][Col + 1])\
					and (el < arr[Row + 1][Col + 1])\
					and (el < arr[Row + 1][Col]):
						count += 1
				elif (Col == colLength - 1):
					# Проверка элемента в правом верхнем углу
					if  (el < arr[Row][Col - 1])\
					and (el < arr[Row + 1][Col - 1])\
					and (el < arr[Row + 1][Col]):
						count += 1
				else:
					# Проверка остальных элементов в первой строке
					if  (el < arr[Row][Col - 1])\
					and (el < arr[Row + 1][Col - 1])\
					and (el < arr[Row + 1][Col])\
					and (el < arr[Row + 1][Col + 1])\
					and (el < arr[Row][Col + 1]):
						count += 1

			# Проверка последней строки
			if (Row == rowLength - 1):
				if (Col == 0):
					# Проверка элемента в левом нижнем углу
					if  (el < arr[Row - 1][Col])\
					and (el < arr[Row - 1][Col + 1])\
					and (el < arr[Row][Col + 1]):
						count += 1
				elif (Col == colLength - 1):
					# Проверка элемента в правом верхнем углу
					if  (el < arr[Row - 1][Col])\
					and (el < arr[Row - 1][Col - 1])\
					and (el < arr[Row][Col - 1]):
						count += 1
				else:
					# Проверка остальных элементов в поселедней строке
					if  (el < arr[Row][Col - 1])\
					and (el < arr[Row - 1][Col - 1])\
					and (el < arr[Row - 1][Col])\
					and (el < arr[Row - 1][Col + 1])\
					and (el < arr[Row][Col + 1]):
						count += 1

			# Проверка остальных строк (промежуточных)
			if (Row != rowLength - 1) and (Row != 0):
				# Проверка левого крайнего элемента
				if (Col == 0):
					if  (el < arr[Row - 1][Col])\
					and (el < arr[Row + 1][Col])\
					and (el < arr[Row][Col + 1])\
					and (el < arr[Row + 1][Col + 1])\
					and (el < arr[Row - 1][Col + 1]):
						count += 1
				
				# Проверка правого крайнего элемента
				elif (Col == colLength - 1):
					if  (el < arr[Row - 1][Col])\
					and (el < arr[Row + 1][Col])\
					and (el < arr[Row][Col - 1])\
					and (el < arr[Row + 1][Col - 1])\
					and (el < arr[Row - 1][Col - 1]):
						count += 1
				
				# Проверка любых не крайних элементов
				else:
					if  (el < arr[Row - 1][Col - 1])\
					and (el < arr[Row - 1][Col])\
					and (el < arr[Row - 1][Col + 1])\
					and (el < arr[Row + 1][Col - 1])\
					and (el < arr[Row + 1][Col])\
					and (el < arr[Row + 1][Col + 1])\
					and (el < arr[Row][Col - 1])\
					and (el < arr[Row][Col + 1]):
						count += 1

	return count


# Находит сумму элементов выше главной диагонали
def sumAbs(arr):
	rowLength = len(arr)
	colLength = len(arr[0])

	sum = 0

	startIndex = 1
	for Row in range(rowLength - 1):
		for Col in range(startIndex, colLength):
			sum += abs(arr[Row][Col])

		startIndex += 1
	
	return sum

arr = makeRandomArr(10, 10, 0, 9)

fileOutput = open('output.txt', 'w', encoding="utf-8")

fileOutput.write('_______ Исходный массив _______\n')
for Row in range(len(arr)):
	fileOutput.write('{0}\n'.format(arr[Row]))
fileOutput.write('_______________________________\n')

fileOutput.write('Количество локальных минимумов: {0}\n'.format(findLocalMin(arr)))
fileOutput.write('Сумма модулей элементов выше главной диагонали: {0}\n'.format(sumAbs(arr)))