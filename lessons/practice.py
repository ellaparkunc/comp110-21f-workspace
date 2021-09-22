player: str = str()

def main() -> None:
    # The Main Function where all my main functions are located
    greet()
    i: int = 0
    while i < 1:
        print("Where do you put your muddy boots? ")
        choice_1: str = str(input("\"In mi stew cause they tastey gud!\" ? y or n "))
        print(choice_1)
        if str(choice_1) == str("y"):
            procedure()
            i = i = 1
        if str(choice_1) == str("n"):
            choice_2: str = str(input("All right, then where? On your wife's head? y or n "))
            print(choice_2)
            if str(choice_2) == str("y"):
                funct()
                i = i = 1
            if str(choice_2) == str("n"):
                choice_3: str = str(input("\"Heavens, my boots are spotless, thank VERY much and I always put them where they belong\" y or n "))
                if str(choice_3) == str("y"):
                    print(f"That's what I thought, you're the infamous cowboy imposter, The Shady {player}!! I should have known when you said your name was {player}.")
                    i = 1 + 1
                if str(choice_3) == str("no"):
                    print(f"Lets try this again, silly {player}. ")
                else:
                    print("hey duddde")
            else:
                print("Come on man")
        else:
            print("You have to answer y or n and capitalization matters.")


def greet() -> None:
    # A Friendly Greeting
    print("Howdy, Pardner! Welcome to the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc. ")
    global player
    player = str(input("Whatcha go by round these parts? "))
    print(f"Okay Herdsman {player}, saddle up! ")

if __name__ == "__main__":
    main()