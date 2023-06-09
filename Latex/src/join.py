def join(self, p):

    new_img = []
    
    for i in range(len(self.img)):
        new_img.append(list(self.img[i]) + list(p.img[i]))
    
    return Picture(new_img)