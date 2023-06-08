from interpreter import draw
from chessPictures import *

squareBl = square.negative()
newImg = squareBl.join(square)

newImg = newImg.horizontalRepeat(3)

draw(newImg)