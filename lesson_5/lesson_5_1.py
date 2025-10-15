# streets = ['Луговая','Осенняя','Весенняя']
# ages = [23,54,26]

"""
        0           1           2
 ['Луговая', 'Осенняя', 'Весенняя']
        -3          -2          -1
"""
# print(streets[-2])
# print(streets[2])
# print(streets[-1])

# avg_age = int(sum(ages)/len(ages))
# print(avg_age)

# ages[1] = 31
# print(ages)

# lst = ['Луговая', 123, '21.22', True, False, ['Луговая', 123, '21.22', True, False,]]
# print(lst)

lst = []
lst2= list()
lst3 = list("Луговаяа")
# print(lst3)
# print(len(lst3))
# print(max(lst3))
# print(max(ages))
# print(min(lst3))
# print(min(ages))
# print(sum(ages))
# print(sorted(lst3))
# print(sorted(ages))
# print(sorted(ages, reverse=True))

streets = ['Луговая','Осенняя','Весенняя']
ages = [23,54,26]
result = streets + ages
print(result + ['A'])
print(result * 2)
print('Луговая' in result)
result.append('1234')
print(result)
result.append([2, 5])
print(result)
del result [1]
del result [-1]
print(result)


