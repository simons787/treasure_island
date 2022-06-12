print("Welcome to the treasure island, your mission is to find the treasure")

direction = str(input(" Do you wanna go left or right ?"))
if direction == left:
    print("Ok, now you are going to the left")
    print("There is a small pond")
    doOne = str(input("Do you want to swim or wait ?"))
    if doOne == wait:
        print("OK")
    else:
        print("Game over")
else:
    print("Game over")
