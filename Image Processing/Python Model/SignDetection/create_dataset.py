import os
import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

#initialize hand tracking module from Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

#Hands object for static image mode -- min detection confidence = 0.3
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

#lists for processed hand landmarks (data) and corresponding labels
data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []
        #lists for normalized x and y coordinates of hand landmarks
        x_ = []
        y_ = []

        #convert read image to RGB format
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #plt.figure()
        #plt.imshow(img_rgb)

        #process image to detect hand landmarks
        results = hands.process(img_rgb)
        #iterate through detected hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #extract x and y coordinates of each hand landmark
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    #append normalized coordinates to respective lists
                    x_.append(x)
                    y_.append(y)

                #subtract min value to normalize coordinates
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            #append normalized landmarks data and label
            data.append(data_aux)
            labels.append(dir_)
#save the processed data and labels to a pickle file
# with open('data.pickle', 'wb') as f:
#     pickle.dump({'data': data, 'labels': labels}, f)

f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
