import sys
import math
from ttfunctions import *
from ttgraphics import *
import time

start_time = time.time()
elapsed_time = 0
board = []
poss_moves = False
score = 0
highscore = 0
first_selection = False
second_selection = False
second_box_i = 0
second_box_j = 0
mx_2 = 0
my_2 = 0
chains = []
play = False
multiplier = 1

#opens the high score txt file and assigns highscore to that number
tempscore = open("highscore.txt", 'r')
highscore = int(tempscore.read())
tempscore.close()


"""Start Loop"""
board = create_board() #generates the board
print(board)
board = check_board(board) #gets rid of chains in the initial board
#poss_moves = ttfunctions.check_for_possible_moves(board) POSSIBLE MOVES ALGORITHM GOES HERE!

"""Main Loop"""
#while poss_moves != False:
#    poss_moves = ttfunctions.check_for_possible_moves(board) #check for possible moves
draw_board(board, score, highscore)
print(board)

while True:
    resume = welcome_screen(play)
    if resume == True:
        draw_board(board, score, highscore)
        while elapsed_time < 30.0: #need to alter this condition
            elapsed_time = time.time() - start_time

            if first_selection == False:
                first_selection, first_box_i, first_box_j = detect_first_box(board, first_selection)

            if first_selection == True:
                second_selection, second_box_i, second_box_j, mx_2, my_2 = detect_second_box(board, second_selection)

            if first_selection == True and second_selection == True:
                check_adjacent = is_adjacent(first_box_i, first_box_j, second_box_i, second_box_j)
                if check_adjacent == True:
                    board, first_selection, second_selection = swap(board, first_box_i, first_box_j, second_box_i, second_box_j, score, highscore)
                    is_a_chain, chains = find_chains(board)
                    if is_a_chain == False:
                        board, first_selection, second_selection = swap(board, first_box_i, first_box_j, second_box_i, second_box_j, score, highscore)
                    if is_a_chain == True:
                        multiplier = 1
                        while len(chains) != 0:
                            is_a_chain, chains = find_chains(board)
                            board = make_matches_zero(board, chains)
                            draw_board(board, score, highscore)
                            score += calculate_score(chains) * multiplier
                            if score > highscore:
                                highscore = score
                            board = drop_pieces(board)
                            draw_board(board, score, highscore)
                            board = insert_new_pieces(board)
                            draw_board(board, score, highscore)
                            multiplier += 1
                    if score > highscore:
                        highscore = score
                if check_adjacent == False:
                    #update the first and second selection and the value of first_box_i and first_box_j
                    first_selection, second_selection, first_box_i, first_box_j = update_selection(board, second_box_i, second_box_j, mx_2, my_2, score, highscore)
            if score >= highscore:
                tempscore = open("highscore.txt", "w")
                tempscore.write(str(highscore))

        if elapsed_time > 30.0:
            resume = game_lost_screen(play, score, highscore)

        start_time = time.time()
        elapsed_time = 0
        score = 0
        chains = []
        board = create_board()
        board = check_board(board)
