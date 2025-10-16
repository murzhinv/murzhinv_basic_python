a = 19
b = 18

# if a > b:
#     res = a
#
# elif b > a:
#     res = b
# else:
#     print("Числа равны ")
#
if a > b:
    res = a
else:
    res = b
print(res)

res = a + 10 if a > b else b
print(res)