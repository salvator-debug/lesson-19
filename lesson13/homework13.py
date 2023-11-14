import os
import shutil

os.mkdir("lesson13\FOLDER")  # створюю папку FOLDER
os.mkdir("lesson13\FOLDER2")  # створюю папку FOLDRE2
shutil.move(
    "lesson13\FOLDER2", "lesson13\FOLDER"
)  # переміщую папку FOLDER2 в папку FOLDER
shutil.copy("lesson13\homework13.py", "lesson13\FOLDER2")  # копіюю цю папку в FOLDER2
shutil.rmtree("lesson13\FOLDER")  # видаляю папку FOLDER якщо вона не пуста


# task2


with open("lesson13/test.txt", "a") as file:  # відкриваю текстовий файл
    file.write("Random text ")
with open("lesson13/test.txt", "r") as file:  # зчитую його зміст
    print(file.read())

something = str(input("що ви хочете дописати ? "))
with open("lesson13/test.txt", "a") as file:  # дописую щось в текстовому файлі
    file.write(something)
file.close()  # закриваю файл
