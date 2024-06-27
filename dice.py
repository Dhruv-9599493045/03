print(''' do you want to roll the dice
      1. yes            2.no''')
#a = input("yes/no : ")
while True:
    import random
    #b = random.randint(1 , 6)
    #print(b)

    c = input("y/n ")
    if (c == "y"):
        print(random.randint(1 , 6))
    else:
        break

