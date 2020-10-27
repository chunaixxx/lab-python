from math import (cos, sin, tan, radians, pi)

try:
    aDeg = float(input('Введите значение аргумента в градусах: '))
    a = radians(aDeg)

    def y1(a):
        if (cos(a) - sin(a)) == 0:
            raise ZeroDivisionError()

        return ((cos(a) + sin(a))/(cos(a) - sin(a)))

    def y2(a):
        if cos(2 * a) == 0:
            raise ZeroDivisionError()

        return tan(2 * a) + 1/cos(2 * a)

    print('a = {0:.9f}, y1 = {1:.9f}, y2 = {2:.9f}'.format(a, y1(a), y2(a)))

except ZeroDivisionError:
    print('Программа не смогла посчитать данное выражение.')

except ValueError:
    print('Введите корректное число.')










# def y2(a):
#     if cos(2 * a) == 0:
#         return 1.0

#     try:
#         return tan(2 * a) + 1/cos(2 * a)
#     except ArithmeticError:
#         print('Ошибка')

# if (y1(a) or y2(a)) == 'ERROR':
#     print('Нет решений')
# else:
#     print('a = {0:.9f}, y1 = {1:.9f}, y2 = {2:.9f}'.format(a, y1(a), y2(a)))