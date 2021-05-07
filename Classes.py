class pawn():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        self.firstMove = True
        self.moves = []

    def moveset(self):
        if self.firstMove:
            self.moves = [[0,1],[0,2]]
        else:
            self.moves = [[0,1]]


class rook():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        pass

class bishop():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
<<<<<<< HEAD
        pass
=======

>>>>>>> 0f27c48a30c3cab41b369df7d6bd5deb19b6ef12

class queen():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        pass

class king():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        pass

class knight():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        pass
