print("++++++++++++++++++++++++++++++++++++++++++++++++"
      "\n 1. Работа с целыми и вещественными числами"
      "\n++++++++++++++++++++++++++++++++++++++++++++++++")
a = 8
b = 3
x = 2.5
y = -1.7

print(type(int(a)))
print(type(int(b)))
print(type(int(x)))
print(type(int(y)))

print(" 2. Основные арифметические операции")

num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

print("3. Особенности работы с делением")
a = 10
b = 3
print(a/b)
print(a//b)
print(a%b)

a = -10
b = 3
print(a/b)
print(a//b)
print(a%b)

a = 10
b = -3
print(a/b)
print(a//b)
print(a%b)

print("4. Работа с приоритетом операторов")
print(5 + 3 * 2)
print((5 + 3) * 2)
print(10 / 2 ** 2)

print("5. Использование сокращенных операторов")
count = 10
count += 5
print(count)

count -= 3
print(count)

count *= 2
print(count)

count /= 4
print(count)

print("""++++++++++++++++++++++++++++++++++++++++++++++++
"Строки в Python".
++++++++++++++++++++++++++++++++++++++++++++++++""")

print("1. Создание строк")
s1 = "Python"
s2 = 'Программирование'
print(s1)
print(s2)

s3 = """Python Програмирование"""
print(s3)

s4 = " "
print(len(s4))

print("2. Конкатенация строк")
first_name = "Николай"
last_name = "Муржи"
full_name = first_name + " " + last_name
print(full_name)
print(first_name + " " + last_name)

print("3. Преобразование типов")

s = "Возраст: "
age = 25
print(s + str(age))

print("4. Дублирование строк")
print("xa " * 5)
# print("xa " * 2.5) должны быть целые числа

print("5. Длина строки")
text = "Привет, мир!"
print(len(text))

foo = " "
print(len(foo))
print(foo)

print("6. Проверка вхождения подстроки")
sentence = "Я изучаю Python"
print("Python" in sentence)
print("java" in sentence)

print("7. Сравнение строк")
a = "apple"
b = "banana"

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("8. Код символов")
print(ord("A"))
cod_1 = ord("a")
print(cod_1)
print(ord("Я"))