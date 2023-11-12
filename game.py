"""
Charlie Ho
A01358146
"""
import random


def create_character():
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # check if users want to change their mind
    while proceed != 'Y':
        proceed = input("Is this correct? (Y/N) ").upper()
    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "Name": character_name}
    return player


def game_difficulty():
    while True:
        difficulty = input("Life is hard, how hard you want this adventure to be on a scale "
                           "from 1 (easiest) to 3 (difficult)? ")
        try:
            float(difficulty)
        except ValueError:
            print("Oh, you can't even type numbers?!")  # if user input is not a number
        else:
            if float(difficulty) not in [1, 2, 3]:  # if user input is not an integer
                print("Please enter an integer.")
                continue
            else:
                print("Great! I like your choice.")
                return difficulty


def make_board():
    rows = 5
    columns = 5
    list_of_locations = ('school', 'interview', 'library', 'hackathon')  # may add more locations
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row,column)] = random.choice(list_of_locations)
    return board


def game():
    # create_character()
    # game_difficulty()
    # make_board()
    make_board()


def main():
    """
    Execute the game function.
    """
    print('-' * 80)
    print("\t \t Welcome!")
    print('-' * 80)
    game()


if __name__ == '__main__':
    main()
