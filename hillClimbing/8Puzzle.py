#8Puzzle impelementation

import  random
import  copy
import time
import math

tmprtur = 40.0

class problem:

    def __init__(self,initialState = None):
        if (initialState == None):
            tempstate = [i for i in range(9)]
            random.shuffle(tempstate)
            self.statevar = [[tempstate[(i*3) + j] for j in range(3)] for i in range(3)]
        else:
            self.setState(initialState)

    def setState(self,statev):
        self.statevar = [[statev[i][j] for j in range(3)] for i in range(3)]

    def getstate(self):
        return self.statevar

    def getsuccessors(self):
        neighbors = []
        for i in range(9):
            temprow = int(i/3)
            tempcol = i%3
            if(self.statevar[temprow][tempcol] == 0):
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
        return neighbors

def cmpCost(statev):
    cost = 0
    for i in range(9):
        currow = int(i/3)
        curcol = i % 3
        if(statev[currow][curcol] != 0):
            number = statev[currow][curcol]
            rightrow = int(number/3)
            rightcol = number % 3
            cost += (abs(rightrow - currow) + abs(rightcol + curcol))
    return cost

def stepAscent(statev = None):
    curstate = problem(statev)
    while(True):
        neighbors = curstate.getsuccessors()
        print(neighbors)
        bestnibr = curstate.getstate()
        lowescost = cmpCost(bestnibr)
        while(neighbors.__len__() > 0):
            nibrstate = neighbors.pop()
            nibrcost = cmpCost(nibrstate)
            if(lowescost > nibrcost):
                bestnibr = nibrstate
                lowescost = nibrcost
        if (bestnibr == curstate.getstate()):
            break
        curstate.setState(bestnibr)
    return curstate.getstate()

def firstChoice(statev = None):
    curstate = problem(statev)
    print(curstate.getstate())
    print(cmpCost(curstate.getstate()))
    while(True):
        neighbors = curstate.getsuccessors()
        print(neighbors)
        bestnibr = curstate.getstate()
        lowescost = cmpCost(bestnibr)
        while(neighbors.__len__() > 0):
            rndNum = random.randint(0,neighbors.__len__()-1)
            nibrstate = neighbors.pop(rndNum)
            nibrcost = cmpCost(nibrstate)
            if(lowescost > nibrcost):
                bestnibr = nibrstate
                lowescost = nibrcost
                break
        if (bestnibr == curstate.getstate()):
            break
        curstate.setState(bestnibr)
    return curstate.getstate()

def randomRestart(iterationNum = None):
    lowestcost = 1000
    curstate = None
    while (True):
        if (iterationNum != None):
            if (iterationNum <= 0):
                break
            iterationNum -= 1
        tempstate = stepAscent()
        print(tempstate)
        tempCost = cmpCost(tempstate)
        print(tempCost)
        if (tempCost < lowestcost):
            curstate = tempstate
            lowestcost = tempCost
        if (lowestcost == 0):
            break
    return curstate

def simulateAnnealing(startTime,statev = None):
    curstate = problem(statev)
    lowestCost = cmpCost(curstate.getstate())
    while(True):
        if(lowestCost == 0):
            break
        neighbors = curstate.getsuccessors()
        successorNum = random.randint(0,neighbors.__len__())
        tempstate = neighbors.pop(successorNum)
        tempCost = cmpCost(tempstate)
        if(tempCost < lowestCost):
            break
        else:
            chanceSelection = math.exp()

    return 1

def temperature(startTime):
    curtime = time.time()
    curtime -= startTime
    (1/(math.log10(curtime)))

sustate=firstChoice()
print(sustate)
print(cmpCost(sustate))


# print(int(time.time()))
# #simulateAnnealing(time.time())
# sulstate=randomRestart(100)
# testprob=problem(sulstate)
# print(testprob.getstate())
# print(cmpCost(testprob.getstate()))


