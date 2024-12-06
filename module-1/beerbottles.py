# BeerBottles.py
# beer bottles song program
def countdown_bottles(num_bottles):
    """
    Counts down bottles of beer and prints the lyrics.

    Args:
        num_bottles: The initial number of bottles.
    """

    while num_bottles > 1:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.\n")

    if num_bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down, pass it around, 0 bottles of beer on the wall.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")

    if num_bottles == 0:
        print("0 bottles of beer on the wall, 0 bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")

def main():
    """
    Prompts the user for the number of bottles and starts the countdown.
    """

    print("Welcome to the 'Bottles of Beer' countdown program!")

    while True:
        try:
            user_input = int(input("How many bottles of beer are on the wall? "))
            if user_input < 0:
                print("Please enter a number greater than or equal to 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    countdown_bottles(user_input)

    print("Thanks for using the 'Bottles of Beer' program!")

if __name__ == "__main__":
    main()
