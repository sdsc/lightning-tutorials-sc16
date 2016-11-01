import numpy as np
import cv2
import time
import Dialog
import glob
import itertools
import sys

def main():

  #set up path to face detection parameters
  path4opencv                ='./haarcascades'
  face_cascade_path          = path4opencv+'/haarcascade_frontalface_alt.xml'
  eye_cascade_path           = path4opencv+'/haarcascade_eye.xml'

  #set up object for pre-trained classifier object 
  #  the recognition works to find most relevant image features first
  #  as it scans the image,
  #  then 'cascades' to a larger and/or specific set of features 
  face_cascade          = cv2.CascadeClassifier(face_cascade_path)
  eye_cascade           = cv2.CascadeClassifier(eye_cascade_path)
  
  print 'starting...'

  with open('ImageList.txt','r') as infile:
    for filename in infile:
        filename=filename.rstrip()
        filename=filename.rstrip('\n')
        print 'reading '+filename
        img  = cv2.imread('./'+filename,cv2.IMREAD_GRAYSCALE)
        gray = cv2.equalizeHist(img)
        #gray =cv2.cvtColor(imgeq, cv2.COLOR_BGR2GRAY)  #use grayscale if its color

        #call detect function
        faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(75,75), flags=cv2.CASCADE_SCALE_IMAGE)

        numfaces=len(faces)
        #check for eyes and show the face to user
        for face in faces:
              print 'a face found ...'
              [x, y, w, h]=face  
              print 'size width:'+str(w)+" height:"+str(h)
              cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),4)
              roi_gray    =gray[y:y+h,x:x+w]
              eyes        =eye_cascade.detectMultiScale(roi_gray)
              if len(eyes)==2:
                  print '2 eyes found ...'
                  for (ex,ey,ew,eh) in eyes:    
                      cv2.rectangle(gray,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(255,0,0),4)
        
        cv2.namedWindow('FSA_depression_era_Photo')
        cv2.imshow('FSA_depression_era_Photo',gray)
        cv2.waitKey(200)
        dial_res=Dialog.Dialog(title='Found'+str(numfaces)+' faces',
                        text='do you want to:',
                        bitmap='questhead',
                        default=0,
                        strings=('try next image','Quit'))
        if dial_res.num==1:
                     print '.. stopping'
                     exit()
        else:
                     cv2.destroyWindow('FSA_epression_era_Photo')
                     cv2.waitKey(1)
                     print 'about to start again in 1 sec...'

  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    


