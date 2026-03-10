# Eli Weaver
# Description: A menu to allow the player to pick what they want to do.

def showMenu() :
    while (True) :
        print(" 1 - Play the game")
        print(" 2 - Display final record")
        print(" 3 - Exit\n")

        iChoice = int( input("Make a selection: "))

        if (iChoice != 1 and iChoice != 2 and iChoice != 3) :
            print("Enter a valid choice!")
        else :
            return iChoice