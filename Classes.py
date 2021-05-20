class pawn():
    def __init__(self,x,y,img, color):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color
        self.img = img
        self.firstMove = True
        self.moves = []

    def moveset(self, whitePieces, blackPieces):
        pieces = whitePieces + blackPieces
        if self.color == -1:
            enemy = blackPieces
        else:
            enemy = whitePieces
        if self.firstMove:
            for i in pieces:
                if i.y == self.y + self.color*125 and i.x == self.x:
                    print(True)
                    self.moves = [[0,0]]
                    break
                elif i.y == self.y + self.color*250 and i.x == self.x:
                    self.moves = [[0,self.color*1]]
                    break
                else:
                    self.moves = [[0,self.color*1],[0,self.color*2]]

                for i in enemy:
                    if i.x == self.x - 125 and i.y == self.y + self.color*125:
                        self.moves.append([-1,self.color*1])
                    if i.x == self.x + 125 and i.y == self.y + self.color*125:
                        self.moves.append([1,self.color*1])
        else:

            for i in pieces:
                if i.y == self.y + self.color*125 and i.x == self.x:
                    self.moves = [[0,0]]
                    if i.x == self.x - 125:
                        self.moves.append([-1,1])
                    if i.x == self.x + 125:
                        self.moves.append([1,1])
                    break
                else:
                    self.moves = [[0,self.color*1]]

            for i in enemy:
                if i.x == self.x - 125 and i.y == self.y + self.color*125:
                    self.moves.append([-1,self.color*1])
                if i.x == self.x + 125 and i.y == self.y + self.color*125:
                    self.moves.append([1,self.color*1])


class rook():
    def __init__(self,x,y,img, color):
        self.x = x
        self.y = y
        self.dx = 0
        self.img = img
        self.color = color
        self.moves = []

    def moveset(self, whitePieces, blackPieces):
        pieces = whitePieces + blackPieces
        if self.color == -1:
            enemy = blackPieces
        else:
            enemy = whitePieces

class bishop():
    def __init__(self,x,y,img,color):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color
        self.img = img
        self.moves = []


    def moveset(self, whitePieces, blackPieces):
        pieces = whitePieces + blackPieces
        if self.color == -1:
            enemy = blackPieces
        else:
            enemy = whitePieces

class queen():
    def __init__(self,x,y,img,color):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color
        self.img = img
        self.moves = []

    def moveset(self, whitePieces, blackPieces):
        pieces = whitePieces + blackPieces
        if self.color == -1:
            enemy = blackPieces
        else:
            enemy = whitePieces

class king():
    def __init__(self,x,y,img,color):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color
        self.img = img
        self.moves = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]

    def moveset(self, whitePieces, blackPieces):
        self.moves = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]
        if self.color == -1:
            enemy = blackPieces
            friend = whitePieces
        else:
            enemy = whitePieces
            friend = blackPieces

        for i in friend:
            x = (i.x-self.x)/125
            y = (i.y-self.y)/125

            move = [x,y]
            try:
                self.moves.remove(move)
            except:
                pass


class knight():
    def __init__(self,x,y,img,color):
        self.x = x
        self.y = y
        self.dx = 0
        self.color = color
        self.img = img
        self.moves = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

    def moveset(self, whitePieces, blackPieces):
        pieces = whitePieces + blackPieces
        if self.color == -1:
            enemy = blackPieces
        else:
            enemy = whitePieces
