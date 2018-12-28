# hill climbing algorithm for 8-Queen

import random
import copy


class board:

    def __init__(self, initialBoard=None):  # initialBoard must be 2d list
        if (initialBoard == None):
            self.boardvar = [["Empty" for j in range(8)] for i in range(8)]
            for i in range(8):
                # if the random num exist in previos numbers,create another number its the reason i wrote while
                while(True):
                    x = random.randint(0, 7)
                    y = random.randint(0, 7)
                    if(self.boardvar[x][y] == "Empty"):
                        self.boardvar[x][y] = "Queen"
                        break
        else:
            self.setboard(initialBoard)

    def setboard(self, nextboard):
        for i in range(8):
            for j in range(8):
                self.boardvar[i][j] = nextboard[i][j]

    def setindex(self, x, y, value):
        self.boardvar[x][y] = value

    def getboard(self):
        return self.boardvar

    def getindex(self, x, y):
        return self.boardvar[x][y]

    def isGoal(self):
        for i in range(8):
            for j in range(8):
                if (self.boardvar[i][j] == "Queen"):
                    for k in range(8):
                        if (self.boardvar[k][j] == "Queen" and k != i):
                            return False
                        if (self.boardvar[i][k] == "Queen" and k != j):
                            return False
                        if (k < 8 - max(i, j) and k > 0):
                            if (self.boardvar[i + k][j + k] == "Queen"):
                                return False
                        if (k < min(i, j) and k > 0):
                            if (self.boardvar[i - k][j - k] == "Queen"):
                                return False
        return True

    def findNeighbor(self):
        neighbor = []
        for i in range(8):
            for j in range(8):
                if (self.boardvar[i][j] == "Queen"):

                    # move upright Queen 1cell
                    if (i > 0 and j < 7 and self.boardvar[i - 1][j + 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i - 1][j + 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move up Queen 1cell
                    if (i > 0 and self.boardvar[i - 1][j] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i - 1][j] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move upleft Queen 1cell
                    if (i > 0 and j > 0 and self.boardvar[i - 1][j - 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i - 1][j - 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move left Queen 1cell
                    if (j > 0 and self.boardvar[i][j - 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i][j - 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move downleft Queen 1cell
                    if (i < 7 and j > 0 and self.boardvar[i + 1][j - 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i + 1][j - 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move down Queen 1cell
                    if (i < 7 and self.boardvar[i + 1][j] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i + 1][j] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move downright Queen 1cell
                    if (i < 7 and j < 7 and self.boardvar[i + 1][j + 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i + 1][j + 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)

                    # move right Queen 1cell
                    if (j < 7 and self.boardvar[i][j + 1] == "Empty"):
                        boardtmp = copy.deepcopy(self.getboard())
                        boardtmp[i][j + 1] = "Queen"
                        boardtmp[i][j] = "Empty"
                        neighbor.append(boardtmp)
        return neighbor


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
    string = """ qx1 : %d   qy1 : %d  
                 qx2 : %d   qy2 : %d
    """,
    for i in range(8):
        for j in range(8):
            if (boardV[i][j] == "Queen"):
                for k in range(8):
                    if (boardV[k][j] == "Queen" and k != i):
                        cost += 1
                    if (boardV[i][k] == "Queen" and k != j):
                        cost += 1
                    if (k < min(8 - i,8 - j) and k > 0):
                        if (boardV[i + k][j + k] == "Queen"):
                            cost += 1
                    if (k < min(i+1, j+1) and k > 0):
                        if (boardV[i - k][j - k] == "Queen"):
                            cost += 1
                    if (k < min(i+1, 8-j) and k > 0):
                        if (boardV[i - k][j + k] == "Queen"):
                            cost += 1
                    if (k < min(8-i, j+1) and k > 0):
                        if (boardV[i + k][j - k] == "Queen"):
                            cost += 1
    return cost




# search algorithms


def stepAscent(boardv=None):  # if boardv be None then randomly create a board for initial board
    tempboard = board(boardv)  # intial the first board in init board func
    while (True):
        neighbors = tempboard.findNeighbor()
        bestnibr = tempboard.getboard()
        lowestcost = cmpCost(tempboard.getboard())
        while (neighbors.__len__() > 0):
            nibrboard = neighbors.pop()
            nibrcost = cmpCost(nibrboard)
            if (nibrcost < lowestcost):
                bestnibr = nibrboard
                lowestcost = nibrcost
        if (bestnibr == tempboard.getboard()):
            break
        tempboard.setboard(bestnibr)
    return tempboard.getboard()


def stochastic(boardv = None):
    tempboard = board(boardv)
    while (True):
        neighbors = tempboard.findNeighbor()
        bestnibr = tempboard.getboard()
        print(tempboard.getboard())

        lowestcost = cmpCost(tempboard.getboard())
        print(lowestcost)
        while (neighbors.__len__() > 0):
            nibrboard = neighbors.pop()
            nibrcost = cmpCost(nibrboard)
            if (nibrcost < lowestcost):
                bestnibr = nibrboard
                lowestcost = nibrcost
                break
        if (bestnibr == tempboard.getboard()):
            break
        tempboard.setboard(bestnibr)
    return tempboard.getboard()

def randomRestart(iterationNum = None):
    if(iterationNum == None):
        iterationNum = True
    lowestcost = 1000
    bestboard = None
    while(iterationNum):
        tempboard=stepAscent()
        print(tempboard)
        tempCost = cmpCost(tempboard)
        print(tempCost)
        if(tempCost < lowestcost):
            bestboard = tempboard
            lowestcost = tempCost
        if(lowestcost == 0):
            break
        """if(bestboard == None):
            iterationNum +=1
        iterationNum -=1"""
    return bestboard


boardv = randomRestart()
print(boardv)
print(cmpCost(boardv))
"""myboard = board()
print(myboard.getboard())
print(myboard.isGoal())
"""