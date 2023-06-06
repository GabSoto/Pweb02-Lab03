from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

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
    # falta
    return Picture(None)

  def under(self, p):

    under = p.img

    for i in range(len(self.img)):
      under.append(self.img[i])
    return Picture(under)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):

    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

