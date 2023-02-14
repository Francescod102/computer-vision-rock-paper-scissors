import random

def get_computer_choice():
    move_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(move_list)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return user_choice

computer_win = 0
user_win  = 0
       
def get_winner(computer_choice,user_choice):
    winner = None 
    if computer_choice=='Rock':

        if user_choice=='Rock':
            print("it is a tie!")
        
        elif user_choice=='Paper':
            print('You won!')
            winner = "computer"
            
        else:
            print("You lost")
            winner = 'computer'
            

    elif  computer_choice=="Paper":

        if user_choice=='Rock': 
            print ("You lost")
            winner = 'computer'
            
        elif user_choice=="Paper":
            print ("it is a tie!") 
            
        else:
            print("You won!") 
            winner = 'user'
            
    elif computer_choice=='Scissors':
        
        if user_choice=='Rock': 
            print("You won!")
            winner ='user'
            

        elif user_choice=="Paper": 
            print("You lost")
            winner = 'computer'
           
        else:
            print ("it is a tie!")
              
    return winner

computer_win = 0
user_win = 0

while computer_win < 3 and user_win < 3 :
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    winner = get_winner(computer_choice, user_choice)
    if winner == 'computer': 
        computer_win +=1
    elif winner == "user" :
        user_win +=1
    print(computer_win,user_win)
if computer_win > user_win :
    print("computer_win")
elif computer_win < user_win :
    print('user_win')

    # user_continues = input ("Do you want to play ?( y/n)")
# if user_choice in ['Yes']:
#     pass
# elif user_choice in ['No']:
#     else:
#     break

    # computer_choice = get_computer_choice()
    # print (computer_choice)
    # user_choice = get_user_choice()

    # print (get_winner (computer_choice ,user_choice,))
    
# def play ():
#         play = (get_computer_choice,get_user_choice,get_winner)
        