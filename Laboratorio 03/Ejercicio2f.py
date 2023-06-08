from interpreter import draw
from chessPictures import *

squareBl = square.negative()
newImg = square.join(squareBl)
newImg2 = squareBl.join(square)

newImg = newImg.horizontalRepeat(3)
newImg2 = newImg2.horizontalRepeat(3)

table = newImg.up(newImg2)

table = table.verticalRepeat(1)
draw(table)