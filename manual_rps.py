from random import choice

def get_computer_choice():
    return choice(["Rock", "Paper", "Scissors"])

def get_user_choice ():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return(user_choice)

def get_winner(computer_choice, user_choice):
    if computer_choice  == 'Rock' and user_choice == 'Paper':
       return "You won"
    elif computer_choice == "Rock" and user_choice == "Scissors":
       return "You lost"
    elif computer_choice == "Rock" and user_choice == "Rock":
        return "it's a tie"
    
    if computer_choice  == 'Scissors' and user_choice == 'Rock':
       return "You won"
    elif computer_choice == "Scissors" and user_choice == "Paper":
       return " You lost"
    elif computer_choice == "Scissors" and user_choice == "Scissors":
        return "it's a tie"
    
    if computer_choice  == 'Paper' and user_choice == 'Scissors':
       return "You won"
    elif computer_choice == "Paper" and user_choice == "Rock":
       return "You Lost"
    elif computer_choice == "Paper" and user_choice == "Paper":
        return "it's a tie"
    



computer_choice = get_computer_choice()
user_choice = get_user_choice()
    
print (get_winner(computer_choice,  user_choice))