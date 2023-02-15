import random
import cv2
from keras.models import load_model
import numpy as np
import time
from datetime import datetime

model = load_model("keras_model.h5")


def get_prediction():
    
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (
            image_np.astype(np.float32) / 127.0
        ) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow("frame", frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


#         # After the loop release the cap object
#         cap.release()
#         # Destroy all the windows
#         cv2.destroyAllWindows()


def get_computer_choice():
    move_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(move_list)
    return computer_choice


def get_user_choice():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return user_choice


computer_win = 0
user_win = 0


def get_winner(computer_choice, user_choice):
    winner = None
    if computer_choice == "Rock":
        if user_choice == "Rock":
            print("it is a tie!")

        elif user_choice == "Paper":
            print("You won!")
            winner = "computer"

        else:
            print("You lost")
            winner = "computer"

    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
            winner = "computer"

        elif user_choice == "Paper":
            print("it is a tie!")

        else:
            print("You won!")
            winner = "user"

    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
            winner = "user"

        elif user_choice == "Paper":
            print("You lost")
            winner = "computer"

        else:
            print("it is a tie!")

    return winner


computer_win = 0
user_win = 0
totalplay = 0
while computer_win < 3 and user_win < 3 and totalplay <5 :
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    winner = get_winner(computer_choice, user_choice)
    if winner == "computer":
        computer_win += 1
    elif winner == "user":
        user_win += 1
    print(computer_win, user_win)
    totalplay += 1



if computer_win > user_win:
    print("computer_win")
elif computer_win < user_win:
    print("user_win")
else:
    print ("It's a tie !!!")