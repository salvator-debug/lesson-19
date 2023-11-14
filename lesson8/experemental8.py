list_of_colors = []
colors = ["red", "blue", "yellow", "green", "purple", "pink", "brown", "black", "white"]
while True:
    color = input("введіть кольор: ").lower()
    if not color in colors:
        print("такого кольору не існує")
    else:
        list_of_colors.append(color)
    if len(list_of_colors) == 4:
        break

print(list_of_colors)
