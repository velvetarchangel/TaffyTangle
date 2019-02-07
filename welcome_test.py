from stddraw import *
from color import Color
import picture as p
cutepurple = Color(130,0,172)
cuteblue = Color(7,185,252)
setXscale(-1.0, 8.0)
setYscale(-10.0, 1.5)
score = 500
high_score = 900
def game_lost_screen(score, high_score):
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
    setPenColor(BLACK)
    setFontSize(40)
    text(3.5, 0, "Game Over!")
    text(3.5, -1.0, "Your score is " + str(score))
    text(3.5, -2.0, "High score is " + str(high_score))
    if mousePressed():
        if mouseX() >= 0.0 and mouseX() <= 3.0 and mouseY() >= -6.0 and mouseY() <=-4.0:
            play = True
        elif mouseX() >= 4.0 and mouseX() <= 7.0 and mouseY() >= -6.0 and mouseY() <= -4.0:
            exit()
    show()
    return(play)

game_lost_screen(score, high_score)