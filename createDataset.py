import os
import numpy as np
import string
import cv2

    #  The main aim of this file is create a GUI It enables the webcam, 
    #  which takes inputs for training dataset and the testing dataset
    
    
    #  Asking the user to chose which type of dataset he wants to create

print("\nPress A or B as Follows:")
print('\nA. Training Data')
print('B. Testing Data\n')

dataType = input()

    #  Initializing the GUI of Chosen Dataset-Type Window

directory = 'dataset'

if dataType == 'A':
    directory = directory + '/Training Data/'
    print('\nInitializing the Training Dataset Creation GUI\n')
    
elif dataType == 'B':
    directory = directory + '/Testing Data/'
    print('\nInitializing the Testing Dataset Creation GUI\n')
    
else:
    print('Try again !!')
    
    #  If user enters either A or B, then following code snippet will run
    
if(dataType == 'A' or dataType == 'B'):
    
    
    commandReceived = -1        #  Variable to take input every time from user what character gesture represents
    cap = cv2.VideoCapture(0)   #  Starting Capturing the Video Through webcam
    
    while True:
        
        keepCapturingGesture, gestureFrame = cap.read()
        
        #  We will flip the geature image captured by the system to get user friendly environment
        
        gestureFrame = cv2.flip(gestureFrame, 1)
        
        #  Now storing the count of total geature images in each character in each dataset folder
        
        count = {}
        
        for character in string.ascii_lowercase:
            count[character] = len(os.listdir(directory + "/" + str(character)))
            
        #  Now defining the parameters for the size, location etc of the Gesture Input Webcam Window
            
        x1 = int(0.5*gestureFrame.shape[1])
        y1 = 10
        x2 = gestureFrame.shape[1]-10
        y2 = int(0.5*gestureFrame.shape[1])
        cv2.rectangle(gestureFrame, (220, 9), (621, 200), (255,0,0) ,1)
        roi = gestureFrame[10:410, 220:520]
    
        cv2.imshow("Gesture Window", gestureFrame)
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(gray,(5,5),2)
        th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, testingData_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        testingData_image = cv2.resize(testingData_image, (300,300))
        cv2.imshow("Data Creation", testingData_image)
        
        
        #  Now checking if any key pressed by the user matches any character or not
        
        commandReceived = cv2.waitKey(7)
        
        #  If key pressed is esc, it tells the system to stop capturing gestures

        if commandReceived & 0xFF == 27:
            break
        
        #  Else, hunt if the key pressed matches any alphabet, 
        #  store the captured gesture in the folder of that lphabet
        
        for character in string.ascii_lowercase:
            if commandReceived & 0xFF == ord(character):
                temp = character
                folder = str(temp)
                newGesturePath = directory + folder.upper() + '/' + "Image " + str(count[character]) + '.jpg'
                print("Image Captured For Character : " + str(temp).upper() + "\n")
                cv2.imwrite(newGesturePath , testingData_image)
                
        #  After the work is done, we will destroy all the windows 

    cap.release()
    cv2.destroyAllWindows()
    
    print('\n====================================\n')
    print('Gesture Window Cleared Successfully!!')
    print('\n====================================\n')

