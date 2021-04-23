class pawn():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        # if color == black:
        #     self.dy = -1
        #
        # else:
        #     self.dy = 1
        self.img = img
        self.firstMove = True

<<<<<<< HEAD
        def promote():
            if self.y == 1 or 8:
                self.remove()
                self.add(click())
                self.x = self.x
                self.y = self.y
=======
class tower():
    def __init__(self):
        self.x = x
        self.y = y
        self.dx = 0
        pass
>>>>>>> 98119e7598a01450d5ca3139aa56311b8106e51b

        if self.firstMove == True:
            self.dy = 1 or 2
            self.firstMove == False
        else:
            self.dy = 1

        def enPassant():
            pass



class rook():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img


class bishop():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img

class queen():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img



class king():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img


class knight():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img
