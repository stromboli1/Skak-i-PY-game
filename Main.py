import pygame as pg
import os

pg.init()
win = pg.display.set_mode((1500,1000))
pg.display.set_caption("Skak")
clock = pg.time.Clock()
path = os.path.abspath(os.getcwd()) + "//Chess_pieces_SVG//"

print(path)

chess_pieces = pg.image.load(path+"b_bishop_png_shadow_1024px.png")
board_brown = pg.image.load(path+"square brown light_png_shadow_1024px.png")
board_grey = pg.image.load(path+"square gray light _png_shadow_1024px.png")

sc_chess_pieces = pg.transform.scale(chess_pieces,(125,125))

def redrawGameWindow():
    for x in range(8):
        for y in range(8):
            if (x+1) % 2 == 1 and (y+1) % 2 == 1:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            elif (x+1) % 2 == 0 and (y+1) % 2 == 0:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            else:
                win.blit(pg.transform.scale(board_grey,(125,125)),(250+125*x,125*y))

    win.blit(sc_chess_pieces,(250,250))

    pg.display.update()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    redrawGameWindow()
