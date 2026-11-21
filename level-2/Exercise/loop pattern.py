text = 5

for i in range(text,-1,-1):
    print(i * " ", end="")
    print((text-i) * "^")

for i in range(8, 15, 2):
    print(i)


def count_vowels(word):
    w_low = word.lower()
    count = 0
    for i in w_low:
        if i in "aioue":
            count +=1
    print(f"Number of vowels in {word}:  {count}")
count_vowels("Galina")

def print_pattern(n):
    for row in range(2, n + 1):
        if row % 2 == 0:
            print("*" * row)
        else:
            print("-" * row)

print_pattern(6)

import turtle
from random import randint

turtle.bgcolor("black")
turtle.colormode(255)
turtle.pensize(3)
turtle.speed(0)

side_lengh = 5

for i in range(50):
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    turtle.color(red, green, blue)

    for j in range(3):
        turtle.forward(side_lengh)
        turtle.left(120)
    side_lengh += 10
    turtle.left(20)
turtle.exitonclick()


