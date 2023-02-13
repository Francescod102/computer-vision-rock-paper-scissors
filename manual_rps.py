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
            print("You won! (Paper wraps Rock)") 
        elif user_choice=='Scissors':
            print("You lost! ( Rocke blunts Scissors)")

        
    if computer_choice=="Paper":


    
        if user_choice=='Rock': 
           print ("You lost! (Paper wraps Rock)")
        elif user_choice=="Paper":
             print ("it is a tie!") 
        elif user_choice=="Scissors": 
            print("You won! (Scissors cut Paper)") 


    if computer_choice=="Scissors":

        if user_choice=='Rock': 
            print("You won! (Rock blunts Scissors)")
        elif user_choice=="Paper": 
            print("You lost! (Scissors cut Paper)")
        elif user_choice=="Scissors":
            print ("it is a tie!")
    
print()


computer_choice = get_computer_choice()
print (computer_choice)
user_choice = get_user_choice()
    
print (get_winner(computer_choice,user_choice,))


def play ():
    play = (get_computer_choice,get_user_choice,get_winner)

    