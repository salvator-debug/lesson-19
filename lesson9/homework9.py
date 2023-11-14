from random import *

random_list = [randint(0, 20) for i in range(10)]

# task1
double_list = [i for i in random_list if i % 2 == 0]
print("елементи списку з парними індексами : ", (double_list))
# task2
print("сума елементів всього списку : ", (sum(random_list)))
# task3
nondouble_list = (sum(random_list)) - (sum(double_list))
print("непарні елементи списку : ", (nondouble_list)), print(
    "парні елементи списку : ", (sum(double_list))
)
# task4


print(("максимальний елемент : "), (max(random_list)))
print(("його індекс : "), random_list.index(max(random_list)))
