# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А и B')
print('координата х точки А -')
x1 = float(input())
print('координата y точки А -')
y1 = float(input())
print('координата х точки B -')
x2 = float(input())
print('координата y точки B -')
y2 = float(input())
if x1 > x2:
    x = x1 - x2
else:
    x = x2 - x1
if y1 > y2:
    y = y1 - y2
else:
    y = y2 - y1
print('расстояние между точками А и В равно ', round(((y**2 + x**2)**0.5), 2))
