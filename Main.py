import pygame as pg
from Classes import pawn
from Classes import bishop
from Classes import rook
from Classes import knight
from Classes import queen
from Classes import king
import os
import math
import random

pg.init()
win = pg.display.set_mode((1500,1000))
pg.display.set_caption("Skak")
clock = pg.time.Clock()
path = os.path.abspath(os.getcwd()) + "//Chess_pieces_SVG//"

b_bishop_img = pg.image.load(path + "b_bishop_png_shadow_1024px.png")
b_knight_img = pg.image.load(path + "b_knight_png_shadow_1024px.png")
b_pawn_img = pg.image.load(path+"b_pawn_png_shadow_1024px.png")
b_rook_img = pg.image.load(path + "b_rook_png_shadow_1024px.png")
b_queen_img = pg.image.load(path + "b_queen_png_shadow_1024px.png")
b_king_img = pg.image.load(path + "b_king_png_shadow_1024px.png")
board_brown = pg.image.load(path+"square brown light_png_shadow_1024px.png")
board_grey = pg.image.load(path+"square gray light _png_shadow_1024px.png")
w_bishop_img = pg.image.load(path + "w_bishop_png_shadow_1024px.png")
w_knight_img = pg.image.load(path + "w_knight_png_shadow_1024px.png")
w_pawn_img = pg.image.load(path + "w_pawn_png_shadow_1024px.png")
w_rook_img = pg.image.load(path + "w_rook_png_shadow_1024px.png")
w_queen_img = pg.image.load(path + "w_queen_png_shadow_1024px.png")
w_king_img = pg.image.load(path + "w_king_png_shadow_1024px.png")

sc_b_pawn_img = pg.transform.scale(b_pawn_img,(125,125))
sc_b_bishop_img = pg.transform.scale(b_bishop_img,(125,125))
sc_b_knight_img = pg.transform.scale(b_knight_img,(125,125))
sc_b_rook_img = pg.transform.scale(b_rook_img,(125,125))
sc_b_queen_img = pg.transform.scale(b_queen_img,(125,125))
sc_b_king_img = pg.transform.scale(b_king_img,(125,125))

sc_w_pawn_img = pg.transform.scale(w_pawn_img,(125,125))
sc_w_bishop_img = pg.transform.scale(w_bishop_img,(125,125))
sc_w_knight_img = pg.transform.scale(w_knight_img,(125,125))
sc_w_rook_img = pg.transform.scale(w_rook_img,(125,125))
sc_w_queen_img = pg.transform.scale(w_queen_img,(125,125))
sc_w_king_img = pg.transform.scale(w_king_img,(125,125))

blackPieces = []
whitePieces = []

for i in range(8):
    blackPieces.append(pawn(250+125*i,125,sc_b_pawn_img))


for i in range(2):
    blackPieces.append(rook(250+i*875,0,sc_b_rook_img))
    blackPieces.append(bishop(500+375*i,0,sc_b_bishop_img))
    blackPieces.append(knight(375+625*i,0,sc_b_knight_img))

for i in range(1):
    blackPieces.append(queen(625*(i+1),0,sc_b_queen_img))
    blackPieces.append(king(750*(i+1),0,sc_b_king_img))

for i in range(8):
        whitePieces.append(pawn(250+125*i,500,sc_w_pawn_img))

def redrawGameWindow():
    for x in range(8):
        for y in range(8):
            if (x+1) % 2 == 1 and (y+1) % 2 == 1:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            elif (x+1) % 2 == 0 and (y+1) % 2 == 0:
                win.blit(pg.transform.scale(board_brown,(125,125)),(250+125*x,125*y))
            else:
                win.blit(pg.transform.scale(board_grey,(125,125)),(250+125*x,125*y))

    for i in blackPieces:
        win.blit(i.img,(i.x,i.y))

    pg.display.update()

run = True
turn = 0
while run:
    pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if pressed1:
        pos = pg.mouse.get_pos()
        for i in blackPieces:
            print(pos)
            if i.x < pos[0] < i.x + 125 and i.y < pos[1] < i.y + 125:
                print("Hello")


    redrawGameWindow()
