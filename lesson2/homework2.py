# калькулятор
num1 = int(input("Введіть перше число : "))
num2 = int(input("Введіть друге число : "))
znak = input("Введіть знак :(+, -, *, /, //, **, %)")
if znak == "+":
    print(num1 + num2)
if znak == "-":
    print(num1 - num2)
if znak == "*":
    print(num1 * num2)
if znak == "/":
    if num2 == 0 or num1 == 0:
        print("Ділення на нуль немає")
    else:
        print(num1 / num2)
if znak == "//":
    print(num1 // num2)
    if num2 == 0 or num1 == 0:
        print("Ділення на нуль немає")
    else:
        print(num1 % num2)

if znak == "**":
    print(num1**num2)
if znak == "%":
    if num2 == 0 or num1 == 0:
        print("Ділення на нуль немає")
    else:
        print(num1 % num2)

# місяці
numer = int(input("номер місяця :"))
if numer == 3 or numer == 4 or numer == 5:
    print("весна")
elif numer == 6 or numer == 7 or numer == 8:
    print("літо")
elif numer == 9 or numer == 10 or numer == 11:
    print("осінь")
elif numer == 12 or numer == 1 or numer == 2:
    print("зима")
elif numer > 12 or numer <= 0:
    print("такого місяця не існує")
