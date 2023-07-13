import Working

np_board= Working.extracted
board=[[0]*9]*9

#Creating List Object
for i in range(len(np_board[0])):
     for j in range(len(np_board[0])):
          board[i][j]=int(np_board[i][j])

print("---Sudoku Extracted by the API---")
Working.print_board(board)
print("")


def solver(bo):
     #The base case for the recursive function would be that our sudoku board is full, means no remaining zero elements.
     find= Working.find_empty(bo) 
     if find==None:
          return True
          #Means no zero elements exist
     else:
          row, colm=find
     
     for i in range(1,10):
          if Working.valid(bo, i, (row,colm)):
               bo[row][colm]=i
               
               if solver(bo):
                    return True
               bo[row][colm]=0
     
     return False

solver(board)
print("---Our Sudoku Solution---")
Working.print_board(board)


    





               