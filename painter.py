import os
from PIL import Image  

TOTAL_SIZE = 1000
TILE_SIZE = 100
TILE_PATH = "tiles/"

from SimpleMapSolver import SimpleMapSolver

mapSolver = SimpleMapSolver(11,7) 
mapSolver.fillLookUpTable()
mapSolver.solve()
mapo = mapSolver.map
print(*mapo)



def listTiles():
    tileList = [-1] #the first element is error (shouldn't be picked)
    tileNames = os.listdir(TILE_PATH)
    tileNames.sort()
    print(tileNames)
    for tileName in tileNames:
        im = Image.open(TILE_PATH + tileName)
        im = im.resize((500,500))
        im.thumbnail((TILE_SIZE, TILE_SIZE), Image.ANTIALIAS)
        tileList.append(im)
    return tileList


def initImage():
    img = Image.new( 
        mode = "RGB", 
        size = (TOTAL_SIZE,TOTAL_SIZE), 
        color = 'white' )
    return img


def paintImage():
    img = initImage()
    tileList = listTiles()
    for i in range(len(mapo)):
        for j in range(len(mapo)):
            print(f"{i}:{j}|", end='')
            img.paste(
                tileList[mapo[i][j]],
                (
                    j * TILE_SIZE,
                    i * TILE_SIZE
                )
            )
        #print()
    return img

def save_img(path, img, index=""):
    filePath = path + "img" + index + ".jpg"
    img.save(filePath)
    print("Map succesfully created at "+ filePath)


def main():
    save_img(
        "",
        paintImage(),
    )

main()