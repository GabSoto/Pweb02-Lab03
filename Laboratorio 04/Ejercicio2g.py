from interpreter import draw
from chessPictures import *

blackRock = rock.negative()
blacknight = knight.negative()
blackBishop = bishop.negative()
blackQueen = queen.negative()
blacKing = king.negative()
blackPawn = pawn.negative()

blackSquare = square.negative()

# Top part (black pieces)
table00 = blackRock.under(square)
table01 = blacknight.under(blackSquare)
new2 = table00.join(table01)

table02 = blackBishop.under(square)
new2 = new2.join(table02)

table03 = blackQueen.under(blackSquare)
new2 = new2.join(table03)

table04 = blacKing.under(square)
new2 = new2.join(table04)

table05 = blackBishop.under(blackSquare)
new2 = new2.join(table05)

table06 = blacknight.under(square)
new2 = new2.join(table06)

table07 = blackRock.under(blackSquare)
new2 = new2.join(table07)

# Top part (black pawns)
table11 = blackPawn.under(blackSquare)
table12 = blackPawn.under(square)

new3 = table11.join(table12)
new3 = new3.horizontalRepeat(3)

new2 = new3.up(new2)

# MediumPart ()
newImg = square.join(blackSquare)
newImg2 = blackSquare.join(square)

newImg = newImg.horizontalRepeat(3)
newImg2 = newImg2.horizontalRepeat(3)

new4 = newImg2.up(newImg)
new4 = new4.verticalRepeat(1)

new2 = new4.up(new2)

# Inferior part (white pawns)
table11 = pawn.under(square)
table12 = pawn.under(blackSquare)

new3 = table11.join(table12)
new3 = new3.horizontalRepeat(3)

new2 = new3.up(new2)

# Inferior part (white pieces)
table70 = rock.under(blackSquare)
table71 = knight.under(square)
new5 = table70.join(table71)

table72 = bishop.under(blackSquare)
new5 = new5.join(table72)

table73 = queen.under(square)
new5 = new5.join(table73)

table74 = king.under(blackSquare)
new5 = new5.join(table74)

table75 = bishop.under(square)
new5 = new5.join(table75)

table76 = knight.under(blackSquare)
new5 = new5.join(table76)

table77 = rock.under(square)
new5 = new5.join(table77)

new2 = new5.up(new2)

draw(new2)