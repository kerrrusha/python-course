### классы

# класс:
# чертеж для построения обьектов класса (экземпляров),
# который включает в себя данные а также методы для работы с этими данными
# 
# пример:
# чертеж дома - класс
# построенные дома по этому чертежу - обьекты. 
# эти дома могут различаться:
# кто то может иметь террасу, кто то - винный погреб, кто то - бассейн

import enum

class Color(enum.Enum):
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0
    GRAY = 122, 122, 122

    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255

class Car:
    # конструктор по умолчанию
    def __init__(self) -> None:
        self.mark = "unknown"
        self.model = "unknown"
        self.productionYear = "unknown"
        self.color = "unknown"

    # конструктор с параметрами
    def __init__(self, mark, model, productionYear, color) -> None:
        self.mark = mark
        self.model = model
        self.productionYear = productionYear
        self.color = color

    def youngerThan(self, otherCar):
        return self.productionYear > otherCar.productionYear

    def theSameColor(self, otherCar):
        return self.color == otherCar.color

    def __str__(self):
        return f"{self.mark} {self.model}, {self.productionYear} year, {self.color.name} color"



golf = Car("Volkswagen", "Golf IV", 2002, Color.GRAY)
camry = Car("Toyota", "Camry 3.5", 2015, Color.GRAY)

cars = [golf, camry]
for car in cars:
    print(car)

print(golf.youngerThan(camry))
print(golf.theSameColor(camry))