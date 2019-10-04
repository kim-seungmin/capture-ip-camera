import time
import cv2
import socket
import os
import RPi.GPIO as GPIO
####################         cameraUDP_header        ######################
#recording
#url = 'rtsp://CVCam.iptime.org:554/profile2/media.smp'
url = 'rtsp://admin:88888888@172.24.1.63:10554/tcp/av0_0'
capture = cv2.VideoCapture(url)
#capture2 = cv2.VideoCapture(url2)
fourcc = cv2.VideoWriter_fourcc(*'H264')
#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#LED
###########################################################################



#####################        pirUDP_header          #######################
GPIO.setmode(GPIO.BCM)
pir_pin = 26
GPIO.setup(pir_pin, GPIO.IN)
time.sleep(30)

###########################################################################


def loop():
    while True:
        if GPIO.input(pir_pin) == True:
#_______________________mix cameraUDP ____________________________________#
            selectFlag = 0
            now = time.localtime()
            date = "%04d-%02d-%02d_%02d-%02d:%02d_cam1" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            sock.sendto("cam1".encode(),('127.0.0.1',10001))
            os.system('sudo python /home/pi/Raspberry_Pi/led.py &')
            #video = cv2.VideoWriter("/home/pi/Raspberry_Pi/h.mp4", fourcc, 10.0, (640, 360))
            video = cv2.VideoWriter("/home/pi/Raspberry_Pi/h1.mp4", fourcc, 10.0, (640, 360))
            capture = cv2.VideoCapture(url)
            #capture2 = cv2.VideoCapture(url2)
            while(selectFlag!=300):
                ret, frame = capture.read()
            #    ret2, frame2 = capture2.read()
                #if(ret and ret2):
                selectFlag+=1
                frame = cv2.resize(frame,(640, 360), interpolation = cv2.INTER_AREA)
                video.write(frame)
            #    video2.write(frame2)
            video.release() #memory clear
            #video2.release()
            capture.release()
            #capture2.release()
            os.system('sudo mv /home/pi/Raspberry_Pi/h1.mp4 /usr/local/tomcat9/webapps/TheftPrevention/video/%s.mp4' %date)#here
            #os.system('sudo mv /home/pi/Raspberry_Pi/h1.mp4 /home/pi/Raspberry_Pi/video/%s.mp4' %date)
            #os.system('sudo mv /home/pi/Raspberry_Pi/h1.mp4 /usr/local/tomcat9/webapps/TheftPrevention/video/%s.mp4' %date)#here 
            #os.system('sudo mv /home/pi/Raspberry_Pi/h1.mp4 /usr/local/tomcat9/webapps/TheftPrevention/video/%s_2.mp4' %date)#here %s -> %s_2
            time.sleep(1)
            #value = '0'
            selectFlag=0
        #else
#_________________________________________________________________________# 
        else:
            time.sleep(1)

try :
    loop()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    capture.release()
    cv2.destroyAllWindows()
