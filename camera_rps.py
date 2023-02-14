import cv2
from keras.models import load_model
import numpy as np

def get_prediction():  
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

print (get_prediction())


import time
from datetime import datetime

script_start_time = datetime.now()

for i in range(100000):
    j = 10 + i

end_time = time.time()
final_time = end_time + script_start_time
print ( final_time)

script_end_time = datetime.now()
print(script_end_time +script_start_time)

