import os
from PIL import Image  
from SimpleMapSolver import SimpleMapSolver

class Painter:
    def __init__(self, canvasSize, tileSize, tileMap, tilePath="tiles/", outputPath=""):
        self.canvasSize = canvasSize
        self.tileSize = tileSize
        self.tilePath = tilePath
        self.tileMap = tileMap
        self.tileList = list()
        self.canvas = None
        self.outputPath = outputPath

    def listTiles(self):
        self.tileList = [-1] #the first element is error (shouldn't be picked)
        tileNames = os.listdir(self.tilePath)
        tileNames.sort()
        for tileName in tileNames:
            im = Image.open(self.tilePath + tileName)
            im = im.resize((self.tileSize * 2,self.tileSize * 2))
            im.thumbnail((self.tileSize, self.tileSize), Image.ANTIALIAS)
            self.tileList.append(im)

    def initCanvas(self):
        self.canvas = Image.new( 
            mode = "RGB", 
            size = (self.canvasSize, self.canvasSize), 
            color = 'white' 
            )

    def paintImage(self):
        for i in range(len(self.tileMap)):
            for j in range(len(self.tileMap)):
                #print(f"{i}:{j}|", end='')
                self.canvas.paste(
                    self.tileList[self.tileMap[i][j]],
                    (
                        j * self.tileSize,
                        i * self.tileSize
                    )
                )


    def saveImage(self):
        index = len(os.listdir(self.outputPath))
        filePath = f"{self.outputPath}img-{index}.jpg"
        self.canvas.save(filePath)
        print(f"{'-'*8} Map succesfully created at {filePath} {'-'*8}")


    def generate(self):
        self.listTiles()
        self.initCanvas()
        self.paintImage()
        self.saveImage()