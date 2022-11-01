from tokenize import String
import cv2 as cv
from cv2 import aruco
import numpy as np
import serial
import time
arduino=serial.Serial(port='COM5',baudrate=115200)
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture(0)


def write_read(x):
    arduino.write(x)
    time.sleep(0.05)
    data=arduino.readline()
    return data

                    
while True:
    
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    id =(marker_IDs)
    print(id)
    # arduino.write(bytes(id,'utf-8'))
    # arduino.write(id)

    
    # print(value)
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv.polylines(
                frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()
            cv.putText(
                frame,
                f"id: {ids[0]}",
                top_right,
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (200, 100, 0),
                2,
                cv.LINE_AA,
            )
            # print(ids, "  ", corners)
    




    # a=shopping(id)
    # print (a)
    # if (a>0):
    #     break

    #         ques=input("do you want to continue? type 'y' or 'n' :")
    # if ques=='y':
    #     id=int(input("enter the id"))
    #     continue
    # else:
    #     break
    if id is not None:
        print(type(id))
        a=id.tobytes()
        print(type(a))
        write_read(a)
    cv.imshow("Frame",frame)
    key=cv.waitKey(1)
    if key==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()