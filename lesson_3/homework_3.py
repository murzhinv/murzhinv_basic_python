print("================================================")
print("1. Простая работа с print()")
print("================================================")
# Выведи на экран строку "Привет, мир!".
print("Привет, мир!")
# Выведи три числа: 5, 10, 15 через пробел.
a = 5
b = 10
c = 15
print(a, b, c)
# Выведи результат сложения 10 + 25.
print(10 + 25)
print("================================================")
print("2. Использование параметров sep и end в print()")
# Выведи числа 1, 2 и 3 через символ " & ", используя sep.
print(1, 2, 3, sep = " & ")

print("Напечатай Python и лучший язык в разных вызовах функции print() так, чтобы они выводились в одной строке, используя параметр end.")
print("Python", end = " ")
print("лучший язык")
print("================================================")
print("3. Форматированный вывод с F-строками")
x = 3.14
y = -8
print(f"Координаты точки: x={x}, y={y}")
# name = input("Введите имя: ")
# age = input("Введите возраст: ")
# print(f"Имя: {name}, Возраст: {age}")

print("================================================")
print("4. Работа с input()")
# name = input("Введите ваше имя:")
# print(f"Привет, {name}!")

print("================================================")
print("5. Преобразование типов")
# first_number = float(input("Введите первое число: "))
# second_number = float(input("Введите второе число: "))
# summ = first_number + second_number
# print(f"Сумма чисел {first_number} + {second_number} = {summ}")

# number = int(input("Введите целое число: "))
# print(number % 2 == 0)
# square = number ** 2
# print(f"квадрат числа {number} равен = {square} ")

print("================================================")
print("1. Основы булевой логики")
print("================================================")
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)

res = 8 > 12
print(type(res))
print("================================================")
print("2. Проверка четности и кратности числа")

x = 15
print((x % 2 == 0))
print((x % 5 == 0))
z = (x % 3 == 0) and (x % 5 == 0)
print(f"Число {x} делится на 3 И на 5? Ответ: {z}")

print("3. Работа с логическими операторами (and, or, not)")
# Создай переменную y = 4.5.
# Проверь, попадает ли y в диапазон [1, 10] (используй and).
y = 4.5
print(y>=1 and y<=10)
# Проверь, входит ли y в один из диапозонов [0, 5] или [10, 15] (используй or).
print((y>=0 and y<=5) or (y>=10 and y<=15) )
# Инвертируй проверку y < 5 с помощью not.
foo = not (y <= 5)
print(foo)
print("4. Приоритет логических операций")
# Вычисли и выведи результаты следующих выражений:
# True or False and False
# not False and True
# False or not True and True
# not (10 > 5 or 3 < 1)

res1 = True or False and False
print(f"True or False and False: {res1}")
res2 = not False and True
print(f"not False and True: {res2}")
res3 = False or not True and True
print(f"False or not True and True: {res3}")
res4 = not (10 > 5 or 3 < 1)
print(f"not (10 > 5 or 3 < 1): {res4}")

print("5. Приведение типов к bool")
print(type(bool(0)))
print(type(bool(-5)))
print(type(bool(3.14)))
print(type(bool("")))
print(type(bool("Python")))
print(type(bool(" ")))

print("6. Дополнительное задание")
n = 19
print("Положительное ли число ",n>0)
print(f"Является ли число {n} четным?", "Ответ ",n % 2 == 0 )
print(f"Делится  ли число {n} на 3?", "Ответ ", n % 3 == 0 )

print("================================================")
print("1. Доступ к символам по индексу.")
print("================================================")
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2],s[-1])
print("2. Обращение к символам с проверкой границ")
#print(s[100]) # ошибка, мы вышли за диапазон
print(len(s))
print("3. Создание срезов")
foo1 = s[0:6]
print(foo1)
foo2 = s[-5:]
print(foo2)
foo3 = s[2:7]
print(foo3)
foo4 = s[::2]
print(foo4)
foo5 = s[::-1]
print(foo5)
print("4. Работа с шагом в срезах")
foo6 = s[::3]
print(foo6)
foo7 = s[::-2]
print(foo7)
print("5. Проверка неизменяемости строк")
#s[0] = "п" # строки являются неизменяемыми
s2 = "п" + s[1:]
print(s2)
print("6. Дополнительное задание")
word = "abcdefgh"
print(word[2:5])
print(word[::-1])
print(word[1:-1])





