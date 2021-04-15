class chessPiece():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img

        def move(self,dx,dy):
            self.dy += dy*125
            self.dx += dx*125

        def draw(self):
            pass

        def death(self):
            pass

class pawn(chessPiece):
    def __init__(self,x,y,img):
        self.dx = 0
        self.dy = 1
        super().__init__(x,y,img)



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

square = Square(4)
print(square.area())
