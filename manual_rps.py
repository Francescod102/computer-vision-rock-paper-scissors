import random

def get_computer_choice():
    move_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(move_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return(user_choice)

def get_winner(computer_choice, user_choice):
    if computer_choice=='Rock':

        if user_choice=='Rock':
            print("it is a tie!")
        elif user_choice=='Paper':
            print('You won!')
        else:
            print("You lost")

    elif  computer_choice=="Paper":

        if user_choice=='Rock': 
            print ("You lost")
        elif user_choice=="Paper":
            print ("it is a tie!") 
        else:
            print("You won!") 


        
    elif computer_choice=='Scissors':
         
        if user_choice=='Rock': 
            print("You won!")
        elif user_choice=="Paper": 
            print("You lost")
        else:
            print ("it is a tie!")
            
    
print()


computer_choice = get_computer_choice()
print (computer_choice)
user_choice = get_user_choice()
    
print (get_winner(computer_choice,user_choice,))


def play ():
    play = (get_computer_choice,get_user_choice,get_winner)

    