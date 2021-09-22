"""Who Are You in the Wild Wild West???."""

__author__ = "730330121"

points: int = 0
player: str = str()

def main() -> None:
    # The Main Function where all my main functions are located
    greet()
    print("Where do you put your muddy boots? ")
    procedure()
    func()


def greet() -> None:
    # A Friendly Greeting
    print("Howdy, Pardner! Welcome to the ARE YOU A COWBOY FOR REAL TIMES FOR REAL Game Inc. ")
    player = str(input("Whatcha go by round these parts? "))
    print(f"Okay Herdsman {player}, saddle up! ")

def procedure() -> None:
    # If you choose

# Entrypoint to program
if __name__ == "__main__":
    main()