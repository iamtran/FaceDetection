import numpy as np
import os
import sys
import cv2
import matplotlib.pyplot as plt
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        #print("Hostname :  ",host_name) 
        #print("IP : ",host_ip) 
        host_str = "Hostname :  " + host_name + "              IP : " + host_ip
        #print (host_str)
        return (host_str)
    except: 
        print("Unable to get Hostname and IP") 
        host_str = "Hostname :  " + "Unknown" + "IP : " + "Unknown"
        return (host_str)
  
# Driver code 
#face_cascade = cv2.CascadeClassifier('/home/tiff/OpenCV/data/haarcascades/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/home/tiff/OpenCV/data/haarcascades/haarcascade_eye.xml')
root='/opt/services/flaskapp/src/'
face_cascade = cv2.CascadeClassifier(root+'./OpenCV/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(root+'./OpenCV/data/haarcascades/haarcascade_eye.xml')

def read_image_file_2_detect (filename):
    img = cv2.imread(filename)
    #print(">>>> DEBUG", os.getcwd())
    #print (root+'./OpenCV/data/haarcascades/haarcascade_eye.xml')
    #print(os.path.exists(root+'/OpenCV/data/haarcascades/'))
    #x= os.listdir(root+'/OpenCV/data/haarcascades/')
    #x= os.listdir(root)
    #print (x)
    #print(sys.version)
    #return ((img))
    #host_str = get_Host_name_IP() #Function call 
    return (face_detection (img))


def write_image_2_file (image, outfile):
    cv2.imwrite(outfile, image)
    img = cv2.imread(outfile)
    return img

def face_detection (img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    return img

# Python3 code to display hostname and 
# IP address 
  
# Importing socket library 
import socket 
  
# Function to display hostname and 
# IP address 
