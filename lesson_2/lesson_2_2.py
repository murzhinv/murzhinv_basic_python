s1 = "Nikolay"
s2 = 'Murzhi'

s3 = """
Nikolay
Murzhi"""
print(s3)

s4 = "Nikolay\nMurzhi"
print(s4)

s5 = s1 + " " + s2
print(s5)

s6 = (s1 + " ") * 5
print(s6)
s7 = len(s2)
print(s7)

print(s1 in s3 )
print("Nikolay" == s1)
print("Murzhi" == s3)

a = "1234"
print(type(int(a)))