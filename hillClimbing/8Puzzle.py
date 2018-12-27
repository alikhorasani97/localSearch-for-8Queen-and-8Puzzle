#8Puzzle impelementation

import  random
import  copy

class problem:

    def __init__(self,initialState):
        if (initialState == None):
            tempstate = [i for i in range(9)]
            random.shuffle(tempstate)
            self.statevar = [[tempstate[i*3 + j] for j in range(3)] for i in range(3)]
        else:
            self.setState(initialBoard)

    def setState(self,statev):
        self.statevar = [[statev[i * 3 + j] for j in range(3)] for i in range(3)]

    def getstate(self):
        return self.statevar

    def getsuccessors(self):
        neighbors = []
        for i in range(9):
            temprow = (int)(i/3)
            tempcol = i%3
            if(self.statevar[temprow][tempcol] == 0)
                #move right
                if(tempcol <2):
                    tempstate = copy.deepcopy(self.getstate())
                    tempstate[temprow][tempcol] = tempstate[temprow][tempcol+1]
                    tempstate[temprow][tempcol+1] = 0
                    neighbors.append(tempstate)
                #move down
                if(temprow <2):
                    tempstate = copy.deepcopy(self.getstate())
                    tempstate[temprow][tempcol] = tempstate[temprow+1][tempcol]
                    tempstate[temprow+1][tempcol] = 0
                    neighbors.append(tempstate)
                #move left
                if(tempcol >0):
                    tempstate = copy.deepcopy(self.getstate())
                    tempstate[temprow][tempcol] = tempstate[temprow][tempcol-1]
                    tempstate[temprow][tempcol-1] = 0
                    neighbors.append(tempstate)
                #move up
                if(temprow >0):
                    tempstate = copy.deepcopy(self.getstate())
                    tempstate[temprow][tempcol] = tempstate[temprow-1][tempcol]
                    tempstate[temprow-1][tempcol] = 0
                    neighbors.append(tempstate)

def cmpCost(statev):
    cost = 0
    for i in range(9):
        currow = int(x/3)
        curcol = i % 3
        if(statev[temprow][tempcol] != 0):
            number = statev[temprow][tempcol]
            rightrow = int(number/3)
            rightcol = number % 3
            cost += (abs(rightrow - currow) + abs(rightcol + curcol))
    return cost


