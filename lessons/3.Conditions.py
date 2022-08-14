import enum

### условия 

class Person:
	def __init__(self, name : str, age : int, height : float, balance : float):
		self.name = name
		self.age = age
		self.height = height
		self.balance = balance

kirill = Person("Kirill", 19, 1.78, 162.23)
frida = Person("Frida", 23, 1.65, 220.23)

if kirill.age > frida.age:
	print("Kirill is older than Frida")
elif kirill.age is frida.age:
	print("Kirill and Frida have the same age")
else:
	print("Frida is older than Kirill")


# switch-case-default

class FoodType(enum.Enum):
	PIZZA = enum.auto()
	SALAD = enum.auto()
	BURGER = enum.auto()
	DRINKS = enum.auto()

eating = FoodType.BURGER
print(eating)

eating = FoodType.BURGER.name
print(eating)

eating = FoodType.BURGER.value
print(eating)

match eating:
	case FoodType.PIZZA:
		print("Eating pizza!")
	case FoodType.SALAD:
		print("Eating salad!")
	case FoodType.BURGER:
		print("Eating burger!")
	case FoodType.DRINKS:
		print("Drinking!")
	case _:
		print("Nothings to eat :(")