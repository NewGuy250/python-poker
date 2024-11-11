import random

# Player's turn
def my_turn():
    return True

def persuade_to_all_in():
    persuading_messages = [
        "I think you made a typo... all in!",
        "Imagine if you won with this hand!",
        "Don't be a wuss!",
        "The universe wants you to go all in... do it for the memes!",
        "If you don’t go all in, you’re leaving money on the table!",
        "You’ve got this... ALL IN!",
        "Risk it for the biscuit, ALL IN!",
        "This is the moment. Go all in and become a legend!"
    ]
    return random.choice(persuading_messages)

# Main game function to simulate the player's action
def main():
    if my_turn():
        while True:
            # Ask the player for an action
            action = input("It's your turn! What would you like to do? (fold, call, all in): ").lower()

            # Handle all in
            if action == "all in":
                print("You decided to go all in!")
                return "all in"
            
            # If the player didn't go all in, make them.
            print(persuade_to_all_in())

# Run the game
if __name__ == "__main__":
    main()
