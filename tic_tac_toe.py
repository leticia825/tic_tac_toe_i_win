"""This module implement a console interactive 2 player Tic-Tac-Toe game.
"""
game_on = True
a_turn = 1
chosen_loc = (0, 0)

loc = {(1, 1): "   ", (1, 2): "   ", (1, 3): "   ",
       (2, 1): "   ", (2, 2): "   ", (2, 3): "   ",
       (3, 1): "   ", (3, 2): "   ", (3, 3): "   "}


def board():
    print("   1   2   3")
    print("1 " + loc[(1, 1)] + "|" + loc[(1, 2)] + "|" + loc[(1, 3)])
    print("   --+---+--")
    print("2 " + loc[(2, 1)] + "|" + loc[(2, 2)] + "|" + loc[(2, 3)])
    print("   --+---+--")
    print("3 " + loc[(3, 1)] + "|" + loc[(3, 2)] + "|" + loc[(3, 3)])


def next_turn(turn):
    global a_turn
    a_turn = 3 - turn


def read_move():
    global chosen_loc
    global a_turn

    if a_turn == 1:
        chosen_loc = tuple(map(int, input("Enter X move (row,column no spaces)> ").split(',')))
    if a_turn == 2:
        chosen_loc = tuple(map(int, input("Enter O move (row,column no spaces)> ").split(',')))
    validate_move()


def validate_move():
    global chosen_loc
    global loc
    global a_turn

    if chosen_loc in loc and loc[chosen_loc] == "   ":
        if a_turn == 1:
            loc[chosen_loc] = " X "
        else:
            loc[chosen_loc] = " O "

        next_turn(a_turn)
    else:
        print("Invalid move, try again.")
        read_move()


def winning_move():
    global game_on

    if (loc[(1, 1)] == loc[(1, 2)] == loc[(1, 3)] != "   " or
            loc[(2, 1)] == loc[(2, 2)] == loc[(2, 3)] != "   " or
            loc[(3, 1)] == loc[(3, 2)] == loc[(3, 3)] != "   " or
            loc[(1, 1)] == loc[(2, 1)] == loc[(3, 1)] != "   " or
            loc[(1, 2)] == loc[(2, 2)] == loc[(3, 2)] != "   " or
            loc[(1, 3)] == loc[(2, 3)] == loc[(3, 3)] != "   " or
            loc[(2, 1)] == loc[(2, 2)] == loc[(2, 3)] != "   " or
            loc[(1, 1)] == loc[(2, 2)] == loc[(3, 3)] != "   " or
            loc[(1, 3)] == loc[(2, 2)] == loc[(3, 1)] != "   " or
            loc[(2, 1)] == loc[(2, 2)] == loc[(2, 3)] != "   "):
        declare_winner()
        game_on = False
    else:
        tying_move()


def tying_move():
    if "   " not in loc.values():
        declare_tie()


def declare_winner():
    global a_turn

    if a_turn == 1:
        board()
        print()
        print()
        print("O is the winner!")
    else:
        board()
        print()
        print()
        print("X is the winner!")


def declare_tie():
    global game_on

    board()
    print()
    print()
    print("Looks like a stalemate!")
    game_on = False


def main():
    while game_on:
        board()
        read_move()
        winning_move()


if __name__ == "__main__":
    main()
