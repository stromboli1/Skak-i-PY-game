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
        if self.firstMove:
            for i in pieces:
#                if i.x == self.x -125:
#                    print("x=True")
                if i.y == self.y + self.color*125:
                    print("y=True")

                if i.y == self.y + self.color*125 and i.x == self.x:
                    print(True)
                    self.moves = [[0,0]]
#                    if i.x == self.x - 125 and i.y == self.y + self.color*125:
#                        self.moves.append([-1,1])
#                    if i.x == self.x + 125 and i.y == self.y + self.color*125:
#                        self.moves.append([1,1])
                    break
                elif i.y == self.y + self.color*250 and i.x == self.x:
#                    print(True)
                    self.moves = [[0,self.color*1]]
#                    if i.x == self.x - 125 and i.y == self.y + self.color*125:
#                        self.moves.append([-1,1])
#                    if i.x == self.x + 125 and i.y == self.y + self.color*125:
#                        self.moves.append([1,1])
                    break
                else:
                    self.moves = [[0,self.color*1],[0,self.color*2]]
                    if i.x == self.x - 125 and i.y == self.y + self.color*125:
#                        print(True)
                        self.moves.append([-1,1])
#                        try:
#                            self.moves.remove([-1,1])
#                        except:
#                            self.moves.append([-1,1])
                    if i.x == self.x + 125 and i.y == self.y + self.color*125:
                        self.moves.append([1,1])
#                        try:
#                            self.moves.remove([1,1])
#                        except:
#                            self.moves.append([1,1])
        else:
            for i in pieces:
                if i.y == self.y + self.color*125 and i.x == self.x:
                    self.moves = [[0,0]]
                    break
                else:
                    self.moves = [[0,self.color*1]]

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
