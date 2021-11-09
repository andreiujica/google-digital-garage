# Tic Tac Toe - Andrei Ujica - Atelierul Digital pentru Programatori
# Noiembrie 2021

# X este jucatorul
# O este calculatorul


def create_grid():
    return ["-" for square in range(9)]


def print_grid(grid):
    for square in range(9):
        print(grid[square], end=" ")
        if (square + 1) % 3 == 0:
            print()
    print()


def player_choice(grid):
    player_square = int(input("Introduceti numarul aferent casutei dorite: ")) - 1

    while grid[player_square] != "-":
        print("Casuta deja ocupata. Alegeti alta casuta.\n")
        player_square = int(input("Introduceti numarul aferent casutei dorite: ")) - 1

    grid[player_square] = "X"


def computer_choice(grid):
    choice_rankings = {
        "first": [4],
        "second": [0, 2, 6, 8],
        "third": [1, 3, 5, 7]
    }

    for rank, squares in choice_rankings.items():
        for square in squares:
            if grid[square] == "-":
                grid[square] = "O"
                print(f"Computerul a ales casuta {square}")
                return


def check_win(grid):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]

    for combination in win_combinations:
        if grid[combination[0]] == grid[combination[1]] == grid[combination[2]] == "X":
            print("Player wins!")
            return True
        elif grid[combination[0]] == grid[combination[1]] == grid[combination[2]] == "O":
            print("Computer wins!")
            return True

    return False


def check_draw(grid):
    for square in grid:
        if square != "-":
            continue
        else:
            return False

    print("It is a draw.")
    return True


def main():
    print("1 2 3\n4 5 6\n7 8 9")
    grid = create_grid()
    win_state = False
    draw_state = False

    while win_state == False and draw_state == False:
        player_choice(grid)
        computer_choice(grid)

        print_grid(grid)

        win_state = check_win(grid)
        draw_state = check_draw(grid)


if __name__ == "__main__":
    main()
