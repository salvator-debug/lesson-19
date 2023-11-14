num = int(input("введіть число :"))
for i in range(num):
    for x in range(num):
        if i == 0 or x == 0 or i == num - 1 or x == num - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
