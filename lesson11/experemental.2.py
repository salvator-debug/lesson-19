from random import *

numbers = [randint(-10, 10) for i in range(5)]
print(numbers)


def bigmult(numbers):
    n = 1
    for el in numbers:
        n *= el
    return n


print(bigmult(numbers))


# task2
def letters(text):
    small_letters = 0
    big_letters = 0
    for el in text:
        if el.isupper():
            big_letters += 1
        else:
            small_letters += 1
    return f"No. Кількіcть великих букв : {big_letters} No. Кількість маленьких букв : {small_letters} "


text = str(input("введіть текст : "))
print(letters(text))
