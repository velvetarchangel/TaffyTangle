import sys
from math import *
import random
from stddraw import *
import ttgraphics

def create_board(): #generates the initial board
    line = []
    board = []
    check = 0
    for i in range(9):
        for j in range(7):
            piece = random.randrange(1, 8)
            line.append(piece)
        board.append(line)
        line = []
    return(board)

def check_board(board): #changes the chains in the initial board
    while True:
        check = 0
        for i in range(9):
            for j in range(5):
                if board[i][j] == board[i][j+1] == board[i][j+2]:
                    board[i][j] = random.randrange(1,8)
                    check += 1
        for j in range(7):
            for i in range(7):
                if board[i][j] == board[i+1][j] == board[i+2][j]:
                    board[i][j] = random.randrange(1,8)
                    check += 1
        if check == 0:
            break
    return(board)

def find_chains(board): #finds the chains and returns their index values
    is_a_chain = False
    chains = [] #the final list of indexes for the matches
    matches = [] # temporary lists of matches that get appended to the total
    #check for horizontal matches
    for i in range(9):
        for j in range(6):
            if board[i][j] == board[i][j+1]:
                matches.append((i, j))
            elif board[i][j] != board[i][j+1] and board[i][j] == board[i][j-1]:
                matches.append((i, j))
            if j == 5 and board[i][j] == board[i][j+1]:
                matches.append((i, j+1))
                if len(matches) > 2:
                    chains.append(matches)
                    is_a_chain = True
                    matches = []
                else:
                    matches = []
            if board[i][j] != board[i][j+1]:
                if len(matches) > 2:
                    chains.append(matches)
                    is_a_chain = True
                    matches = []
                else:
                    matches = []
        matches = []
    #check veritcals for matches
    for j in range(7):
        for i in range(8):
            if board[i][j] == board[i+1][j]:
                matches.append((i, j))
            elif board[i][j] != board[i+1][j] and board[i][j] == board[i-1][j]:
                matches.append((i, j))
            if i == 7 and board[i][j] == board[i+1][j]:
                matches.append((i+1, j))
                if len(matches) > 2:
                    chains.append(matches)
                    is_a_chain = True
                    matches = []
                else:
                    matches = []
            if board[i][j] != board[i+1][j]:
                if len(matches) > 2:
                    chains.append(matches)
                    is_a_chain = True
                    matches = []
                else:
                    matches = []
        matches = []
    return(is_a_chain, chains)

def make_matches_zero(board, chains):
    for i in range(len(chains)):
        for j in range(len(chains[i])):
            board[chains[i][j][0]][chains[i][j][1]] = 0
    return(board)

def calculate_score(chains):
    score = 0
    points = {3: 30, 4: 60, 5: 120, 6: 240, 7: 480, 8: 960, 9: 1920}
    for i in range(len(chains)):
        score += points.get(len(chains[i]))
    return(score)

def drop_pieces(board): #moves the 0 values up on the board
    while True:
        check = 0
        for i in range(8,0,-1):
            for j in range(7):
                if board[i][j] == 0 and board[i - 1][j] != 0:
                    board [i][j] = board[i - 1][j]
                    board[i - 1][j] = 0
                    check += 1
        if check == 0:
            break
    return(board)

def insert_new_pieces(board): #changes the zeros (empty squares) to random numbers (pieces)
    for i in range(9):
        for j in range(7):
            if board[i][j] == 0:
                board[i][j] = random.randrange(1,8)
    return(board)

def get_row_column(mx,my):
    """takes the x and y values of the click and converts it into an index in the board array"""
    row = -1
    column = -1
    if (mx >= 0 and mx <= 7):
        column = floor(mx)
    if my >= -9 and my <= 0:
        row = floor(abs(my))-1
    return (column, row)

def is_adjacent(first_box_i, first_box_j, second_box_i, second_box_j):
    """checks to see if the selections are adjacent"""
    first_coord = [first_box_i, first_box_j]
    second_coord = [second_box_i, second_box_j]
    if first_coord[0] == second_coord[0] and first_coord[1] == second_coord[1]-1:
        return True
    elif first_coord[0] == second_coord[0] and first_coord[1] == second_coord[1]+1:
        return True
    elif first_coord[0] == second_coord[0]+1 and first_coord[1] == second_coord[1]:
        return True
    elif first_coord[0] == second_coord[0]-1 and first_coord[1] == second_coord[1]:
        return True
    else:
        return False

def detect_first_box(board, first_selection):
    first_box_i = 0 # the row value of the first selection box
    first_box_j = 0 # the column value of the first selection box
    """waits for the first mouse press and feeds data into the next loop"""
    if mousePressed():
        mx = floor(mouseX())
        my = floor(mouseY())
        column, row = get_row_column(mx,my)
        if row != -1 and column != -1: # this handles errors... if the selection is outside the board it does NOTHING
            first_selection = True
            ttgraphics.draw_first_box(mx, my)
            first_box_i = row
            first_box_j = column
    show(0)
    return(first_selection, first_box_i, first_box_j)

def detect_second_box(board, second_selection): #WORKING
    mx = 0
    my = 0
    second_box_i = 0
    second_box_j = 0
    if mousePressed():
        mx = floor(mouseX())
        my = floor(mouseY())
        column, row = get_row_column(mx,my)
        if row != -1 and column != -1: # this handles errors... if the selection is outside the board it does NOTHING
            second_selection = True
            #clear()
            #ttgraphics.draw_board(board)
            second_box_i = row
            second_box_j = column
            ttgraphics.draw_second_box(mx, my)
    show(0)
    return(second_selection, second_box_i, second_box_j, mx,my)

def swap(board, first_box_i, first_box_j, second_box_i, second_box_j, score, highscore):
    clear()
    board[first_box_i][first_box_j], board[second_box_i][second_box_j] = board[second_box_i][second_box_j], board[first_box_i][first_box_j] #swap algorithm
    ttgraphics.draw_board(board, score, highscore)
    first_selection = False # I want this to pass control back to the user
    second_selection = False
    return(board, first_selection, second_selection)

def update_selection(board, second_box_i, second_box_j, mx_2, my_2, score, highscore):
    """updates the second selection as the first selection"""
    clear()
    ttgraphics.draw_board(board, score, highscore)
    ttgraphics.draw_first_box(mx_2,my_2)
    first_box_i, first_box_j = second_box_i, second_box_j
    first_selection = True # I want this to run back to the top of the loop and pass control back to the user
    second_selection = False
    return(first_selection, second_selection, first_box_i, first_box_j)
