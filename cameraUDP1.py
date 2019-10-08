import cv2
import os

rtsp = 'ur rtsp'
capture = cv2.VideoCapture(rtsp)
fourcc = cv2.VideoWriter_fourcc(*'H264')
try :
    selectFlag = 0
    video = cv2.VideoWriter("./ipcamcap.mp4", fourcc, 10.0, (640, 360))
    capture = cv2.VideoCapture(url)
    while(selectFlag!=300):
         ret, frame = capture.read()
         selectFlag+=1
         frame = cv2.resize(frame,(640, 360), interpolation = cv2.INTER_AREA)
         video.write(frame)
    video.release() #memory clear
    capture.release()

except KeyboardInterrupt:
    pass

finally:
    capture.release()
    cv2.destroyAllWindows()
