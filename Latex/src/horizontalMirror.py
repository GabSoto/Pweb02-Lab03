def horizontalMirror(self):
    horizontal = []
    a=0
    for i in range (len(self.img)):
        a-=1
        horizontal.append(self.img[a])
    return Picture(horizontal)