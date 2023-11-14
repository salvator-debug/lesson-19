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
