from typing import List, Tuple, Optional

Positions = (2, 0), (2, 1), (2, 2), \
            (1, 0), (1, 1), (1, 2), \
            (0, 0), (0, 1), (0, 2)

# quit during game doesnt work

class TicTacToe:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.moves = 0

    def get_player(self) -> str:
        if self.moves % 2 == 0:
            return "X"
        return "O"

    def get_input(self) -> str:
        result = input(f"It's {self.get_player()}'s turn: ")
        if result.isdecimal() and 0 < int(result) < 10:
            return result
        if result.upper() == "Q":
            return "q" #method end
        else:
            print("Incorrect input. Try again or press Q to quit the game!")
            return self.get_input()
    
    def is_valid(self, col: int, row: int) -> bool:
        if self.board[col][row] == " ":
            return True
        return False

    def uncover(self) -> Optional[str]:
        input = self.get_input()
        if input == "q":
            return "q"
        col, row = Positions[int(input) - 1]
        if self.is_valid(col, row):
            self.board[col][row] = self.get_player()
            self.moves += 1
        else:
            print(f"This squere is already occupied by {self.board[col][row]}. Try again.")
            self.uncover()
        return

    def show(self) -> None:
        for row in range(3):
            print(f" {self.board[row][0]} | {self.board[row][1]} | {self.board[row][2]}")
            if row < 2:
                print("-" * 11)
        return
    
    def check_win(self) -> Optional[str]:
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][1]

        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[1][i]
        
        # check diagonals
        for i in [1, -2]:
            if self.board[i - 1][i - 1] == self.board[i][i] == self.board[i+1][i + 1] != " ":
                return self.board[i][i]
        return None

    def end(self, winner: Optional[str]):
        if winner == "q":
            print("Game quitted")
        elif  winner is not None:
            print(f"The Winner is {winner}")
        else:
            print("It's Draw")
        return

def play() -> None:
    game = TicTacToe()
    while True:
        game.show()
        winner = game.uncover() 
        if winner is None:
            winner = game.check_win()
        if winner is not None:
            game.show()
            game.end(winner)
            return
        if game.moves == 9:
            game.show()
            game.end(None)
            return
    assert False


def main():
    play()


if __name__ == '__main__':
    main()