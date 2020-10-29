arr = []

try:
	arrayLength = int(input('Введите длину массива: '))

	# Ввод элементов массива
	print('Введите элементы массива')
	for i in range(arrayLength):
		arr.append(int(input('> ')))

	# Функция возвращающая минимальное число в массиве
	def minArr(arr):
		min = abs(arr[0])

		for i in range(arrayLength):
			if (abs(arr[i]) < min):
				min = arr[i]

		return min

	# Сумма модулей элементов после нуля
	def sumAfterZero(arr):
		firtZeroIndex = -1
		sum = 0

		# Находим индекс первого элемента равного нулю
		for i in range(arrayLength):
			if arr[i] == 0:
				firtZeroIndex = i
				break;

		# Находим сумму модулей элементов расположенных после firtZeroIndex
		for i in range(firtZeroIndex, arrayLength):
			sum += abs(arr[i])

		return sum

	# Преобразовывает массив таким образом, что первая половина элементов
	# массива стоят на четных позициях, а вторая на нечетных
	def changeArr(arr):
		newArr = []
		firstHalf = -1

		if (arrayLength % 2 == 1):
			firstHalf = int(((arrayLength - 1)/2))
		else:
			firstHalf = int(arrayLength/2)

		for i in range(firstHalf):
			newArr.append(arr[i])
			if (i != firstHalf - 1):
				newArr.append(None)

		for i in range(firstHalf, arrayLength):
			if (i != firstHalf):
				newArr.append(None)
			newArr.append(arr[i])

		return newArr
		
	print('Исходный массив: {}'.format(arr))
	print('_________________________________')
	print('Минимальное по модулю число: {}'.format(minArr(arr)))
	print('Сумма модулей элементов после нуля: {}'.format(sumAfterZero(arr)))
	print('Преобразованный массив: {}'.format(changeArr(arr)))
except ValueError:
    print('Введите корректное число.')
