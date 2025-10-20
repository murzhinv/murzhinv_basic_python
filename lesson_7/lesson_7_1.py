# sum_1 = 1 + 2 + 3 + 4 +5
# print(sum_1)

# num = 1000
# sum_2 = 0
# i = 1
# while i <= num:
#     sum_2 += i
#     i += 1
#
# print(sum_2)

# input_password = input("Введите пароль: ")
# correct_password = "Gfhjkm123"

# while input_password != correct_password:
#     print("Пароль не верен! Введите еще раз")
#     input_password = input("Введите пароль: ")
# print("Пароль вверный")

# input_password = input("Введите пароль: ")
# correct_password = "12345"
# counter = 1
#
# while input_password != correct_password:
#     print(f"Пароль введен неправильно {counter} раз! Введите еще раз")
#     input_password = input("Введите пароль: ")
#     counter += 1
#     if counter == 3:
#         print(f"Доступ запрещен. Было больше {counter} попыток")
#         break
# print("Пароль верный")

# numbers = [23, 43, 75, 33, 80, 51, 62]
# result = []
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         result.append(numbers[i])
#     i += 1
#     if i == len(numbers):
#        break
# print(result)

num = 1
res_sum = 0
while num != 0:
    input_num = input("Введите целое число или 0 для выхода: ")
    if not input_num.isdigit():
        print("Введено не число, перезапустите программу")
        break
    num = int(input_num)
    if num % 2 == 0:
        continue
    res_sum += num
else:
    print(res_sum)
