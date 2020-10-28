arr = []

arrayLength = int(input('Введите длину массива: '))

# Ввод элементов массива
print('Введите элементы массива')
for i in range(arrayLength):
	arr.append(int(input('> ')))
#

# Функция возвращающая минимальное число в массиве
def minArr(arr):
	min = abs(arr[0])

	for i in range(arrayLength):
		if (abs(arr[i]) < min):
			min = arr[i]

	return min
#

print('Минимальное по модулю число: {}'.format(minArr(arr)))