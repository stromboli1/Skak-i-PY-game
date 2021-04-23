class pawn():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 1
        self.img = img
        self.firstMove = True

        def promote():
            if self.y == 1 or 8:
                self.remove()
                self.add(click())
                self.x = self.x
                self.y = self.y

         if self.firstMove:
             self.dy = 1 or 2



class tower():
    def __init__(self):
        self.x = x
        self.y = y
        self.dx = i or 0
        self.dy = 0 or i
        self.img = img
        self.firstMove = True

class runner():
    def __init__(self):
        self.x = x
        self.y = y
        self.dx = i
        self.dy = i
        self.img = img
        self.firstMove = True

class queen():
    def __init__(self):
        pass

class king():
    def __init__(self):
        pass

class knight():
    def __init__(self):
        pass
