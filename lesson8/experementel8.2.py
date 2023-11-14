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
