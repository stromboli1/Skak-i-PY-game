<<<<<<< Updated upstream
=======
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

def mvcal(xORy, felt):
    if xORy == x:
        return (felt-250)/125
    elif xORy == y:
        return felt/125


class rook():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
        self.moves = []

    def moveset(self):
        for i in range(1,8):
            self.moves.append([abs(i-mvcal(x,self.x)),0])
            self.moves.append([0,abs(i-mvcal(y,self.y))])

        print(self.moves)


class bishop():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img


class queen():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img

class king():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img

class knight():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0

        self.img = img
>>>>>>> Stashed changes
