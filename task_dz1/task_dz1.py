# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

numberDay = int(input('Введите цифру, обозначающую день недели: '))

if (numberDay == 6 or numberDay == 7):
    print(numberDay, 'день недели является выходным')
elif (numberDay > 0 and numberDay < 6):
    print(numberDay, 'день недели не является выходным')
else:
    print("Введите число от 1 до 7")
