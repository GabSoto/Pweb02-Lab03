from interpreter import draw
from chessPictures import *

squareBl = square.negative()
newImg = square.join(squareBl)

newImg = newImg.horizontalRepeat(3)

draw(newImg)