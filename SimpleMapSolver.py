import random
from secrets import choice

class SimpleMapSolver:

    def __init__(self, mapSize, numberOfTiles):
        self.mapSize = mapSize
        self.numberOfTiles = numberOfTiles
        self.map = [[0]*mapSize for i in range(mapSize)]
        self.lookupTable = dict()

    def __str__(self):
        for line in map:
            string += " ".join(line) + "\n"
        return string

    def fillLookUpTable(self):
        for i in range(self.numberOfTiles+1):
            self.lookupTable[i] = set([i-1,i,i+1])
            if i == 0:
                self.lookupTable[i] = set([x for x in range(1, self.numberOfTiles+1)])
            if i == 1:
                self.lookupTable[i] = set([i,i+1])
            if i == self.numberOfTiles:
                self.lookupTable[i] = set([i-1,i])

    def updateTile(self, leftTile, upTile):
        possibleChoices = self.lookupTable[leftTile].intersection(
            self.lookupTable[upTile]
            )
        return choice(list(possibleChoices))
            
    def solve(self):
        x = 0
        y = 0
        self.map[x][y] = random.randint(1,self.numberOfTiles)
        for j in range(self.mapSize):
            for i in range(self.mapSize):
                if (x==0) and (y==0):
                    self.map[x][y] = self.updateTile(0,0) 
                elif (x==0):
                    self.map[x][y] = self.updateTile(self.map[x][y-1],0) 
                elif (y==0):
                    self.map[x][y] = self.updateTile(0,self.map[x-1][y]) 
                else:
                    self.map[x][y] = self.updateTile(self.map[x][y-1],self.map[x-1][y]) 
                y += 1
            y = 0
            x += 1