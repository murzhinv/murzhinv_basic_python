print("================================================")
print("Кортежи в Python")
print("================================================")
print("задача №1")
my_tuple = (31, "Николай", 3.5, True, [1, 2, 3])
print(my_tuple[1])
print(my_tuple[-1])

print("================================================")
print("задача №2")
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))

print("================================================")
print("задача №3")
lst = ["Python", "Java", "C++", "JavaScript"]
lst1 = tuple(lst)
print(lst1)
if "C++" in lst1:
    print("'C++' есть в списке" )
else:print("'C++' нет  в списке" )

print("================================================")
print("задача №4")
numbers = tuple(range(1,11))
print(numbers)
print(numbers[:3])
print(numbers[-3:])
print(numbers[::2])

print("================================================")
print("задача №5")
my_tuple = ([1, 2, 3], {"a": 10, "b": 20})
print(my_tuple)
my_tuple[0].append(5)
print(my_tuple)

print("================================================")




