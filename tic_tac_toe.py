"""
File: tic_tac_toe.py
Author: Kevin Garzón
Assignment: Tic-Tac-Toe W02 Prove: Developer - Solo Code Submission

Purpose: Practice working software by programming.
Practice a version control system
"""

def main():

    # variables and list declaration
    status = "playing"
    moves_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = "X"

    # Print the initial board
    print_interface(moves_list)
    print()

    # Ask for a movement until a player wins or there's a draw
    while status == "playing":

        # Verify if the player X selected an valid square and change it in the board
        if turn == "X":
            move = int(input("X's turn to choose a square (1-9): "))
            if moves_list[move - 1] != "X" and moves_list[move - 1] != "O":
                moves_list[move - 1] = "X"
                turn = "O"
            else:
                print()
                print("You selected an occupied square. Try again")
                turn = "X"
            

        # Verify if the player O selected an valid square and change it in the board
        elif turn == "O":
            move = int(input("O's turn to choose a square (1-9): "))
            if moves_list[move - 1] != "X" and moves_list[move - 1] != "O":
                moves_list[move - 1] = "O"
                turn = "X"
            else:
                print()
                print("You selected an occupied square. Try again")
                turn = "O"

        # Print the board after the movement and check if there is a winner or a draw
        print()
        print_interface(moves_list)
        print()
        status = check_draw(moves_list, status)
        status = check_winner(moves_list, status)
        
    # If there's a winner or a draw, finish the game
    print("Game over. Thanks for playing!")

def print_interface(moves_list):

    print(f"{moves_list[0]} | {moves_list[1]} | {moves_list[2]}")
    print("—————————")
    print(f"{moves_list[3]} | {moves_list[4]} | {moves_list[5]}")
    print("—————————")
    print(f"{moves_list[6]} | {moves_list[7]} | {moves_list[8]}")

def check_winner(moves_list, status):
    winner = 0

    # Horizontal checking
    if moves_list[0] == "X" and moves_list[1] == "X" and moves_list[2] == "X":
        winner = "X"
    elif moves_list[3] == "X" and moves_list[4] == "X" and moves_list[5] == "X":
        winner = "X"
    elif moves_list[6] == "X" and moves_list[7] == "X" and moves_list[8] == "X":
        winner = "X"
    elif moves_list[0] == "O" and moves_list[1] == "O" and moves_list[2] == "O":
        winner = "O"
    elif moves_list[3] == "O" and moves_list[4] == "O" and moves_list[5] == "O":
        winner = "O"
    elif moves_list[6] == "O" and moves_list[7] == "O" and moves_list[8] == "O":
        winner = "O"

    # Vertical checking
    elif moves_list[0] == "X" and moves_list[3] == "X" and moves_list[6] == "X":
        winner = "X"
    elif moves_list[1] == "X" and moves_list[4] == "X" and moves_list[7] == "X":
        winner = "X"
    elif moves_list[2] == "X" and moves_list[5] == "X" and moves_list[8] == "X":
        winner = "X"
    elif moves_list[0] == "O" and moves_list[3] == "O" and moves_list[6] == "O":
        winner = "O"
    elif moves_list[1] == "O" and moves_list[4] == "O" and moves_list[7] == "O":
        winner = "O"
    elif moves_list[2] == "O" and moves_list[5] == "O" and moves_list[8] == "O":
        winner = "O"
    
    # Diagonal checking
    elif moves_list[0] == "X" and moves_list[4] == "X" and moves_list[8] == "X":
        winner = "X"
    elif moves_list[2] == "X" and moves_list[4] == "X" and moves_list[6] == "X":
        winner = "X"
    elif moves_list[0] == "O" and moves_list[4] == "O" and moves_list[8] == "O":
        winner = "O"
    elif moves_list[2] == "O" and moves_list[4] == "O" and moves_list[6] == "O":
        winner = "O"

    # If winner is X or O, change the status to gameover and print a message.
    if winner == "X":
        print("X player wins. Good game.")
        status = "gameover"
    elif winner == "O":
        print("O player wins. Good game.")
        status = "gameover"

    return (status)

def check_draw(moves_list, status):

    # Iterates the list of the board to finds a draw
    for move in moves_list:
        if move != "X" and move != "O":
            status = "playing"
            break
        else:
            status = "draw"
            continue
    return status


if __name__ == "__main__":
    main()