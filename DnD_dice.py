#code source Simon Monk 03_02_double_dice
import random
for x in range(1, 2):
    die_4 = random.randint(1,4)
    die_6 = random.randint(1, 6)
    die_8 = random.randint(1,8)
    die_10 = random.randint(1,10)
    die_12 = random.randint(1,12)
    die_20 = random.randint(1,20)
    total = die_4 + die_6 + die_8 + die_10 + die_12 + die_20
    print("Total=", total)
    if total == 6:
        print('Lucky Sixes!')
    if total == 11:
        print('Eleven Thrown!')
    if die_12 == die_20:
        print('Double Thrown!')
    print("D20 =", die_20)
    if die_20 == 20:
        print('Max D20!!')
    print("D12 =", die_12)
    if die_12 == 12:
        print('Max D12!!')             
    print("D08 =", die_8)
    if die_8 == 8:
        print('Max D8!!')
    print("D06 =", die_6)
    if die_6 == 6:
        print('Max D6!!')
    print("D04 =", die_4)
    if die_4 == 4:
        print('Max D4!!')