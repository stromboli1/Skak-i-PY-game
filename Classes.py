class pawn():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.img = img
        self.firstMove = True
        self.moves = []


    def promote():
        if self.y == 1 or 8:
            self.remove()
            self.add(click())
            self.x = self.x
            self.y = self.y



    def moveset(self):
        if self.firstMove:
            self.moves = [[0,1],[0,2]]
        else:
            self.moves = [[0,1]]



class rook():
    def __init__(self):
        self.x = x
        self.y = y
        self.dx = 0
        pass

        if self.firstMove == True:
            self.dy = 1 or 2
            self.firstMove == False
        else:
            self.dy = 1

        def enPassant():
            pass


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
