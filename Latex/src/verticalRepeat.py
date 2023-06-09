def verticalRepeat(self, n):
    repeated_img = self.img
    
    for i in range(n):
        repeated_img = self.up(Picture(repeated_img)).img
    
    return Picture(repeated_img)