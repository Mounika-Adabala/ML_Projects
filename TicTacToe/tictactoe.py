def constboard(board): # displays current state of the board
  print("Current State of the board: \n\n");
  # 0 -> _
  # -1 -> X
  # 1 -> O
  for i in range(0, 9):
    if((i > 0) and (i % 3 == 0)):
      print("\n");
    if(board[i] == 0):
      print("_", end=" ");
    if(board[i] == -1):
      print("X", end=" ");
    if(board[i] == 1):
      print("O", end=" ");
  print("\n\n");

#---------------------------------------------------
# game b/w users
def user1turn(board):
  pos = input("Enter X's pos from [1,2,...,9]");
  pos = int(pos)
  if(board[pos-1]!=0):
    print("Wrong Move!!!");
    exit(0);
  board[pos-1]=-1;

def user2turn(board):
  pos = input("Enter O's pos from [1,2,...,9]");
  pos = int(pos)
  if(board[pos-1]!=0):
    print("Wrong Move!!!");
    exit(0);
  board[pos-1]=1;
# -------------------------------------------------

def minmax(board, player):
  x = analyze(board);
  if(x!=0):
    return (x*player);
  pos = -1;
  value = -2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=player;
      score=-minmax(board, -1*player);
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
  if(pos==-1):
    return 0;
  return value;

def compturn(board):
  pos = -1;
  value = -2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=1;
      score=-minmax(board, -1);
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
  board[pos]=1;


def analyze(board):
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][0]]
    return 0



def main():
  choice = int(input("Enter 1 for single player,2 for multiplayer: "));
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice == 1):
    print("Computer: O vs  You: X");
    player = int(input("Enter to play (1)st or (2)nd: "));
    for i in range(0, 9):
      if(analyze(board)!=0):
        break;
      if((i + player) % 2 == 0):
        compturn(board);
      else:
        constboard(board); #showcase the board
        user1turn(board); #user input on board
  else: #game b/w two players
    for i in range(0, 9):
      if(analyze(board)!=0):
        break;
      if(i % 2 == 0):
        constboard(board); #showcase the board
        user1turn(board); #user1 input on board
      else:
        constboard(board); #showcase the board
        user2turn(board); #user2 input on board
  x = analyze(board);
  if(x == 0):
    constboard(board);
    print("Draw!");
  if(x == -1):
    constboard(board);
    print("Player X wins!!..Player  O looses!!");
  if(x == 1):
    constboard(board);
    print("Player O wins!!..Player  X looses!!");
