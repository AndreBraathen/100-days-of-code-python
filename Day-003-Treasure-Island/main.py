print("Welcome to Treasure Island.")
choice1 = input('You're at a crossroad. Where do you want to go? "left" or "right"?\n').lower()

if choice1 == "left":
    choice2 = input('You've come to a lake. Type "wait" to wait for a boat or "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at three doors: red, yellow, blue. Which one do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("Burned by fire. Game over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")