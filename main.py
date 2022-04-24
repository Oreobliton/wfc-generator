from Painter import Painter
from SimpleMapSolver import SimpleMapSolver

TOTAL_SIZE = 1000
TILE_SIZE = 100
TILE_PATH = "tiles/"
OUTPUT_PATH = "out/"
ITERATIONS = 20
TILE_NUMBER = 7
#The map is a matrix of MAP_SIZE row per MAP_SIZE columns
#MAP_SIZE needs to be divisible by TOTAL_SIZE
MAP_SIZE = 10 

for _ in range(ITERATIONS):
    mapSolver = SimpleMapSolver(MAP_SIZE,TILE_NUMBER) 
    tileMap = mapSolver.generate()
    painter = Painter(
        TOTAL_SIZE,
        TILE_SIZE,
        tileMap,
        tilePath = TILE_PATH,
        outputPath = OUTPUT_PATH
    )
    painter.generate()