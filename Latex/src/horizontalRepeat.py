def horizontalRepeat(self, n):
    repeated_img = self.img
    
    for i in range(n):
        repeated_img = self.join(Picture(repeated_img)).img
    
    return Picture(repeated_img)