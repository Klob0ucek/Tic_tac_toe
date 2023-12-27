from typing import List, Tuple


Grid = List[List[str]]


def draw(grid: Grid) -> None:
    hight: int = 0
    for col in grid:
        if len(col) > hight:
            hight = len(col)
    for i in range(hight):
        for col in grid:
            print("+---", end = "")
        print("+")

        for row in grid:
            if len(row) >= hight:

# COLOR

                print("|", end = "")
                if row[hight - 1] == "X":
                    print('\x1b[6;30;42m' + " " + row[hight - 1] + " ",end = "" + '\x1b[0m')
                else:
                    print('\x1b[7;31;42m' + " " + row[hight - 1] + " ",end = "" + '\x1b[0m')

# COLOR

            else:
                print("|   ", end = "")
        print("|")
        hight -= 1
    for col in grid:
        print("+---", end = "")
    print("+")

    for i in range(len(grid) - 1):
        print("  " + str(i) + " ", end = "")
    print("  " + str(len(grid) - 1))


def check_win(grid: Grid, player: str, pos: Tuple[int, int]) -> bool:
    in_row: int = 0
    max_in_row: int = 0
    col, row = pos

    # check win in column
    if len(grid[col]) >= 4:
        for token in grid[col]:
            if token == player:
                in_row += 1
            else:
                in_row = 0
    if in_row == 4:
        return True
    in_row = 0

    # check win in row
    max_in_row = 0
    for cols in grid:
        if len(cols) >= row + 1:
            if cols[row] == player:
                in_row += 1
                if max_in_row < in_row:
                    max_in_row = in_row
            else:
                in_row = 0
        else:
            in_row = 0
    if in_row == 4 or max_in_row == 4:
        return True
    in_row = 0

    # check win on up diagonal | / |
    max_in_row = 0
    start_col: int = col - row
    start_row: int = 0
    if start_col < 0:
        start_row = abs(start_col)
        start_col = 0

    while start_col < len(grid):
        if (len(grid[start_col]) < start_row + 1):
            in_row = 0
            start_col += 1
            start_row += 1
            continue
        if grid[start_col][start_row] == player:
            in_row += 1
            if max_in_row < in_row:
                max_in_row = in_row
        else:
            in_row = 0
        start_col += 1
        start_row += 1
    if max_in_row == 4:
        return True
    in_row = 0

    # check win on down diagonal | \ |
    max_in_row = 0
    start_col = col + row
    start_row = 0
    if start_col >= len(grid):
        start_row = abs(len(grid) - 1 - start_col)
        start_col = len(grid) - 1

    while (start_col >= 0):
        if (len(grid[start_col]) < start_row + 1):
            in_row = 0
            start_col -= 1
            start_row += 1
            continue
        if grid[start_col][start_row] == player:
            in_row += 1
            if max_in_row < in_row:
                max_in_row = in_row
        else:
            in_row = 0
        start_col -= 1
        start_row += 1
    if max_in_row == 4:
        return True
    in_row = 0

    return False


def play(grid: Grid, player: str, column: int) -> bool:
    grid[column].append(player)

    col: int = column
    row: int = len(grid[column]) - 1
    return check_win(grid, player, (col, row))


def main() -> None:
    pass

def run_game(size: int) -> None:
    player = 'O'
    grid: Grid = [[] for _ in range(size)]
    draw(grid)
    over = False
    while not over:
        player = 'X' if player == 'O' else 'O'
        column = input("\nPlayer " + player + ": ")

        if column == "" or column.isalpha() or int(column) >= size:
            print("Invalid input. Try Again: ")
            player = 'X' if player == 'O' else 'O'
            continue

        print()
        column = int(column)
        over = play(grid, player, column)
        draw(grid)
    print("\nGame over, player", player, "won.")


if __name__ == '__main__':
    main()
    run_game(9)

