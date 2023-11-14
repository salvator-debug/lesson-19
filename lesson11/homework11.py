from random import *

numbers = [randint(-10, 10) for i in range(5)]
print(numbers)
# створюю рандомний список


def bigmult(numbers):
    n = 1
    # якби я написав 2 результат бувби вдвічі більшим
    for el in numbers:
        n *= el
    # числа в списку будуть множитись по порядку одне на одне
    return n


# повертаю результат
print(bigmult(numbers))
# пишу функцію


# task2
def letters(text):
    small_letters = 0
    big_letters = 0
    # створюю змінні великі й малі букви
    for el in text:
        # по порядку в тексті що напише користувач
        if el.isupper():
            big_letters += 1
            # якщо буква велика змінна виликі букви збільшується на 1
        else:
            small_letters += 1
            # якщо ні то змінна маленька буква збільшується на 1
    return f"No. Кількіcть великих букв : {big_letters} No. Кількість маленьких букв : {small_letters} "


# пишу результат з потрібним текстом
text = str(input("введіть текст : "))
print(letters(text))
# пишу функцію
