from operator import index

print("================================================")
print("Методы списков")
print("================================================")
print("1. Добавление элементов")
numbers = [5, 10, 15]
numbers.append(20)
print(numbers)

numbers.insert(1,7)
print(numbers)

numbers.append('Python')
print(numbers)
print("================================================")
print("2. Удаление элементов")
print(numbers)
numbers.remove(10)

print(numbers)
print(numbers.pop(-1))

print(numbers)
print(numbers.pop(1))

numbers.clear()
print(numbers)
print("================================================")
print("3. Копирование списков")
letters = ["a", "b", "c"]
print(id(letters.copy()))
print(id(list(letters)))

print(id(letters.copy()) == id(list(letters)))
print("================================================")
print("4. Поиск элементов")
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))

print(marks.index(5))

print(6 in marks)
print("================================================")
print("5. Изменение порядка элементов")
nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
print("================================================")
print("6. Сортировка строк")
cities = ['Москва','Питер','Казань', 'Сочи']
print(cities)

cities.sort()
print(cities)

new_cities = sorted(cities)
print(new_cities)
print(cities)
print("================================================")
print("7. Дополнительное задание")
chars = list("programming")
print(chars)
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort() # сортировка в алфавитном порядке
print(chars)


print("================================================")