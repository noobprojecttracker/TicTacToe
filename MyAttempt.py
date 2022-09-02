import random

spots = {
    1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
}
available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
removed_spots = []

Turns = 0
Letter = ''

def play_again():
    want_to_play = input("Do you want to play again?:\n (a) yes\n (b) no: ")
    if want_to_play == "a":
        return True
    else:
        return False

def print_board(spots):
    board = (
        f'|{spots[1]}||{spots[2]}||{spots[3]}|\n'
        f'|{spots[4]}||{spots[5]}||{spots[6]}|\n'
        f'|{spots[7]}||{spots[8]}||{spots[9]}|'
             )
    print(board)

def check_winner(spots):
    if spots[1] == spots[2] == spots[3]:
        return True
    elif spots[4] == spots[5] == spots[6]:
        return True
    elif spots[7] == spots[8] == spots[9]:
        return True
    elif spots[1] == spots[4] == spots[7]:
        return True
    elif spots[3] == spots[6] == spots[9]:
        return True
    elif spots[1] == spots[5] == spots[9]:
        return True
    elif spots[3] == spots[5] == spots[7]:
        return True
    else:
        return False

winner = False

while winner == False:
    print_board(spots)
    if available_spots == [] and check_winner(spots) == False:
        print("It's a draw!")
    if check_winner(spots) == True:
        Turns -= 1
        print(Letter, 'won!')
        if play_again() == True:
            spots = {
                1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
            }
            Turns = 0
            available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            removed_spots = []
            print_board(spots)
        else:
            print("Ok. Enjoy your day.")
            break
    if Turns % 2 == 0:
        Letter = 'X'
    else:
        Letter = 'O'
    if check_winner(spots) == False:
        try:
            user_input = int(input('\nenter choice: '))
            if user_input in available_spots:
                available_spots.remove(user_input)
                removed_spots.append(user_input)
                spots[user_input] = Letter
                Turns += 1
            elif user_input in removed_spots:
                print('A user is  already here. Try a different spot...')
                Turns == Turns
            elif (user_input not in removed_spots) and (user_input not in available_spots):
                print("This spot does not exist. Try again")
                Turns == Turns
        except ValueError:
            print('Input must be an available spot. Try again!')
            Turns == Turns
            if play_again() == True:
                spots = {
                    1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
                }
                Turns = 0
                available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                removed_spots = []
                print_board(spots)
            else:
                print("Ok. Enjoy your day.")
                break

