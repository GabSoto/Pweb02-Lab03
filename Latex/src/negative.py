def negative(self):
    negative = []
    for row in self.img:
        inverted_row = [self._invColor(color) for color in row]
        negative.append(inverted_row)
    return Picture(negative)