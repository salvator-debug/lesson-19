from random import *


random_list = [randint(0, 100) for i in range(10)]
print(random_list)

big = random_list[0]
for nomer in range(10):
    if random_list[nomer] > big:
        big = random_list[nomer]
# спочатку ми беремо 1 число якщо наступне чило його більше - пишемо наступне якщо ні - то пишемо 1 число і так далі
print("найбільше число: ", big)


# task2
def common_member(a, b):
    for el in a:
        if el in b:
            return True, el
            # якщо однаковий елемент є і в a і в b функція повертає True
    return False  # якщо ні то False


a = [randint(0, 100) for i in range(10)]
b = [randint(0, 100) for i in range(10)]
print(a)
print(b)
print(common_member(a, b))
# пишемо однаковий елемент якщо він є
