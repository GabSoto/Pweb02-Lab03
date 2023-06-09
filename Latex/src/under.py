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