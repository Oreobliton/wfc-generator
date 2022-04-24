import random
from secrets import choice
MAP_SIZE = 16
TILE_NUMBER = 7

 
def makeLookUpTable(numberOfTiles):
    lookupTable = dict()
    for i in range(numberOfTiles+1):
        lookupTable[i] = set([i-1,i,i+1])
        if i == 0:
            lookupTable[i] = set([x for x in range(1, numberOfTiles+1)])
        if i == 1:
            lookupTable[i] = set([i,i+1])
        if i == numberOfTiles:
            lookupTable[i] = set([i-1,i])
    return lookupTable


def prettyPrint(map):
    for line in map:
        print(*line)

def updateTile(previousNumberLeft, previousNumberUp):
    possibleChoices = lookupTable[previousNumberLeft].intersection(lookupTable[previousNumberUp])
    return choice(list(possibleChoices))
        
def solve():
    #random input
    x = 0
    y = 0
    map[x][y] = random.randint(1,TILE_NUMBER)
    for j in range(MAP_SIZE):
        for i in range(MAP_SIZE):
            if (x==0) and (y==0):
                map[x][y] = updateTile(0,0) 
            elif (x==0):
                map[x][y] = updateTile(map[x][y-1],0) 
            elif (y==0):
                map[x][y] = updateTile(0,map[x-1][y]) 
            else:
                map[x][y] = updateTile(map[x][y-1],map[x-1][y]) 
            y += 1
        y = 0
        x += 1
    return map

map =[ [0]*MAP_SIZE for i in range(MAP_SIZE)]
lookupTable = makeLookUpTable(TILE_NUMBER)
#print(makeLookUpTable(TILE_NUMBER))
prettyPrint(solve())
