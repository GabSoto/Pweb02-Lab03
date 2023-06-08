from interpreter import draw
from chessPictures import *

knight1 = knight
blacKnight1 = knight.negative()

knight2 = knight
knight2 = knight2.verticalMirror()

blacKnight2 = knight.negative()
blacKnight2 = blacKnight2.verticalMirror()

newPicture = (blacKnight2.join(knight2)).up(knight1.join(blacKnight1))
draw(newPicture)