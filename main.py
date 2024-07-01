from minesweeper import Minesweeper
from minesweeper_ai import MinesweeperAI

def play_game(rows, cols, num_mines):
    game = Minesweeper(rows, cols, num_mines)
    ai = MinesweeperAI(game)

    game_over = False
    while not game_over and not game.is_solved():
        game.display()
        print()
        game_over = ai.make_move()

    if game.is_solved():
        print("AI wins!")
    else:
        print("AI hit a mine!")
    game.display()

if __name__ == "__main__":
    play_game(10, 10, 10)
