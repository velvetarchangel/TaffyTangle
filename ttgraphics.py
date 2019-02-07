import sys
from stddraw import *
import math
import ttfunctions
from color import Color
import picture as p

#pieces from https://www.deviantart.com/ldinos

moon_gem = p.Picture('moon_gem.gif')
blue_gem = p.Picture('blue_gem.png')
orange_gem = p.Picture('orange_gem.png')
green_gem = p.Picture('green_gem.png')
purple_gem = p.Picture('purple_gem.png')
yellow_gem = p.Picture('yellow_gem.png')
red_gem = p.Picture('red_gem.png')


cutepurple = Color(130,0,172)
cuteblue = Color(7,185,252)

setXscale(-1.0, 8.0)
setYscale(-10.0, 1.5)

def blank_taffy(i,j):
    setPenColor(BLACK)
    filledSquare(j + 0.5, -i - 0.5, 0.5)

def square_taffy(i,j):
    picture(blue_gem, j+ 0.5, -i-0.5)

def traingle_taffy(i, j):
    picture(orange_gem, j+ 0.5, -i-0.5)

def pentagon_taffy(i,j):
    picture(green_gem, j+0.5, -i-0.5)

def octagon_taffy(i,j):
    picture(red_gem, j+0.5, -i-0.5)

def parallelogram_taffy(i,j):
    picture(yellow_gem, j+0.5, -i-0.5)

def circle_taffy(i,j):
    picture(purple_gem, j+0.5, -i-0.5)

def moon_jewel(i,j):
    picture(moon_gem, j+0.5, -i-0.5)

def draw_board(board, score, highscore):
    clear()
    clear(BLACK)
    for i in range(9):
        for j in range(7):
            if board[i][j] == 0:
                blank_taffy(i,j)
            elif board[i][j] == 1:
                square_taffy(i,j)
            elif board[i][j] == 2:
                traingle_taffy(i,j)
            elif board[i][j] == 3:
                circle_taffy(i,j)
            elif board[i][j] == 4:
                pentagon_taffy(i,j)
            elif board[i][j] == 5:
                octagon_taffy(i,j)
            elif board[i][j] == 6:
                parallelogram_taffy(i,j)
            elif board[i][j] == 7:
                moon_jewel(i,j)
    setPenColor(WHITE)
    setFontSize(25)
    setFontFamily("Lucida")
    text(1, .75, "Score: " + str(score))
    text(5, .75, "High Score: " + str(highscore))
    show(200)

def draw_first_box(mx, my):
    setPenColor(GREEN)
    setPenRadius(0.005)
    rectangle(mx,my,1.0,1.0)
    show(0)

def draw_second_box(mx, my):
    setPenColor(GREEN)
    setPenRadius(0.005)
    rectangle(mx, my, 1.0, 1.0)
    show(0)

def welcome_screen(play):
    setPenColor(cutepurple)
    filledRectangle(0, -6, 3, 2)
    setPenColor(BLACK)
    rectangle(0, -6, 3, 2)
    setPenColor(cuteblue)
    filledRectangle(4, -6, 3, 2)
    setPenColor(DARK_BLUE)
    rectangle(4, -6, 3, 2)
    setPenColor(WHITE)
    setFontFamily("Lucida")
    setFontSize(50)
    text(1.5, -5, "Play")
    text(5.5, -5, "Exit")
    setFontSize(30)
    text(3.5, -9.75, "Score As Many Points As Possible In 30 Seconds!")
    if mousePressed():
        if mouseX() >= 0.0 and mouseX() <= 3.0 and mouseY() >= -6.0 and mouseY() <=-4.0:
            play = True
        elif mouseX() >= 4.0 and mouseX() <= 7.0 and mouseY() >= -6.0 and mouseY() <= -4.0:
            exit()
    show(500)
    return(play)

def game_lost_screen(play, score, high_score):
    clear()
    clear(BLACK)
    setPenColor(cutepurple)
    filledRectangle(0, -6, 3, 2)
    setPenColor(BLACK)
    rectangle(0, -6, 3, 2)
    setPenColor(cuteblue)
    filledRectangle(4, -6, 3, 2)
    setPenColor(DARK_BLUE)
    rectangle(4, -6, 3, 2)
    setPenColor(WHITE)
    setFontFamily("Lucida")
    setFontSize(50)
    text(1.5, -5, "Play")
    text(5.5, -5, "Exit")
    setPenColor(WHITE)
    setFontSize(40)
    text(3.5, 0, "Time's Up!  Game Over!")
    text(3.5, -1.0, "Your score is " + str(score))
    text(3.5, -2.0, "High score is " + str(high_score))
    if mousePressed():
        if mouseX() >= 0.0 and mouseX() <= 3.0 and mouseY() >= -6.0 and mouseY() <=-4.0:
            play = True
        elif mouseX() >= 4.0 and mouseX() <= 7.0 and mouseY() >= -6.0 and mouseY() <= -4.0:
            exit()
    show(500)
    return(play)
