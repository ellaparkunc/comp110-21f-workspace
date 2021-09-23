"""Who Are You in the Wild Wild West???."""

__author__ = "730330121"

from random import randint
player: str = str()
points: int = 0
NAMED_CONSTANT: str = "\U0001F920"
print(NAMED_CONSTANT)


def main() -> None:
    """The Main Function where all my main functions are located."""
    greet()
    i: int = 0
    while i < 1:
        choice_0: str = str(input("Would you like to know how much of a cowboy you are, 1, know how many horses you have, 2, or quit, 3? "))
        if str(choice_0) == str("3"):
            i = i + 1
            quit()
        if str(choice_0) == str("1"):
            global points
            global j
            print(f"Hiya, {player}, where do you put your muddy boots? {NAMED_CONSTANT} ")
            choice_1: str = str(input("\"In mi stew cause they tastey gud!\" ? y or n "))
            if str(choice_1) == str("y"):
                """Leading to procedure."""
                points = points + 37
                print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")
                procedure()
                print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points. ")
                choice_6: str = str(input("Would you like to like to play again ,p or quit, q? "))
                if str(choice_6) == str("p"):
                    i = 0
                if str(choice_6) == str("q"):
                    i = i + 1
                    j = j + 1
            if str(choice_1) == str("n"):
                choice_2: str = str(input("All right, then where? On your wife's head? y or n "))
                if str(choice_2) == str("y"):
                    """Leading to function."""
                    i = i = 1
                    points = points + 22
                    print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")
                    points = (funct(points))
                    print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")
                    choice_7: str = str(input("Would you like to like to play again ,p or quit, q? "))
                    if str(choice_7) == str("p"):
                        i = 0
                    if str(choice_7) == str("q"):
                        i = i + 1
                        
                        quit()
                    
                if str(choice_2) == str("n"):
                    choice_3: str = str(input("\"Heavens, my boots are spotless, thank VERY much and I always put them where they belong\" y or n "))
                    if str(choice_3) == str("y"):
                        print(f"That's what I thought, you're the infamous cowboy imposter, The Shady {player}!! I should have known when you said your name was {player}. ")
                        i = 1 + 1
                        print("I'm exiting the game for you so you can think of some different answers. ")
                        quit()
                    if str(choice_3) == str("n"):
                        print(f"Lets try this again, silly {player}. ")
                    else:
                        print(f"All right, I know you can do this, {player}!")
                        print("We'll continue on.")
                else:
                    print("Let's try this again")
            else:
                print("\"I'm gonna choose some different answers this time!\"")
        if str(choice_0) == str("2"):
            points = (points + horse(0))
            print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")


def greet() -> None:
    """A Friendly Greeting."""
    print("Howdy, Pardner! Welcome to the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc. ")
    global player
    player = str(input("Whatcha go by round these parts? "))
    print(f"Okay Herdsman {player}, saddle up! ")


def procedure() -> None:
    """My Second Set of Questions (relies on global varriables shsared b/w main procedure and function I write)."""
    global points
    print(f"Now I know all cowboys love their horses, so {player}, what's your horse's name? ")
    print("Your choices are Frederique or Lizzo. ")
    choice_4: str = str(input("Type f for Frederique or l for Lizzo. "))
    if str(choice_4) == str("f"):
        points = points + 77
        print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")
        print(f"Thank you, {player}, for playing the the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc!")
        print("I hope you have a great day.")
    if str(choice_4) == str("l"):
        points = points + 44
        print(f"Your Cowboy Points {NAMED_CONSTANT} are at {points} points.")
        print(f"Thank you, {player}, for playing the the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc!")
        print("I hope you have a great day.")


def funct(a: int) -> int: 
    """A function that asks my last question and also doesn't let my function direcly access globals points."""
    print(f"So {player}, how do you like your coffee out on the range? ")
    choice_5: str = str(input("Answer \"b\" for black coffee or \"s\" for coffee like Starbucks makes. "))
    if str(choice_5) == str("b"):
        a = a + 100
    if str(choice_5) == str("s"):
        c: int = randint(1, 100)
        a = a + c
    return(a)


def horse(h: int) -> int:
    h = randint(1, 3000)
    print(f"Whoa, there bessy {player}! You have {h} horses! {NAMED_CONSTANT}")
    return(int(h + 1))


j: int = 0
while j < 1:
    if __name__ == "__main__":
        main()