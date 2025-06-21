import random

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
    # Define all winning triplets
    wins = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    return any(cells[a] == cells[b] == cells[c] == mark for a, b, c in wins)

def is_draw(cells):
    return all(cell in ['X', 'O'] for cell in cells)

def get_ai_move(cells, ai_mark, player_mark):
    # Minimax-based unbeatable AI
    def minimax(cells, is_maximizing):
        if check_winner(cells, ai_mark):
            return 1
        elif check_winner(cells, player_mark):
            return -1
        elif is_draw(cells):
            return 0

        scores = []
        for i in range(9):
            if cells[i] not in ['X', 'O']:
                cells[i] = ai_mark if is_maximizing else player_mark
                score = minimax(cells, not is_maximizing)
                scores.append((score, i))
                cells[i] = str(i + 1)

        return max(scores)[0] if is_maximizing else min(scores)[0]

    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if cells[i] not in ['X', 'O']:
            cells[i] = ai_mark
            score = minimax(cells, False)
            cells[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def main():
    # Ask for game mode
    mode = input("Choose mode: 1 - PvP (2 Players), 2 - PvE (vs AI): ").strip()
    if mode == "2":
        p1 = input("Enter your name (X): ").strip() or "Player"
        p2 = "Computer"
        players = [(p1, 'X'), (p2, 'O')]
        ai_enabled = True
    else:
        p1 = input("Enter name for Player 1 (X): ").strip() or "Player1"
        p2 = input("Enter name for Player 2 (O): ").strip() or "Player2"
        players = [(p1, 'X'), (p2, 'O')]
        ai_enabled = False

    cells = [str(i) for i in range(1, 10)]
    turn = 0

    while True:
        name, mark = players[turn]
        print_board(cells)

        if ai_enabled and name == "Computer":
            print("Computer is thinking...")
            idx = get_ai_move(cells, 'O', 'X')
        else:
            choice = input(f"{name} ({mark}), choose a cell (1-9): ")
            if not choice.isdigit() or int(choice) not in range(1, 10):
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            idx = int(choice) - 1
            if cells[idx] in ['X', 'O']:
                print("That cell is already occupied. Please choose another one.")
                continue

        cells[idx] = mark

        if check_winner(cells, mark):
            print_board(cells)
            print(f"🎉 Congratulations {name} ({mark})! You win!")
            break

        if is_draw(cells):
            print_board(cells)
            print("It's a draw!")
            break

        turn = 1 - turn

if __name__ == "__main__":
    main()