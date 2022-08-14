### циклы и списки

# в списках каждый элемент находится на своей позиции,
# которая называется индексом.
# в списках, нумерация индексов (позиций) начинается с 0:
#    i:        0        1        2       3        4
students = ["Jaime", "Chloe", "Carla", "Amma", "Sofia"]
amount = len(students)

print(f"Students amount: {amount}")

print(f"Student at 0th index: {students[0]}")
print(f"Student at 2th index: {students[2]}")

print("#################################################")

# арифметический цикл
for i in range(amount):
    print(f"{i+1}) {students[i]}")

print("#################################################")

# цикл методом перебора
for student in students:
    print(f"student = {student}")

print("#################################################")

# условный цикл
i = 0
while i < 5:
    print(students[i])
    i += 1

# условный бесконечный цикл
while True:
    pass    # "заглушка" для отсутствия кода 
            # (когда мы ничего пока еще не придумали, что здесь должно быть)
