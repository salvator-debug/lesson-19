suma = 0
for i in range(10):
    number1 = input("введіть перше число:")
    while not number1.isdigit() and number1 < 10:
        print("ви ввели не число або число")
        number1 = input("введіть перше число:")
    number1 = int(number1)
    suma += number1
mark1 = int(input("введіть першу оцінку:"))
if (mark1 < 13) == True:
    print
    for i in range(10):
        number2 = input("введіть друге число:")
    while not number2.isdigit():
        print("ви ввели не число")
        number2 = input("введіть друге число:")
    number2 = int(number2)
    suma += number2
    mark2 = int(input("введіть другу оцінку:"))
    while (mark2 > 0 and mark2 < 13) == True:
        print
    else:
        print("оцінка має бути 12-бальній системі")
else:
    print("введіть оцінку по 12 системі")
print(suma)
