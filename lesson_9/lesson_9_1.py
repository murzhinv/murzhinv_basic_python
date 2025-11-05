print("Словари в Python (dict)")

# dict_ex = ["Николай", "Муржи", "31", ["Москва", "Питер", "Казан"]]
dict_ex = {"name": "Николай", "last_name": "Муржи", "age": 31, "cities": ["Москва", "Питер", "Казан"], "smoke": False}
#print(dict_ex['age'])

# dict_ex = dict(name = "Nikolay", last_name = "Murzhi")
# print(dict_ex["name"])

# dict_ex = [["name", "Nikolay"], ["last_name", "Murzhi"]]
# print(dict(dict_ex))

# dict_ex = dict()

# """
# Ключами могут быть
# str
# int
# bool
# tuple
# """

# print(len(dict_ex))
# # del dict_ex['dqwfq']
#
# print(dict_ex)
# print('name' in dict_ex)

# dict_ex = dict.fromkeys(["Николай", "Муржи"], "qwert")
# dict_ex.clear()
# dict_ex_2 = dict_ex.copy()
# dict_ex_3 = dict(dict_ex)
# print(id(dict_ex_3))
# print(dict_ex_3)
# dict_ex_2['name'] = "Nikolay"
# dict_ex_2['name1'] = "Nikolay1"
# print(id(dict_ex))
# print(dict_ex)
# print(id(dict_ex_2))
# print(dict_ex_2)

# name = dict_ex.get("name")
# if name:
#     print(name)
# else:
#     print("Нет name")

# dict_ex.setdefault('name1', 'Dmitry')
# print(dict_ex)
# print(dict_ex)
# str1 = dict_ex.pop('name')
# print(str1)
# print(dict_ex)

# print(dict_ex)
# item = dict_ex.popitem()
# print(item)
# print(dict_ex)
# print(list(dict_ex.keys()))
# print(list(dict_ex.values()))
# print(list(dict_ex.items()))
# for key, value in dict_ex.items():
#     print(key, value)

dict_ex1 = {"name": "Николай"}
dict_ex2 = { "last_name": "Муржи"}
dict_ex1.update(dict_ex2)

print(dict_ex1)
print(dict_ex2)
dict_res = {**dict_ex1, **dict_ex2}
print(dict_res)


