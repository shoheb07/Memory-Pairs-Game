import random
import time

def create_board(size):
    pairs = list(range(1, (size * size // 2) + 1)) * 2
    random.shuffle(pairs)
    return [pairs[i:i + size] for i in range(size)]

def display_board(board, revealed):
    size = len(board)
    print("\nBoard:")
    for i in range(size):
        for j in range(size):
            if revealed[i][j]:
                print(f"{board[i][j]:2}", end=" ")
            else:
                print(" X", end=" ")
        print()

def get_input(size):
    while True:
        try:
            row = int(input("Enter row (0-based): "))
            col = int(input("Enter column (0-based): "))
            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Enter valid numbers.")

def check_win(revealed):
    return all(all(row) for row in revealed)

def play_game(size=4):
    board = create_board(size)
    revealed = [[False]*size for _ in range(size)]
    moves = 0

    while not check_win(revealed):
        display_board(board, revealed)

        print("\nSelect first card")
        r1, c1 = get_input(size)
        revealed[r1][c1] = True
        display_board(board, revealed)

        print("\nSelect second card")
        r2, c2 = get_input(size)
        revealed[r2][c2] = True
        display_board(board, revealed)

        moves += 1

        if board[r1][c1] != board[r2][c2]:
            print("\n❌ Not a match!")
            time.sleep(1)
            revealed[r1][c1] = False
            revealed[r2][c2] = False
        else:
            print("\n✅ Match found!")

    print(f"\n🎉 You won in {moves} moves!")

if __name__ == "__main__":
    play_game()
