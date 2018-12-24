#hill climbing algorithm for 8-Queen

import random
import copy

class board:

    def __init__(self,initialBoard = None):#initialBoard must be 2d list
        if(initialBoard == None):
            self.boardvar = [["Empty" for j in range(8)] for i in range(8)]
            print(self.boardvar)
            for i in range(8):
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                self.boardvar[x][y] = "Queen"
        else:
            self.setboard(initialBoard)


    def setboard(self,nextboard):
        for i in range(8):
            for j in range(8):
                self.boardvar[i][j] = nextboard[i][j]


    def setindex(self,x,y,value):
        self.boardvar[x][y] = value

    def getindex(self,x,y):
        return self.boardvar[x][y]

    def isGoal(self):
        for i in range(8):
            for j in range(8):
                if(self.boardvar[i][j] == "Queen"):
                    for k in range(8):
                        if(self.boardvar[k][j] == "Queen" and k != i):
                            return False
                        if(self.boardvar[i][k] == "Queen" and k != j):
                            return False
                        if(k < 8-max(i,j) and k>0):
                            if(self.boardvar[i+k][j+k] == "Queen"):
                                return False
                        if(k < min(i,j) and k>0):
                            if (self.boardvar[i - k][j - k] == "Queen"):
                                return False
        return True

    def findNeighbor(self):
        lowestCost = cmpCost(self.boardvar)
        bestBoard = self.boardvar
        neighbor = []
        for i in range(8):
            for j in range(8):
                if (self.boardvar[i][j] == "Queen"):
                    #move up Queen 1cell
                    if(i>0 and self.boardvar[i-1][j] == "Empty"):
                        boardtmp = copy.deepcopy(self.boardvar)
                        boardtmp[i-1][j] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)
                        #if(cmpCost(boardtmp) < lowestCost):

                    # move upright Queen 1cell
                    if (i > 0 and j<7 and self.boardvar[i - 1][j + 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.boardvar)
                        boardtmp[i - 1][j + 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                    # move up Queen 1cell
                    if (i > 0 and self.boardvar[i - 1][j] == "Empty"):
                        boardtmp = copy.deepcopy(self.boardvar)
                        boardtmp[i - 1][j] = "Queen"
                        boardtmp[i][j] = "Empty"



"""
    def cmpCost(self):
        cost = 0
        for i in range(8):
            for j in range(8):
                if(self.boardvar[i][j] == "Queen"):
                    for k in range(8):
                        if(self.boardvar[k][j] == "Queen" and k != i):
                            return cost+=1
                        if(self.boardvar[i][k] == "Queen" and k != j):
                            return cost+=1
                        if(k < 8-max(i,j) and k>0):
                            if(self.boardvar[i+k][j+k] == "Queen"):
                                return cost+=1
                        if(k < min(i,j) and k>0):
                            if (self.boardvar[i - k][j - k] == "Queen"):
                                return cost+=1
        return cost
"""


"""
    def isQueenBetween2Point(self,Qx1,Qy1,Qx2,Qy2):
        if(Qx1 == Qx2)#2Queen are in the same column
            
"""

def cmpCost(boardV):
    cost = 0
    for i in range(8):
        for j in range(8):
            if (boardV[i][j] == "Queen"):
                for k in range(8):
                    if (boardV[k][j] == "Queen" and k != i):
                        cost += 1
                    if (boardV[i][k] == "Queen" and k != j):
                        cost += 1
                    if (k < 8 - max(i, j) and k > 0):
                        if (boardV[i + k][j + k] == "Queen"):
                            cost += 1
                    if (k < min(i, j) and k > 0):
                        if (boardV[i - k][j - k] == "Queen"):
                            cost += 1
    return cost

myboard = board()
print(myboard.boardvar)
print(myboard.isGoal())