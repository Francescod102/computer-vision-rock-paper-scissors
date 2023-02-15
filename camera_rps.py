import random
import cv2
from keras.models import load_model
import numpy as np
import time
from datetime import datetime



move_list = ["Rock", "Paper", "Scissors", "Nothing"]

def task_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        cap.release() 
        cv2.destroyAllWindows()

    
def get_prediction():
    model = load_model("keras_model.h5")
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    while time.time() < start_time + 10:
        count_down = str(int(start_time + 10 - time.time()))

        ret, frame = cap.read()
        # frame_test= np.array(frame)
        # frame_test.shape

        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        prediction = move_list[np.argmax(prediction)]
        # cv2.putText(frame, "user_choise",(50,50),cv2.FRONY_HERSHEY_PLAIN,5,(255,50,50),4)
        # cv2.putText(frame, count_down,(150,150),cv2.FRONY_HERSHEY_PLAIN,5,(255,50,50),4)
        cv2.imshow("frame", frame)
        # Press q to close the window
        # print(prediction)
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

         # After the loop release the cap object
    cap.release()
        # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction


def get_computer_choice():
     move_list = ["Rock", "Paper", "Scissors"]
     computer_choice = random.choice(move_list)
     return computer_choice


def get_user_choice():
     user_choice = get_prediction()
     return user_choice


def get_winner():
    computer_win = 0
    user_win = 0
    totalplay = 0
    while computer_win < 3 and user_win < 3:

        computer_choice = random.choice(move_list[:3])
        user_choice = get_prediction()
        print("usr =", user_choice, "comp = ", computer_choice)
        # cv2.putText(frame,f"{user_choice}-{computer_choice}",)
        totalplay += 1
        if computer_choice == user_choice:
            print("It is a tie")
            winner = "tie"
        elif (computer_choice == "Rock" and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Paper" and user_choice == "Rock"):
            print("You lost!")
            winner = "compute_choicer"
            computer_win += 1

        else:
            print("You lost")
            winner = "user_choice"
            user_win += 1

        # return winner
    if computer_win == 3:
        print("computer_win")
    elif user_win == 3:
        print("user_win")
    else:
        print("you lost!")

        return winner
    
get_winner()
task_camera()


#     elif computer_choice == "Paper":
#         if user_choice == "Rock":
#             print("You lost")
#             winner = "computer"

#         elif user_choice == "Paper":
#             print("it is a tie!")

#         else:
#             print("You won!")
#             winner = "user"

#     elif computer_choice == "Scissors":
#         if user_choice == "Rock":
#             print("You won!")
#             winner = "user"

#         elif user_choice == "Paper":
#             print("You lost")
#             winner = "computer"

#         else:
#             print("it is a tie!")

#     return winner


# computer_win = 0
# user_win = 0
# totalplay = 0
# while computer_win < 3 and user_win < 3 and totalplay <5 :
#     computer_choice = get_computer_choice()
#     user_choice = get_user_choice()

#     winner = get_winner(computer_choice, user_choice)
#     if winner == "computer":
#         computer_win += 1
#     elif winner == "user":
#         user_win += 1
#     print(computer_win, user_win)
#     totalplay += 1

# if computer_win ==3():
#     print("computer_win")
# elif computer_win < user_win:
#     print("user_win")
# else:
#     print ("It's a tie !!!")
