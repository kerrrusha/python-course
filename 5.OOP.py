# ООП - Обьектно Ориентированное Программирование
# ООП - подход к разработке программ, который подразумевает, что
# все что есть у тебя в программе - это обьекты.
# 
# у ООП есть так называемые "четыре кита":
# АБСТРАКЦИЯ, ПОЛИМОРФИЗМ, НАСЛЕДОВАНИЕ, ИНКАПСУЛЯЦИЯ

# абстракция - когда формируем класс только теми параметрами,
# которые нам нужны, игнорируя несущественные
class Person:
    # конструктор с параметрами
	def __init__(self, name : str, birthYear : int):
		self.name = name
		self.birthYear = birthYear

kirill = Person("Kirill", 2003)
elon = Person("Elon Musk", 1976)

# полиморфизм (инакословие)
class Math:
    def sum(a, b):
        print("#1")
        return a + b

    def sum(a, b, c):
        print("#2")
        return a + b + c

    def sum(numbers : list):
        print("#3")
        result = 0
        for number in numbers:
            result += number
        return result

# result = Math.sum(3, 5, 10)
# print(result)

# result = Math.sum([3, 5, 10, 25, 23])
# print(result)

# result = Math.sum(10, 20)
# print(result)

# 2
# 3 
# 1

# НАСЛЕДОВАНИЕ (INHERITANCE)
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Segment:
    def __init__(self, A : Dot, B : Dot):
        self.A = A
        self.B = B

    def __str__(self):
        return f"({self.A}, {self.B})"

class Triangle(Segment):
    def __init__(self, A : Dot, B : Dot, C : Dot):
        super().__init__(A, B)
        self.C = C

    def __str__(self):
        return f"({self.A}, {self.B}, {self.C})"

class Quadrilateral(Triangle):
    def __init__(self, A : Dot, B : Dot, C : Dot, D : Dot):
        super().__init__(A, B, C)
        self.D = D
    
    def __str__(self):
        return f"({self.A}, {self.B}, {self.C}, {self.D})"

square = Quadrilateral(
        Dot(0, 0), 
        Dot(0, 1),
        Dot(1, 1),
        Dot(1, 0)
    )

print(square)