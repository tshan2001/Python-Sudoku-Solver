"""
This program uses Recursive-Backtracking algorithm to solve any 9*9 sudoku

Implementation:        Recursive-Backtracking
Completed Functions:   1. Allow users to input the sudoku
                       2. Solve the sudoku and print it

User Interface:        Python Console

Developer:             Tianze Shan
                       Boston University Computer Science Class of 2023
                       (717)-339-8026
                       tshan@bu.edu
"""

class Sudoku:
    def __init__(self, grid1):
        self.grid = grid1
        self.colHasVal = [[False]*10 for _ in range(9)]
        self.rowHasVal = [[False]*10 for _ in range(9)]
        self.subgridHasVal = [[[False]*10 for i in range(3)] for x in range(3)]
        self.valIsFixed = [[False]*9 for _ in range(9)]
        self.readIn()
        
    
    def __repr__(self):
        a = ''
        for i in self.grid:
            a += str(i)
            a += '\n'
        return a        
    
    def placeVal(self, val, row, col):
        self.grid[row][col] = val
        self.colHasVal[col][val] = True
        self.rowHasVal[row][val] = True
        self.subgridHasVal[row//3][col//3][val] = True
        
    def removeVal(self, val, row, col):
        self.grid[row][col] = 0
        self.colHasVal[col][val] = False
        self.rowHasVal[row][val] = False
        self.subgridHasVal[row//3][col//3][val] = False

    def readIn(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.placeVal(self.grid[i][j], i, j)
                    self.valIsFixed[i][j] = True

    def safe(self, val, row, col):
        if (self.valIsFixed[row][col] == False) and \
            (self.subgridHasVal[row//3][col//3][val] == False) and \
                (self.colHasVal[col][val] == False) and (self.rowHasVal[row][val] == False):
                    return True
        return False        
    
    def solveSudoku(self, x):
        if x > 80:
            return True
        row = x // 9
        col = x % 9
        if self.valIsFixed[row][col]:
            self.subgridHasVal[row//3][col//3][self.grid[row][col]] = True
            self.colHasVal[col][self.grid[row][col]] = True
            self.rowHasVal[row][self.grid[row][col]] = True
            return self.solveSudoku(x + 1)
        
        for i in [1,2,3,4,5,6,7,8,9]:
            if self.safe(i, row, col):
                self.placeVal(i, row, col)
                if self.solveSudoku(x+1):
                    return True
                self.removeVal(i, row, col)
        return False
    
    def solve(self):
        return self.solveSudoku(0)
    
def main():
    a = [[0,0,0,0,0,9,5,7,0],\
         [7,0,0,0,3,5,0,9,4],\
         [0,0,0,4,0,0,0,0,3],\
         [8,0,0,1,0,0,6,0,0],\
         [0,0,0,0,6,0,0,0,0],\
         [0,0,9,0,0,7,0,0,5],\
         [4,0,0,0,0,6,0,0,0],\
         [9,7,0,2,4,0,0,0,8],\
         [0,8,5,7,0,0,0,0,0]]
    Solution = Sudoku(a)
    Solution.solveSudoku(0)
    print(Solution)
    
    
    
    
    
    
