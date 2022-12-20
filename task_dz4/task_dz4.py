# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четвери плоскости')
quarter_plane = int(input())
if quarter_plane > 4 or quarter_plane < 1:
    print('недопустимое значение четвери плоскости')
elif quarter_plane == 1:
    print('x = от 1 до ∞, у = от 1 до ∞')
elif quarter_plane == 2:
    print('x = от -1 до -∞, у = от 1 до ∞')
elif quarter_plane == 3:
    print('x = от -1 до -∞, у = от -1 до -∞')
elif quarter_plane == 4:
    print('x = от 1 до ∞, у = от -1 до -∞')
print(' ')
