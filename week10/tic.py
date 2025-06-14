def print_board(cells):
    # Print the current board layout
    print("\n")
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("\n")

def check_winner(cells, mark):
    # Define all winning triplets (rows, columns, diagonals)
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    # Return True if any winning triplet is occupied by the same mark
    return any(cells[a] == cells[b] == cells[c] == mark for a, b, c in wins)

def is_draw(cells):
    # Return True if all cells are filled with X or O
    return all(cell in ['X', 'O'] for cell in cells)

def main():
    # Read player names (defaulting if left blank)
    p1 = input("Enter name for Player 1 (X): ").strip() or "Player1"
    p2 = input("Enter name for Player 2 (O): ").strip() or "Player2"
    players = [(p1, 'X'), (p2, 'O')]

    # Initialize cells labeled 1–9
    cells = [str(i) for i in range(1, 10)]
    turn = 0  # 0 ⇒ Player 1's turn; 1 ⇒ Player 2's turn

    while True:
        name, mark = players[turn]
        print_board(cells)

        # Prompt for move choice
        choice = input(f"{name} ({mark}), choose a cell (1-9): ")
        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        idx = int(choice) - 1
        if cells[idx] in ['X', 'O']:
            print("That cell is already occupied. Please choose another one.")
            continue

        # Place the mark on the chosen cell
        cells[idx] = mark

        # Check for a win
        if check_winner(cells, mark):
            print_board(cells)
            print(f" Congratulations {name} ({mark})! You win!")
            break

        # Check for a draw
        if is_draw(cells):
            print_board(cells)
            print("It's a draw!")
            break

        # Switch turns
        turn = 1 - turn

if __name__ == "__main__":
    main()