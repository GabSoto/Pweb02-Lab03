from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []
    a=0
    for i in range (len(self.img)):
      a-=1
      horizontal.append(self.img[a])
      
    return Picture(horizontal)

  def negative(self):
    negative = []
    for row in self.img:
      inverted_row = [self._invColor(color) for color in row]
      negative.append(inverted_row)
    return Picture(negative)

  def join(self, p):

    new_img = []
    
    for i in range(len(self.img)):
        new_img.append(list(self.img[i]) + list(p.img[i]))
    
    return Picture(new_img)

  def up(self, p):
    up = p.img

    for i in range(len(self.img)):
      up.append(self.img[i])
    return Picture(up)

  def under(self, p):

    under = []

    for i in range(len(self.img)):
      str = ""
      for j in range(len(self.img[i])):
        if(self.img[i][j] == " "):
          str+=p.img[i][j]
        else:
          str+=self.img[i][j]
      
      under.append(str)

    return Picture(under)
  
  def horizontalRepeat(self, n):
    repeated_img = self.img  # Crear una copia de la imagen original
    
    for i in range(n):
        repeated_img = self.join(Picture(repeated_img)).img  # Unir la imagen repetida con la imagen actual
    
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    repeated_img = self.img  # Crear una copia de la imagen original
    
    for i in range(n):
        repeated_img = self.up(Picture(repeated_img)).img  # Unir la imagen repetida con la imagen actual
    
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

