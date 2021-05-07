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


class tower():
    def __init__(self):
        self.x = x
        self.y = y
        self.dx = 0
        pass

class runner():
    def __init__(self):
        pass

class queen():
    def __init__(self):
        pass

class king():
    def __init__(self):
        pass

class knight():
    def __init__(self):
        pass
