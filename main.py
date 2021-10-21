#this code is from this video --> https://www.youtube.com/watch?v=1J8dQA6gN7k
import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

#Get the device resolution
width = GetSystemMetrics(0) #pass 0 to et the width
height = GetSystemMetrics(1) #pass 1 to get the height

#File name based on recording time
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

#Encoding dan thecoding the video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height)) #name of the file, the decoding &encoding, frame rate, resulotion

#if you want to record urself using ur device camera
webcam = cv2.VideoCapture(0) #0 means the camera taht build in on ur device, if this not working increase the number

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) #color corecting
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape #to get the webcam dimension
    img_final[0:fr_height, 0:fr_width, :] = frame[0: fr_height, 0: fr_width, :] #overlaying the webcam to the captured video
    cv2.imshow('Screen Recorder', img_final)
    #cv2.imshow('webcam', frame) --> u don't need this bcz u already overlaying it on top of the recorded screen
    capture_video.write(img_final)
    if cv2.waitKey(10) == ord('s'): #to stop recording press s
        break
