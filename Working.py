import API_Sudoku_Generator

extracted= API_Sudoku_Generator.grid

def find_empty(bo): #Here, we are denoting empty by zero.
     for i in range(len(bo)):
          for j in range(len(bo[0])):
               if bo[i][j]==0:
                    return (i,j) #Rows and Columns
     return None
               
#Step-1
#Checking that the value we entered in the board is valid or not.
def valid(bo, num, pos): #We are passing the board itself, the number and their position(i,j).
     
     #Checking the rwo first.
     for c in range(len(bo[0])):
          if bo[pos[0]][c]==num and pos[1]!=c: #bo[pos[0]][c] means as the pos is passed as a pair of (i,j), pos[0] means i-> that is row of our
               return False                    #newly inserted element, we are required to check the validity of the sudoku after each element is inserted
                                               #thus, bo[pos[0]][c], here, c-represents each column traversal, bol[pos[0]], represents our respective column.
                                               #We are also checking pos[1], that is j in (i, j), as obviously the recently entered element num would be present 
                                               #in the sudoku.
     
     #Checking the columns
     for c in range(len(bo[0])):
          if bo[c][pos[1]]==num and pos[0]!=c:
               return False
     
     #Now, we need to check the validity in a respective square box, to do that first we have to figure out in which box we are in rightnow.
     #So, to do that first check the position of the num-element, thus, read it's x and y position.
     box_x= pos[0] //3
     box_y= pos[1] //3 #In floor division the resultant is rounded off to it's nearest integer, and as even for decimal three can only have 
                       #3-values in this case-{0,1,2}, 0 means first box's row,1 means second box's row and 2 means third box's row
                       #same logic for column.
     for i in range(box_y*3,box_y*3+3):
          for j in range(box_x*3, box_x*3+3): #Try a few indexes and values to understand why we are doing this to check, the whole square.
               if bo[i][j]==num and (i,j)!=pos:
                    return False
     
     return True
                
def print_board(bo):
     for i in range(len(bo)):
          if i%3==0 and i!=0:
               print('------------------')
          for j in range(len(bo[0])):
               if j%3==0 and j!=0:
                    print("|", end="") #This end="" simply removes the '\n', so that we don't go to the  next line.
               if j==8:
                    print(bo[i][j])
               else:
                    print(str(bo[i][j])+" ",end="")
