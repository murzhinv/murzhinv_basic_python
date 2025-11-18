print("================================================")
print("Множества в Python")
print("================================================")
print("задача №1")
set_1 = {1,2,3,4,("a","b","c")}
print(set_1)
set_1.add(5)
print(set_1)
set_1.add(2)
print(set_1)
print("================================================")
print("задача №2")
set_cities = {"Питер", "Москва","Казань"}
print(set_cities)
print(len(set_cities))

print("================================================")
print("задача №3")
set_num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_num.remove(5)
set_num.discard(15)
print(set_num)

print("================================================")
print("задача №4")
str_1 = "abrakadabra"
set_1 = set(str_1)
print(set_1)
print(len(set_1))

print("================================================")
print("задача №5")
set_2 = set()
set_2.add(10)
set_2.add("hello")
set_2.add((1, 2, 3))
# set_2.add([4, 5, 6]) #- нельзя добавить изменяемые типы данных (set, list, dict)

print("================================================")
print("задача №6")
a = {1,4,5,8,9}
b = {9,8,2,3,6,8}
res = a & b
print("Пересечение a и b: ", res)
res = a.intersection(b)
print("Также пересечение равно: ", res)
res = a | b
print("Объединение равно: ", res)
res = a - b
print(res)
res = b - a
print(res)
res = a ^ b
print(res)

print("================================================")
print("задача №7")
add_numbers = {1, 3, 5, 7, 9}
even_numbers = {2, 4, 6, 8, 10}
res = even_numbers & add_numbers # нет пересекающихся элементов  set() - пустое
print(res)
res = even_numbers | add_numbers # все значения записались так как они уникальные, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(res)
print("================================================")
print("задача №8")
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print("На оба курса записаны:", python_students & java_students)
print("Только на один курс записаны: ", python_students ^ java_students)
print("Хотя бы на один курс записаны: ", python_students | java_students)
print("================================================")
print("задача №9")
text1 = set("программирование")
text2 = set("автоматизация")
print(text1 & text2)
print(text1 - text2)
print(text1 ^ text2)
print("================================================")
