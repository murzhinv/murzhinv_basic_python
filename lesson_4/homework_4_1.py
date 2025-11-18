print("================================================")
print("Методы строк")
print("================================================")

print("1. Работа с регистром")
s = "Python для автоматизации"
print(s.upper())
print(s.lower())
print("================================================")
print("2. Подсчет вхождений подстроки")
msg = "абракадабра"
print(msg.find("ра"))
print(msg.find("а",2))
print("================================================")
print("3. Поиск подстроки")
msg = "абракадабра"
print(msg.find("ка"))
print(msg.rfind("а"))
print(msg.find("xyz")) # -1 ничего не нашел
print("================================================")
print("4. Замена подстроки")
text = "Я изучаю Java"
text2 = text.replace("Java", "Python")
print(text2)
print(text2.replace(" ", ""))
print("================================================")
print("5. Проверка содержимого строки")
text3 = "Phyton"
text4 = "1234"
text5 = "123asd"
print(text3. isalpha())
print(text4.isdigit())
print(not text5.isdigit())
print("================================================")
print("6. Дополнение строк")
code = "42"
print(code.rjust(5, "0"))
text = "text"
print(text.ljust(10,"*"))
print("================================================")
print("7. Разбиение строк")
text6 = "яблоко, груша, банан"
print(text6.split(", "))
text7 = "Python;Java;C++"
print(text7.split(";"))
print("================================================")
print("8. Объединение списка в строку")
text8 = ["Привет", "мир", "!"]
print(' ' .join(text8))
text9 = ["apple", "banana", "cherry"]
print(', ' .join(text9))
print("================================================")
print("9. Удаление пробелов")
text10 = " Python"
print(text10.lstrip())
text11 = "Python "
print(text11.rstrip())
text12 = " Python "
print(text12.strip())
print("================================================")
print("10. Дополнительное задание")
text13 = "программирование"
print(text13.replace("п", "П",1))
print(text13.count("р"))
print(text13.index("и",1))
print(text13[::-1])
print("================================================")