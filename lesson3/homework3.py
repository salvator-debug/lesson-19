lane1 = str(input('Введіть перший рядок:'))
lane2 = str(input('Введіть другий рядок:'))
lane3 = str(input('Введіть третій рядок:'))

print('завдання1: довжина=')
print((len(lane1)) + (len(lane2)) + (len(lane3)))

print('Завдання2: найдовший рядок = ')
if (len(lane3))>(len(lane2))and(len(lane3))>(len(lane1)):
    print("Третій рядок")
if (len(lane2))>(len(lane3))and(len(lane2))>(len(lane1)):
    print("Другий рядок")
if (len(lane1))>(len(lane2))and(len(lane1))>(len(lane3)):
    print("Перший рядок")       
print('Завдання3:середина першого рядка:')
if len(lane1) % 2 ==1:
    print(lane1[len(lane1)//2])
else:
    print(lane1[len(lane1)//2-1] + lane1[len(lane1)//2])
print('середина другого рядка:')       
if len(lane2) % 2 ==1:
    print(lane2[len(lane2)//2])
else:
    print(lane2[len(lane2)//2-1] + lane2[len(lane2)//2])
print('середина третього рядка:')     
if len(lane3) % 2 ==1:
    print(lane3[len(lane3)//2])
else:
    print(lane3[len(lane3)//2-1] + lane3[len(lane3)//2])             