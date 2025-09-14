from tkinter import *
import tkinter.font as font
import random

# initial scores
player_score = 0
computer_score = 0

# game options for the computer
options = [('rock', 0), ('paper', 1), ('scissors, 2')]
# ⌈⌋
# funtion - computer wins
def computer_wins():
    global computer_score, player_score
    computer_score = computer_score + 1
    winner_label.config(text = "computer won !!")
    computer_score_label.config(text = "computer score: " + str(computer_score))
    player_score_label.config(text = "player score: " + str(player_score))

# function - player wins

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text = "player won !!")
    computer_score_label.config(text = "computer score: " + str(computer_score))
    player_score_label.config(text = "player score: " + str(player_score))

# function - tie

def tie():
    global computer_score, player_score
    winner_label.config(text = "tie !!")
    computer_score_label.config(text = "computer score: " + str(computer_score))
    player_score_label.config(text = "player score: " + str(player_score))

# main function - player chooses

def player_choice(player_input):
    global computer_score, player_score

    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    
    # update the selection on the screen
    player_choice_label.config(text = "you selected" + player_choice[0])
    computer_choice_label.config(text = "computer selected" + computer_input[0])

    # if player and computer choose the same option
    if player_input == computer_input:
        tie()
    # player chooses rock
    elif player_input[1] == 0:
        if computer_input[1] == 1:
            computer_wins()
        elif computer_input[1] == 2:
            player_wins()
    # player chooses paper
    elif player_input[1] == 1:
        if computer_input[1] == 0:
            player_wins()
        elif computer_input[1] == 2:
            computer_wins()
    # player chooses scissors
    elif player_input[1] == 2:
        if computer_input[1] == 0:
            computer_wins()
        elif computer_input[1] == 1:
            player_wins()

# function - computer randomly selects the choice
def get_computer_choice():
    return random.choice(options)

# gui section
game_window = Tk()
game_window.title("rock paper scissors")

# font settings
app_font = font.Font(font = "Times", size = 12)

# game_title
game_title = Label(text = "rock paper scissors", font = font.Font(size = 20), fg = "pink")
game_title.pack()

# winner label
winner_label = Label(text = "lets start the game !", font = font.Font(size = 18), fg = "pink", pady = 8)
winner_label.pack()

# input frame for buttons
input_frame = Frame(game_window)
input_frame.pack()

# player options
player_options = Label(input_frame, text = "your options", font = app_font, fg = "sky blue")
player_options.grid(row = 0, column = 0, pady = 8)

# buttons for the player
rock_btn = Button(input_frame, text = "rock", width = 15, bd = 0, bg = "sky blue", fg = "white", pady = 5, command = lambda:player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 5, pady = 8)

paper_btn = Button(input_frame, text = "paper", width = 15, bd = 0, bg = "pink", fg = "white", pady = 5, command  = lambda:player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 5, pady = 8)

scissor_btn = Button(input_frame, text = "scissors", width = 15, bd = 0, bg = "purple", fg = "white", pady = 5, command = lambda:player_choice(options[2]))
scissor_btn.grid(row = 1, column = 3, padx = 5 , pady = 8)

# score
score = Label(input_frame, text = "score", bg = "pink", fg = "white", pady = 5)
score.grid(row = 2, column = 1, padx = 5, pady = 8)

# player choice
player_choice_label = Label(input_frame, text = "you selected", font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = "your score is 0", font = app_font)
player_score_label.grid(row = 4, column = 1, pady = 5)

# computer choice
computer_choice_label = Label(input_frame, text = "the computer selected", font = app_font)
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = "computers score", font = app_font)
computer_score_label.grid(row = 4, column = 2, pady = 5)

# game window
game_window.geometry("700x400")

game_window.mainloop()