from interpreter import draw
from chessPictures import *


inverKnight = knight.verticalMirror()
normalKnight = inverKnight.horizontalMirror()

newImg = inverKnight.join(normalKnight) 
draw(newImg)

