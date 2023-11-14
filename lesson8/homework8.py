list_of_colors = []
colors = [
    "red",
    "blue",
    "yellow",
    "green",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "grown",
]
while True:
    color = input("введіть кольор: ").lower()
    if not color in colors:
        print("такого кольору не існує")
    else:
        list_of_colors.append(color)
    if len(list_of_colors) == 4:
        break

print(list_of_colors)
# task2
list_numbers = []
end = ""
while True:
    num = input("введіть число : ")
    if num.isdigit() == False:
        print("введіть цифру")
    elif not int(num) % 2 == 0:
        list_numbers.append(num)
    else:
        print
    if num == "end":
        break

print(list_numbers)
