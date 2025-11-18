print("================================================")
print("Множества в Python")
print("================================================")
print("задача №1")

def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")
greet("Николай")

print("================================================")
print("задача №2")

def square(num):
    res =  num ** 2
    print(res)
square(5)

print("================================================")
print("задача №3")
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

print("================================================")
print("задача №4")

def repeat_string(text, times):
    res = str(text) * times
    return res
print(repeat_string("Python", 3))

print("================================================")
print("задача №5")

def add(a, b):
    res = a + b
    return res
print(add(10, 2))

print("================================================")
print("задача №6")

def get_max(a, b, c):
    res = max(a, b, c)
    return res
print(get_max(10, 25, 7))

print("================================================")
print("задача №7")

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b

print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 5, "/"))

print("================================================")
print("задача №8")
def reverse_string(text):
    reverse = text[::-1]
    return reverse
print(reverse_string("Python"))

print("================================================")
print("задача №9")

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case and ignore_spaces:
        return s1.replace(" ", "").lower() == s2.replace(" ", "").lower()
    elif ignore_case and not ignore_spaces:
        return s1.lower() == s2.lower()
    elif not ignore_case and ignore_spaces:
        return s1.replace(" ", "") == s2.replace(" ", "")
    else:
        return s1 == s2

print(compare_strings("Hello", " hello "))  # True
print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False

print("================================================")
print("задача №10")

def summarize(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    return total

print(summarize(1, 2, 3))           # 6
print(summarize(10, "abc", 5, 2))   # 17

print("================================================")
print("задача №11")

def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print("Имя: ", name)
    print("Возраст: ", age)
    for key, value in extra.items():
        print(f"{key}: {value}")

create_profile("Иван", 30, city="Москва", job="Инженер")
print("================================================")
print("задача №12")

def process_orders(*orders, discount=0):
    total_sum = sum(orders)
    discount_sum = total_sum * (1 - discount / 100)
    print(f"Сумма заказа: {total_sum}")
    print(f"С учетом скидки: {int(discount_sum)}")
    return ""

print(process_orders(100, 200, 300, discount=10))

print("================================================")
print("задача №13")

def merge_lists(*lists):
    sum_list = []
    for x in lists:
        sum_list.extend(x)
    return sum_list
print(merge_lists([1, 2], [3, 4], [5, 6]))


print("================================================")
print("задача №14")

def  merge_dicts(*dicts):
    result = {}
    for i in dicts:
        result.update(i)
    return result
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))

print("================================================")