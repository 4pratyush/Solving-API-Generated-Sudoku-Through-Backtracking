import Working

np_board= Working.extracted

bow=[[0]*9]*9
#Creating List Object
for i in range(0,9):
     bow[i]=np_board[i].tolist()
board=bow

def solver(bo):
     #The base case for the recursive function would be that our sudoku board is full, means no remaining zero elements.
     find= Working.find_empty(bo) 
     if find==None:
          Working.print_board(bo)
          return True #Means no zero elements exist
     else:
          row, colm=find
     
     for i in range(1,10):
          if Working.valid(bo, i, (row,colm)):
               bo[row][colm]=i
               if solver(bo):
                    return True
               bo[row][colm]=0     
     return False
print("---API Extracted Sudoku Board---")
Working.print_board(board)
print("")
print("---Our Solved Sudoku---")
solver(board)



    





               