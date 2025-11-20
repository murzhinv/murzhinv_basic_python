print("================================================")
print("Лямбда-функции")
print("================================================")
print("задача №1")

square = lambda a: a**2
print(square(3))

print("================================================")
print("задача №2")

even_number = lambda x: x % 2 == 0
print(even_number(3))
print(even_number(4))

print("================================================")
print("задача №3")

def sort_by_last_letter(words_list):
    return sorted(words_list, key=lambda x: x[-1])
words_1 = ["banana", "apple", "cherry"]
words_2 = ["apple", "banana", "cherry"]
print(sort_by_last_letter(words_1))
print(sort_by_last_letter(words_2))

print("================================================")
