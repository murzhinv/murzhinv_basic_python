print("================================================")
print("Списки")
print("================================================")
print("1. Создание списков")
cities = ['Москва','Тверь','Вологда']
numbers = [1,2,3,4,5]
mixed = [1, 'qwerty', True, 12.45]
print("================================================")
print("2. Доступ к элементам списка")
print(cities[0])
print(numbers[-1])
# print(cities[10]) выход за границы массива
print("================================================")
print("3. Изменение элементов списка")
# numbers[1] = 10
# print(numbers)
mixed[-1] = "Python"
print(mixed)
print("================================================")
print("4. Функции для работы со списками")
print(len(numbers))

print(f"Максимальное значение равно {max(numbers)}")
print(f"Минимальное значение равно {min(numbers)}")

print(sum(numbers))

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print("================================================")
print("5. Операции со списками")
a = [1, 2, 3]
b = [4, 5]
print(a+b)

c = ["Python", "is", "awesome"]
print(c * 3)
print("================================================")
print("6. Проверка вхождения")
print(3 in numbers)
print("Москва" in cities )
print([1, 2] in mixed)
print("================================================")
print("7. Удаление элементов")
cities1 = ['Москва','Тверь','Вологда']
numbers1 = [1,2,3,4,5]
print(numbers1)
del numbers1 [2]
print(numbers1)

print(cities1)
del cities1 [-1]
print(cities1)
print("================================================")
print("8. Дополнительное задание")
d = "Python"
lst = list(d)
print(lst)

print(max(lst))
print(min(lst))

# print(sum(lst)) нельзя складывать строки и числа
print("================================================")



