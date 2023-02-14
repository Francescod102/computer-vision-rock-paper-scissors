import random

def get_computer_choice():
    move_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(move_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return user_choice

     
def get_winner(computer_choice,user_choice):
    if computer_choice== user_choice:
        print('It is a tie!')
    elif computer_choice=='Rock' and user_choice=='Paper':
        print('You won!')  
    elif computer_choice=='Paper' and user_choice=='Scissors':
        print('You won!')
    elif  computer_choice=="Scissors" and user_choice=='Rock':
        print ('You won!') 
    else:
        print('You lost') 


computer_choice = get_computer_choice()
print (computer_choice)
user_choice = get_user_choice()

print (get_winner (computer_choice ,user_choice,))
    
def play ():
        play = (get_computer_choice,get_user_choice,get_winner)
        
                        
                        