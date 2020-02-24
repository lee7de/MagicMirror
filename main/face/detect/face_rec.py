#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/2/12 20:45

import cv2
import numpy as np

def face_detection(image):
    # 从灰度图找到人脸的位置
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    path = "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(path)
    faces = face_detector.detectMultiScale(gray, 1.1, 2)

    # 在原图上标记出人脸
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    cv2.imshow("result", image)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_detection(frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
