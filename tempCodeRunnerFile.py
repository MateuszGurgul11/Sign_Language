import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
img_size = 500

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']

while True:
    succes, img = cap.read()
    img_output = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        img_white = np.ones((img_size, img_size, 3), np.uint8) * 255
        img_crop = img[y-offset:y + h + offset, x-offset:x + w + offset]
        img_crop_shape = img_crop.shape
        
        aspect_ratio = h / w

        if aspect_ratio > 1:
            konstant = img_size/h
            w_cal = math.ceil(konstant * w)
            img_resize = cv2.resize(img_crop, (w_cal, img_size))
            img_resize_shape = img_resize.shape
            w_gap = math.ceil((img_size - w_cal)/2)
            img_white[:, w_gap:w_cal + w_gap] = img_resize
            prediction, index = classifier.getPrediction(img_white, draw=False)
            print(prediction, index)

        else:
            konstant = img_size / w
            h_cal = math.ceil(konstant * h)
            img_resize = cv2.resize(img_crop, (img_size, h_cal))
            img_resize_shape = img_resize.shape
            h_gap = math.ceil((img_size - h_cal) / 2)
            img_white[h_gap:h_cal + h_gap, :] = img_resize
            prediction, index = classifier.getPrediction(img_white, draw=False)

        cv2.rectangle(img_output, (x - offset, y - offset - 70), (x - offset + 130, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
        cv2.putText(img_output, labels[index], (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 4)
        cv2.rectangle(img_output, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 3)

        cv2.imshow("image_crop", img_crop)
        cv2.imshow("image_white", img_white)

    cv2.imshow('Image', img_output)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break