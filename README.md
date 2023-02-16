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


# Milestone 5
## Task 1
Replace the hard-coded user guess with the output of the computer vision model. Create a new file called camera_rps.py where you will write the new code.
Create a new function called get_prediction that will return the output of the model you used earlier.
Remember that the output of the model you downloaded is a list of probabilities for each class. You need to pick the class with the highest probability. So, for example, assuming you trained the model in this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that you showed "Rock" to the camera with a confidence of 0.8.The model can make many predictions at once if given many images. In your case you only give it one image at a time. That means that the first element in the list returned from the model is a list of probabilities for the four different classes. Print the response of the model if you are unclear of this.

## Task 2
In the previous task, the script reads the input from the camera and then compares it with the computer's choice without stopping. However, when you play a regular game, you usually count down to zero, and at that point you show your hand.In this case, you need to add that countdown. An important thing to remember is that you can't use the sleep function because it will stop the script, and during that time, the camera will not be able to capture the input.
Use the function time.time() to get how much time has passed since the script started. Print, for example, "you chose rock" in the terminal when the countdown gets to zero.


## Task 3
The game should be repeated until either the computer or the user wins three rounds.
Feel free to code the logic as you want, but make sure you defined at least two variables to keep track of the score of the computer and the user. Name them computer_wins and user_wins respectively. using while loop capturing and shwoing your image. 

## Task 5
Readme.jpg
Talk about how you integrated your game with the model, also talk about what more you could have done to improve the functionality of the game.
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera