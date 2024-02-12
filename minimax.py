import copy
import math

Edge = 3

class Tic_Tac_Toe:
  def __init__(self,board_state=[[0 for _ in range(3)] for _ in range(3)],next_move = (-1,-1)):
    self.board_state = board_state
    self.next_move = next_move

  def Game_Terminate(self):
    for i in self.board_state:
      if i == [1 for _ in range(Edge)] or i == [-1 for _ in range(Edge)]:
        return True
    for n in range(Edge):
      temp = []
      for i in self.board_state:
        temp.append(i[n])
      if temp == [1 for _ in range(Edge)] or temp == [-1 for _ in range(Edge)]:
        return True
    temp1 = [self.board_state[0][0],self.board_state[1][1],self.board_state[2][2]]    
    temp2 = [self.board_state[0][2],self.board_state[1][1],self.board_state[2][0]]
    if temp1 == [1 for _ in range(Edge)] or temp1 == [-1 for _ in range(Edge)]:
      return True
    if temp2 == [1 for _ in range(Edge)] or temp2 == [-1 for _ in range(Edge)]:
      return True
    #下满了且没人获胜
    count = 0
    for i in self.board_state:
      for j in i:
        if j!=0:
          count += 1 
    if count == 9: return True
    return False       

  def Score(self):
    player_chess = 1
    opponent_chess = -1
    score = 0
    lines = [
            [[self.board_state[i][j] for j in range(3)] for i in range(3)],
            [[self.board_state[j][i] for j in range(3)] for i in range(3)],
            [[self.board_state[i][i] for i in range(3)]],
            [[self.board_state[i][2 - i] for i in range(3)]]
          ]
    for line_group in lines:
        for line in line_group:
            if line.count(player_chess) == 3:
                score += 10000  # Player forms three in a row: highest score
            elif line.count(player_chess) == 2 and line.count(0) == 1:
                score += 500  # Player forms two in a row (not blocked by opponent): lower high score
            elif line.count(opponent_chess) == 3:
                score = -10000 # Opponent forms three in a row: lowest score
            elif line.count(player_chess) == 2 and line.count(opponent_chess) == 1:
                score += 0 # Player's two in a row are blocked by opponent: lower low score
    return score

  def Possible_Boards(self,player):
    if(player): chess=1
    else: chess=-1
    boards = []
    for i, row in enumerate(self.board_state):
      for j, cell in enumerate(row):
          if cell == 0:
              temp = copy.deepcopy(self.board_state)
              temp[i][j] = chess
              boards.append(Tic_Tac_Toe(temp,(i,j)))
    return boards

def minimax(board: Tic_Tac_Toe, player, depth, alpha, beta):
    # Base case
    if board.Game_Terminate() or depth == 0:
        return board.Score(), board.next_move

    best_move = None

    if player:
        max_score = -math.inf

        for one_board in board.Possible_Boards(player):
            score, _ = minimax(one_board, not player, depth-1, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = one_board.next_move
            alpha = max(alpha, score)  # update alpha value
            if beta <= alpha:  # β cut-off
                break
        return max_score, best_move

    else:
        min_score = math.inf
        for one_board in board.Possible_Boards(player):
            score, _ = minimax(one_board, not player, depth-1, alpha, beta)

            if score < min_score:
                min_score = score
                best_move = one_board.next_move
            beta = min(beta, score)  # update beta value
            if beta <= alpha:  # α cut-off
                break
        return min_score, best_move
    
def minimax_response(board):
   Chessboard = Tic_Tac_Toe(board_state=board)
   _,next_move = minimax(Chessboard,0,9,-math.inf,math.inf)
   return next_move

def Game_Terminater(board):
  Chessboard = Tic_Tac_Toe(board_state=board)
  return Chessboard.Game_Terminate()

def Find_winner(board):
   ChessBoard = Tic_Tac_Toe(board)
   opponent_chess = -1
   player_chess = 1
   lines = [
          [[ChessBoard.board_state[i][j] for j in range(3)] for i in range(3)],
          [[ChessBoard.board_state[j][i] for j in range(3)] for i in range(3)],
          [[ChessBoard.board_state[i][i] for i in range(3)]],
          [[ChessBoard.board_state[i][2 - i] for i in range(3)]]
        ]
   for line_group in lines:
        for line in line_group:
              if line.count(opponent_chess) == 3:
                  return -1
              elif line.count(player_chess) == 3:
                  return 1
   return 0