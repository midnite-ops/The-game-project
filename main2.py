from tkinter import *
import random

game_events = {
    'rock': {'rock': 1, 'paper': 0, 'scissors': 2},
    'paper': {'rock': 2, 'paper': 1, 'scissors': 0},
    'scissors': {'rock': 0, 'paper': 2, 'scissors': 1}
}
computer_score = 0
player_score = 0
def outcome(user_guess):
    global computer_score
    global player_score
    options = ['rock', 'paper', 'scissors']
    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    
    result = game_events[user_guess][computer_choice]
    
    player_choice_label.config(fg='red', text = 'Player choice: '+str(user_guess))
    computer_choice_label.config(fg='green', text = 'Computer choice: '+str(computer_choice))
    
    if result == 2:
        player_score = player_score + 2
        player_result_label.config(text='Player: '+str(player_score))
        result_label.config(fg="blue", text='Outcome: Player won')
        
    elif result == 1:
        player_score = player_score + 1
        computer_score = computer_score + 1
        player_result_label.config(text='Player: '+str(player_score))
        computer_score_label.config(text='Computer: '+str(computer_score))
        result_label.config(fg="blue", text='Outcome: Draw')
        
    elif result == 0:
        computer_score = computer_score + 2
        computer_score_label.config(text='Computer: '+str(computer_score))
        result_label.config(fg="blue", text='Outcome: Computer won')
        
        

window = Tk()

window.title('The Game')

#Labels

Label(window , text = 'Rock, Paper, Scissors', font = ('Arial', 14)).grid(row = 0, sticky = N, pady = 10, padx = 200)

Label(window , text = 'Please select an option', font = ('Arial', 12)).grid(row = 1, sticky = N)

player_result_label = Label(window , text = 'Player : 0', font = ('Arial', 12))
player_result_label.grid(row = 2, sticky = W)

computer_score_label = Label(window , text = 'Computer : 0', font = ('Arial', 12))
computer_score_label.grid(row = 2, sticky = E)

player_choice_label = Label(window, font = ('Arial', 12))
player_choice_label.grid(row = 3, sticky = W)

computer_choice_label = Label(window, font = ('Arial', 12))
computer_choice_label.grid(row = 3, sticky = E)

result_label = Label(window, font = ('Arial', 12))
result_label.grid(row = 3, sticky = N)

#Buttons
Button(window, text = 'Rock', width = 10, command = lambda: outcome('rock')).grid(row = 4, sticky = W, pady = 5, padx = 5)

Button(window, text = 'Paper', width = 10, command = lambda: outcome('paper')).grid(row = 4, sticky = N, pady = 5,)

Button(window, text = 'Scissiors', width = 10, command = lambda: outcome('scissors')).grid(row = 4, sticky = E, pady = 5, padx = 5)

Label(window).grid(row=5)
window.mainloop()