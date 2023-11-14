from random import *

random_list = [randint(0, 100) for i in range(20)]
print(random_list)

even_list = [i for i in random_list if i % 2 == 0]
print(even_list)
odd_list = [i for i in random_list if i % 2 != 0]
print(odd_list)

even_list = [i if i % 2 == 0 else i + 1 for i in random_list]
print(even_list)
