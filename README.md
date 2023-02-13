# Computer Vision RPS
--trained a model :on Go to Teachable-Machine  to start creating the model. Each class is trained with images of yourself showing each option to the camera. The "Nothing" class represents the lack of option in the image. Remember that the more images you train with, the more accurate the model will be 
Make sure you push the model and labels to your GitHub repository after committing.
--explian what you did when you trained the model :from the "Tensorflow" tab in Teachable-Machine. The model should be named keras_model.h5 and the text file containing the labels should be named labels.txt.
The files you are downloading contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. 
Later, you will load them into your Python application in the next milestone.<how you went about it>
--created a githiub repo so i can track my work throuhgout the project <name of repo>
-- published the changes to github 

# Milestone 4
## Task 1
This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
Create another file called manual_rps.py that will be used to play the game without the camera.
You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
Create two functions: get_computer_choice and get_user_choice.
The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
The second function will ask the user for an input and return it.

## Task 2
Using if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors.
For example, if the computer chooses rock and the user chooses scissors, the computer wins.
Wrap the code in a function called get_winner and return the winner.
This function takes two arguments: computer_choice and user_choice.
If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".

## Task 3
All of the code you've programmed so far relates to one thing: running the game - so you should wrap it all in one function.
Create and call a new function called play.
Inside the function you will call all the other three functions you've created (get_computer_choice, get_user_choice, and get_winner)
Now when you run the code, it should play a game of Rock-Paper-Scissors, and it should print whether the computer or you won.
