name = "Sarah"
first_letter = name[0]
second_letter = name[1]
third_letter = name[2]
fourth_letter = name[3]
fifth_letter = name[4]
print(first_letter + second_letter + third_letter + fourth_letter + fifth_letter)

age = 33

if age >= 65:
    print("You are a senior")
elif age < 20 and age >= 13:
    print("You are a teenager")
elif age < 13:
    print("You are a child")
else:
    print("You are an adult")

fav_foods = ["pizza", "chocolate", "sushi", "curry"]

for i in fav_foods:
    print("I love to eat " + i + "!")


def subtract(x, y):
    return x - y


print(subtract(5, 2))  # 3, 5 is x, 2 is y
print(subtract(200, 50))  # 150, 200 is x, 50 is y
print(subtract(20, 70))  # -50, 20 is x, 70 is y

five = subtract(10, 5)
print(five)


def say_hi(person):
    print("Hi " + person)
    return person


sarah = say_hi("Sarah")
print(sarah)
