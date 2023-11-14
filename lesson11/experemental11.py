def Sample_String(small_letter, big_letter, lane=str(input("введіть рядок : "))):
    small_letter = 0
    big_letter = 0

    for i in lane:
        if not i.isdigit() and i != " ":
            if i.islower():
                small_letter += 1
            elif not i.islower():
                big_letter += 1

    return eval(
        f"Великих букв : ",
        {Sample_String(big_letter)},
        "маленьких букв : ",
        {Sample_String(small_letter)},
    )
