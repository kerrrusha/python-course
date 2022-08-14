### переменные и типы данных

# int - целые числа
a = 13
b = 4

print(type(a))
print(f"Число a = {a}")
print(f"Число b = {b}")
print(f"int(3.98) = {str(int(3.98))}")

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

# целочисленное деление
print(f"a // b = {a // b}")
print(f"int(a / b) = {int(a / b)}")

# деление по модулю (остача от деления)
print(f"a % b = {a % b}")

print("###############################")

# float - реальные числа (числа с дробной частью)
a = 19.8
b = 5.25

print(type(a))
print(f"Число a = {a}")
print(f"Число b = {b}")
print(f"float(3) = {float(3)}")

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

# целочисленное деление
print(f"a // b = {a // b}")
print(f"int(a / b) = {int(a / b)}")

print("###############################")

# str - строки (текст)
a = "Hello "
b = "world!"

print(type(a))
print(f"Строка a = {a}")
print(f"Строка b = {b}")

print(f"a + b = {a + b}")

print("###############################")

# bool - логический тип данных (True/False)
a = True
b = False

print(type(a))
print(f"Переменная a = {a}")
print(f"Переменная b = {b}")

print(f"a == b : {a == b}")
print(f"a is b : {a is b}")
print(f"a != b : {a != b}")
print(f"a is not b : {a is not b}")

# логическое "И" - работает как знак умножения
# например: 
# True = 1
# False = 0
#
# 1 И 0 = 0
# 0 И 1 = 0
# 0 И 0 = 0
# 1 И 1 = 1
print(f"a and b : {a and b}")

# логическое "ИЛИ" - работает как знак суммирования
# например: 
# True = 1
# False = 0
#
# 1 И 0 = 1
# 0 И 1 = 1
# 0 И 0 = 0
# 1 И 1 = 1
print(f"a or b : {a or b}")

# 1 * 0 + 1 = 1
print(f"True and False or True : {True and False or True}")
# 1 * 0 + 1 * 1 = 1
print(f"True and False or True and True : {True and False or True and True}")

print("###############################")

a = 10
b = 5
# проверка на равенство (тоже самое что и 'is')
print(a == b)
# присванивание
a = b
print(a)

print("###############################")

# None - тип данных (означает отсутствие каких либо данных)
a = None
print(type(a))

print("###############################")

# list - тип данных СПИСОК
studentNames = ['Артур', "Никита", "Карлсон", "Данила", "Мария"]
print(type(studentNames))
print(studentNames)

# итераторный обход списка
for name in studentNames:
    print(name)

# арифметический обход
for i in range(len(studentNames)):
    print(f"{i}. {studentNames[i]}")

print("###############################")

# function - тип данных (описывает функцию)
def func(a, b):
    return a + b

# ссылка на фукнцию хранится в переменной, 
# теперь переменная может помогать запускать эту функцию
a = func
print(type(a))
print(a(10,5))

print("###############################")

# собственные типы данных
print("##############")
# структура "словарь" (ключ-значение)
person = {
    'name': 'Володя',
    'age': 69,
    'balance': 0.01,
    'friends': ["Хосеангел", "Фаврисио", "Матиас", "Родриго", "Габриэль"]
}
print(type(person))
print(person)

print("##############")
# классы 
class Person:
    def __init__(self, name : str, age : int, balance : float, friends : list):
        self.name = name
        self.age = age
        self.balance = balance
        self.friends = friends

    def __str__(self):
        result = "result of __str__ method:\n"
        result += f"name = {self.name}\n"
        result += f"age = {self.age}\n"
        result += f"balance = {self.balance}\n"
        result += f"friends = {self.friends}\n"
        return result

person = Person("Володя", 69, 0.01, ["Хосеангел", "Фаврисио", "Матиас", "Родриго", "Габриэль"])
print(type(person))
print(person)