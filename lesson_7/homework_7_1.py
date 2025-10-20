print("================================================")
print("Задачи по уроку 'Цикл while'")
print("================================================")
print("1. Вывод чисел от 1 до N")
# n = int(input("Введите целое число: "))
# i = 1
# while i != n:
#     print(i)
#     i += 1

print("================================================")
# print("2. Сумма четных чисел до N")
# n = int(input("Введите целое число: "))
# sum = 0
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)
print("================================================")
print("3. Подсчет количества цифр в числе")
# number = input("Введите целое число: ")
# i = 0
# while i < len(number):
#     i += 1
# print(i)
print("================================================")
print("4. Определение максимальной цифры в числе")

# num = int(input("Введите целое число: "))
# i = 0
# max_digit = 0
# max_num = list(str(num))
# while i < len(max_num):
#         current_value = int(max_num[i])
#         if current_value > max_digit:
#             max_digit = current_value
#         i += 1
# print(max_digit)

print("================================================")
print("5. Запрос пароля")
password = input("Введите пароль: ")
correct_password = "1234"
i = 0
while password != correct_password:
    print("Ошибка! Не верный пароль")
    password = input("Введите пароль: ")
print("Пароль введен успешно ")

print("================================================")

