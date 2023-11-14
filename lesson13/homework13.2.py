with open("lesson13/test.txt", "a") as file:  # відкриваю текстовий файл
    file.write("Random text ")
with open("lesson13/test.txt", "r") as file:  # зчитую його зміст
    print(file.read())

something = str(input("що ви хочете дописати ? "))
with open("lesson13/test.txt", "a") as file:  # дописую щось в текстовому файлі
    file.write(something)
file.close()  # закриваю файл
