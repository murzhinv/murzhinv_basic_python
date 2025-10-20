print("================================================")
print("Задачи по уроку 'Цикл for в Python – основы и применение'")
print("================================================")
print("1. Вывести все символы строки в обратном порядке")
# user_string = input("Введите строку: ")
# result = []
# for i in range(len(user_string) -1, -1, -1):
#     result.append(user_string[i] )
# print(result)

print("================================================")
print("2.Замена четных элементов списка на 0")
numbers = [1, 4, 5, 8, 9, 10, 3]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0
print(numbers)

print("================================================")
print("3. Генерация списка степеней двойки")
# n = int(input("Введите число: "))
# result  = []
# for i in range(n+1):
#     result.append(2 ** i)
# print(result)
print("================================================")
print("4. Вывод всех чисел от A до B с шагом K")
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
K = int(input("Введите шаг K: "))
result = []
for i in range(A, B + 1, K):
    result.append(i)
print(result)
print("================================================")