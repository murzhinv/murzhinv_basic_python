print("================================================")
print("Генераторы множеств и словарей")
print("================================================")
print("задача №1")

set_1 = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(set_1)

print("================================================")
print("задача №2")

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
res = {i.upper() for i in words}
print(res)

print("================================================")
print("задача №3")

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
res = {key: ("отлично" if value >=  80 else "удовлетворительно") for key, value in grades.items()}
print(res)
print("================================================")
print("задача №4")

text = {"Python", "automation", "programming", "testing"}
text_dict = {key: len(key) for key in text}
print(text_dict)
print("================================================")
print("задача №5")

n = int(input("Введите n: "))
res = {
    k : {v ** 2 for v in range(1, k + 1)}
    for k in range(1, n + 1)
}
for key, value in res.items():
    print(key, sorted(value))
print("================================================")
