def up(self, p):
    up = p.img

    for i in range(len(self.img)):
      up.append(self.img[i])
    return Picture(up)