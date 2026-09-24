
def print_board(values):
   print("\n")
   print(f"\t {values[0]} | {values[1]} | {values[2]}")
   print("\t---|---|---")
   print(f"\t {values[3]} | {values[4]} | {values[5]}")
   print("\t---|---|---")
   print(f"\t {values[6]} | {values[7]} | {values[8]}")
   print("\n")


def check_win(values, player):
   win_combos = [
       [0,1,2], [3,4,5], [6,7,8], # rows
       [0,3,6], [1,4,7], [2,5,8], # columns
       [0,4,8], [2,4,6] # diagonals
   ]
   return any(all(values[i] == player for i in combo) for combo in win_combos)


def tic_tac_toe():
   board = [" "] * 9
   current_player = "X"
   for turn in range(9):
       print_board(board)
       move = input(f"Player {current_player}, choose position (1-9): ")
       if not move.isdigit() or int(move) not in range(1,10):
           print("Invalid input! Try again.")
           continue
       pos = int(move) - 1
       if board[pos] != " ":
           print("Position already taken! Try again.")
           continue
       board[pos] = current_player
       if check_win(board, current_player):
           print_board(board)
           print(f"🎉 Player {current_player} wins!")
           return
       current_player = "O" if current_player == "X" else "X"
   print_board(board)
   print("It's a tie!")

   
if __name__ == "__main__":
   tic_tac_toe()