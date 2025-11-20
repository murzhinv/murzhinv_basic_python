print("================================================")
print("Замыкания")
print("================================================")
print("задача №1")

def multiply_by(n):
    def multiplication(x):
        return x * n
    return multiplication
times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))

print("================================================")
print("задача №2")

def counter(start=0):
    res = start
    def update_counter():
        nonlocal res
        res += 1
        return res
    return update_counter

c1 = counter(5)
c2 = counter()

print(c1())
print(c1())
print(c2())
print(c2())

print("================================================")
