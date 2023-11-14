word = str(input("слово:"))
if (word[:]) == (word[::-1]):
    print("паліндром")
else:
    print("не паліндром")
# Завдання 2
numer = str(input("Введіть число:"))
if numer.isdigit() and len(numer) == 2:
    if (numer[0]) == (numer[1]):
        print("числа однакові")
    elif (numer[0]) > (numer[1]):
        print("перше число більше")
    elif (numer[1]) > (numer[0]):
        print("друге число більше")
else:
    print("похибка")
# завдання3
password = str(input("введіть пароль :"))
if len(password) >= 6:
    if (
        (password.isupper()) == False
        and (password.islower()) == False
        and (password.isalpha()) == False
    ):
        print("надійний пароль")
    else:
        print("ненадійний пароль")
else:
    print("довжина пароля повинна бути не менше шести симолів")
