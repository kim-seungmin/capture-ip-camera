import cv2
import os
#____________________________________________ cameraUDP_header ____________________________________________#
url = 'rtsp://admin:88888888@172.24.1.63:10554/tcp/av0_0'
capture = cv2.VideoCapture(url)
fourcc = cv2.VideoWriter_fourcc(*'H264')
#__________________________________________________________________________________________________________#  


#________________________________________________ cameraUDP ________________________________________________#
try :
    selectFlag = 0
    video = cv2.VideoWriter("/home/pi/Raspberry_Pi/ipcamcap.mp4", fourcc, 10.0, (640, 360))
    capture = cv2.VideoCapture(url)
    while(selectFlag!=300):
         ret, frame = capture.read()
         selectFlag+=1
         frame = cv2.resize(frame,(640, 360), interpolation = cv2.INTER_AREA)
         video.write(frame)
    video.release() #memory clear
    capture.release()
#__________________________________________________________________________________________________________#  

except KeyboardInterrupt:
    pass

finally:
    capture.release()
    cv2.destroyAllWindows()
