number = 0
while number < 1 or number > 10:
    number = int(input("введіть число: "))
    if number < 1 or number > 10:
        print("число повинно бути від 1 до 10")

for i in range(11):
    print(str(i) + " x " + str(number) + " = " + str(i * number))

suma = 0
for i in range(4):
    mark = 0
    while mark < 1 or mark > 12:
        mark = int(input("Введіть оцінку предмету " + str(i + 1) + ": "))
        if mark < 1 or i > 12:
            print("оцінка має бути 12-бальній системі")
        else:
            suma = suma + mark
print("Сума балів: " + str((suma)))
# --------
number1 = int(input("введіть перше число:"))

for i in range(10):
    if number1 < 11 and number1 > -1:
        print(i * number1)
    else:
        print("число повинно бути від 0 до 10")
mark1 = int(input("введіть першу оцінку:"))
if mark1 > 0 and mark1 < 13:
    print
else:
    print("оцінка має бути 12-бальній системі")

number2 = int(input("введіть друге число:"))

for i in range(10):
    if number2 < 11 and number2 > -1:
        print(i * number2)
    else:
        print("число повинно бути від 0 до 10")
mark2 = int(input("введіть другу оцінку:"))
if mark2 > 0 and mark2 < 13:
    print
else:
    print("оцінка має бути 12-бальній системі")

number3 = int(input("введіть третє число:"))
for i in range(10):
    if number3 < 11 and number3 > -1:
        print(i * number3)
    else:
        print("число повинно бути від 0 до 10")
mark3 = int(input("введіть третю оцінку:"))
if mark3 > 0 and mark3 < 13:
    print
else:
    print("оцінка має бути 12-бальній системі")

number4 = int(input("введіть четверте число:"))
for i in range(10):
    if number4 > -1 and number4 < 13:
        print(i * number2)
    else:
        print("число повинно бути від 0 до 10")
mark4 = int(input("введіть четверту оцінку:"))
if mark4 > 0 and mark4 < 13:
    print
else:
    print("оцінка має бути 12-бальній системі")
summ = (mark1) + (mark2) + (mark3) + (mark4)
print(summ)
