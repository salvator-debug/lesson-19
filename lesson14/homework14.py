names = ["Roma Arsen Tanya Kolya Ira "]
gmails = [
    "Roma@gmail.com Arsen@gmail.com Tanya@gmail.com  Kolya@gmail.com Ira@gmail.com"
]
with open("lesson14/test.txt", "a") as file:  # відкриваю текстовий файл
    names = "\n".join(names)

    gmails = "\n".join(gmails)

result = ["names :" + names + "gmails :" + gmails]
with open("lesson14/test.txt", "a") as file:
    file.write(str(result))
with open("lesson14/test.txt", "r") as file:  # зчитую його зміст
    print(file.read().split())
