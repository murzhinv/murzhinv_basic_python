print("================================================")
print("Словари в Python (dict)")
print("================================================")
print("задача №1")
# fruit_prices = {"Яблоко": 150, "Банан": 120, "Апельсин": 200, "Манго": 350}
# print(fruit_prices)
# fruit_prices["Ананас"] = 330
# print(fruit_prices)

print("================================================")
print("задача №2")
# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# for name, grade in grades.items():
#     if grade >= 4:
#         print(name)

print("================================================")
print("задача №3")

# country = {"Россия": "Москва", "Турция": "Анкара", "Египет": "Каир", "Япония": "Токио", "Франция": "Париж"}
# print(country)
# input_country = input("Введите название страны (с заглавной буквы): ")
#
# if input_country in country:
#     result = country[input_country]
#     print(f"Столица страны '{input_country}' - {result}")
# else:
#     print("Страна не найдена")

print("================================================")
print("задача №4")
students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]

courses_students = {}
for student_name, course_name in students:
    if course_name in courses_students:
        courses_students[course_name].append(student_name)
    else:courses_students[course_name] = [student_name]
print(courses_students)

print("================================================")
print("задача №5")
# grades = {
#     "Анна": 5,
#     "Борис": 4,
#     "Виктор": 3,
#     "Галина": 5,
#     "Дмитрий": 2,
#     "Елена": 4
# }
# print(students)
# min_grade = min(grades, key=grades.get)
# print(min_grade)
# student_remove = grades.pop(min_grade)
# print(grades)

print("================================================")
print("задача №6")
# students = ["Анна", "Борис", "Виктор", "Галина"]
# students_dict = dict.fromkeys(students)
# print(students_dict)
# students_dict["Анна"] = 20
# students_dict["Борис"] = 22
# students_dict["Виктор"] = 19
# students_dict["Галина"] = 21
#
# print(students_dict)
print("================================================")
print("задача №7")
# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
# currency = input("Введите валюту (USD, EUR или GBP): ").upper()
# if currency in exchange_rates:
#     print(f"Курс {currency}: {exchange_rates[currency]}")
# else:print(f" {currency}: Неизвестная валюта.")
# exchange_rates[currency] = None
# print("Добавлена новая валюта со значением None.")
# print(exchange_rates)
print("================================================")
print("задача №8")
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)
