import numpy as np
import cv2
import time
import Dialog

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

  #Make a loop to grab image from cam and see if a face is there
  keepgoing=True
  while(keepgoing):
      print 'capturing ...'

      #set up video object
      cap=cv2.VideoCapture(0)
      ret,frame=cap.read()     #grab the cam image, take 2nd one in buffer
      ret,frame=cap.read()
      cap.release()
      while ret==True:         #one way to clear buffer (depends on camera)
          ret,dummyframe=cap.read()

      gray     =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #use grayscale

      #call detect function
      faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(75,75), flags=cv2.CASCADE_SCALE_IMAGE)

      #check for eyes and show the face to user
      if len(faces)>0:
          print 'face found ...'
          [x, y, w, h]=faces[0]
          print 'size width:'+str(w)+" height:"+str(h)
          cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),4)
          roi_gray    =gray[y:y+h,x:x+w]
          eyes        =eye_cascade.detectMultiScale(roi_gray)
          if len(eyes)==2:
              print 'eyes found ...'
              for (ex,ey,ew,eh) in eyes:
                  cv2.rectangle(gray,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(255,0,0),4)

              cv2.namedWindow('you?')
 #             cv2.startWindowThread()
              cv2.imshow('you?',gray)
              cv2.waitKey(200)
              dial_res=Dialog.Dialog(title='Face Detected',
                        text='do you want to:',
                        bitmap='questhead',
                        default=0,
                        strings=('Try another face shot','Quit'))
              if dial_res.num==1:
                     keepgoing=False
                     print '.. stopping'
              else:
                     cv2.destroyWindow('you?')
                     cv2.waitKey(1)
                     print 'about to start again in 3 secs...'
                     time.sleep(3)
          else:
              print 'no eyes.. wait a sec'
              time.sleep(1)
      else:
          print 'no face found - wait a sec...'
          #cv2.imshow('...',gray)
          #cv2.waitKey(200)
          time.sleep(1)

  cv2.destroyAllWindows()
  cap.release()
if __name__ == '__main__':
    main()
