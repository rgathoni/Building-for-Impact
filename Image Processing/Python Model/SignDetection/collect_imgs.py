import os
import cv2
#introduce delay after 'Q' is pressed
import time

DATA_DIR = './data' ##collected data directory

#create data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#count of signs to be collected
number_of_classes = 24
#count of images per class to be collected
dataset_size = 35

cap = cv2.VideoCapture(0) #open webcam
for j in range(number_of_classes):
    #create subdirectory for current class -- if it doesn't exist
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for signs {}'.format(j))

    #signal from user to start capturing -- press Q
    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            start_time = time.time()  # Record the time when 'Q' is pressed
            break
    #press Q to break loop

    #capture and save frames as images
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if time.time() - start_time > 5:  # Check if 5 seconds have passed
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

            counter += 1

#release webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
