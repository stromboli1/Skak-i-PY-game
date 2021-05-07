import pygame as pg
from Classes import pawn
import os
import math
import random

pg.init()
win = pg.display.set_mode((1500,1000))
pg.display.set_caption("Skak")
clock = pg.time.Clock()
path = os.path.abspath(os.getcwd()) + "//Chess_pieces_SVG//"

b_pawn_img = pg.image.load(path+"b_pawn_png_shadow_1024px.png")
board_brown = pg.image.load(path+"square brown light_png_shadow_1024px.png")
board_grey = pg.image.load(path+"square gray light _png_shadow_1024px.png")

sc_b_pawn_img = pg.transform.scale(b_pawn_img,(125,125))

blackPieces = []

for i in range(8):
    blackPieces.append(pawn(250+125*i,125,sc_b_pawn_img))

def redrawGameWindow(moves, pickedPiece):
    for x in range(8):
        for y in range(8):
            if (x+1) % 2 == 1 and (y+1) % 2 == 1:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            elif (x+1) % 2 == 0 and (y+1) % 2 == 0:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            else:
                win.blit(pg.transform.scale(board_grey,(125,125)),(250+125*x,125*y))

    if moves != 0:
        for i in moves:
            pg.draw.rect(win,(255,255,255),(pickedPiece.x + 125*i[0],pickedPiece.y + 125*i[1],125,125))


    for i in blackPieces:
        win.blit(i.img,(i.x,i.y))

    pg.display.update()

def moves(piece):
    piece.moveset()
    return piece.moves

clock.tick(10)
run = True
turn = random.randint(0,1)
pickedPiece = 0
move = 0
while run:
    pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if pressed1:
        pos = pg.mouse.get_pos()
        for i in blackPieces:
            if i.x < pos[0] < i.x + 125 and i.y < pos[1] < i.y + 125:
                pickedPiece = i
                break

    if pickedPiece != 0:
        move = moves(pickedPiece)

    redrawGameWindow(move, pickedPiece)
