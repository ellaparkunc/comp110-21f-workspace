player: str = str()
points: int = 0

def main() -> None:
    # The Main Function where all my main functions are located
    greet()
    i: int = 0
    while i < 1:
        print("Where do you put your muddy boots? ")
        choice_1: str = str(input("\"In mi stew cause they tastey gud!\" ? y or n "))
        print(choice_1)
        if str(choice_1) == str("y"):
            i = i + 1
            global points
            points = points + 33
            print(points)
            procedure()
            quit()
        if str(choice_1) == str("n"):
            choice_2: str = str(input("All right, then where? On your wife's head? y or n "))
            print(choice_2)
            if str(choice_2) == str("y"):
                i = i = 1
                funct()
                quit()
            if str(choice_2) == str("n"):
                choice_3: str = str(input("\"Heavens, my boots are spotless, thank VERY much and I always put them where they belong\" y or n "))
                if str(choice_3) == str("y"):
                    global points
                    points = points - 100
                    print(f"That's what I thought, you're the infamous cowboy imposter, The Shady {player}!! I should have known when you said your name was {player}. ")
                    i = 1 + 1
                    print("This town aint big enough for the two of us. ")
                    print(f"You have {points} cowboy points :( ")
                    quit()
                if str(choice_3) == str("n"):
                    print(f"Lets try this again, silly {player}. ")
                else:
                    print(f"All right, I know you can do this, {player}!")
                    print("Answer exactly \"y\" or \"n\" to continue on")
            else:
                print("Come on man, it's a yes or no question! ")
                print("Answer exactly \"y\" or \"n\" to continue on")
                print("Let's try this again")
        else:
            print("You have to answer \"y\" or \"n\" and capitalization matters.")
            print("Let's try this again")

def greet() -> None:
    # A Friendly Greeting
    print("Howdy, Pardner! Welcome to the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc. ")
    global player
    player = str(input("Whatcha go by round these parts? "))
    print(f"Okay Herdsman {player}, saddle up! ")

def procedure() -> None:
    #My Second Set of Questions (relies on global varriables shsared b/w main procedure and function I write)
    print("Now I know all cowboys love their horses, so what's your horse's name? ")
    print("Your choices are Frederique or Lizzo. ")
    choice_4: str = str(input("Type f for Frederique or l for Lizzo. "))
    if str(choice_4) == str("f"):
        print("Thank you for playing the the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc!")
        print("I hope you have a great day.")
    if str(choice_4) == str("l"):
        print("Thank you for playing the the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc!")
        print("I hope you have a great day.")

if __name__ == "__main__":
    main()