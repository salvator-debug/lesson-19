# task1
hight = int(input("введіть висоту: "))
while hight < -1 or hight > 15:
    print("висота повинна були від 1 до 15")
    hight = int(input("введіть висоту: "))

    print
for i in range(hight):
    print(("-" * i + "*" * (hight - i)) + "*" * (hight - (i + 1)))

# task2
for i in range(1, 11):
    print("\t", i, end="")
print()

for i in range(1, 11):
    print(i, end="")
    for j in range(1, 11):
        print("\t", i * j, end="")
    print()
