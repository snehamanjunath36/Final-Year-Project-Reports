import time
import RPi.GPIO as GPIO
import pytesseract
import pyttsx3
import cv2
from PIL import Image
from pytesseract import Output
import imutils
import subprocess
def imagetts():
    cam= cv2.VideoCapture(-1)
    while True:
        ret,image=cam.read()
        cv2.imshow('imagetest',image)
        k=cv2.waitKey(1)
        if k!=-1:
            break
    cv2.imwrite('/home/sneha/testimg.jpg',image)
    cam.release()
    cv2.destroyAllWindows()

    
GPIO.setmode(GPIO.BOARD)
delayt=.1
value=0
ldr=7
led=11
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)
def rc_time(ldr):
    count=0
    GPIO.setup(ldr,GPIO.OUT)
    GPIO.output(ldr,False)
    time.sleep(delayt)
    GPIO.setup(ldr,GPIO.IN)
    
    while(GPIO.input(ldr)==0):
        count+=1
    return count

try:
#     while True:
    print("ldr value:")
    value=rc_time(ldr)
    print(value)
    if(value<=11000):
        print('lights are off')
        GPIO.output(led,False)
        imagetts()
    if(value>11000):
        print('lights are on')
        GPIO.output(led,True)
        imagetts()
finally:
    GPIO.cleanup()
    
def execute_unix(inputcommand):
       p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
       (output, err) = p.communicate()
       return output

# imagesss='/home/sneha/testimg.jpg'
        #image=cv2.imread(imagesss)
image = cv2.imread('/home/sneha/testimg.jpg')
cv2.imshow('me',image)
        #rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_osd(image, output_type=Output.DICT)
        # display the orientation information
a=results["rotate"]
print('rotation degree:' +str(a))

engine = pyttsx3.init()
if a==180:
    a = "hold the image upright"
    c = 'espeak -ven+f3 -k5 -s120--punct="<characters>" "%s" 2>>/dev/null' % a 
    execute_unix(c)
elif a==90:
    a = "turn the object 90 degree in anticlock-wise direction."
    c = 'espeak -ven+f3 -k5 -s120 --punct="<characters>" "%s" 2>>/dev/null' % a 
    execute_unix(c)
elif a==270:
    a = "turn the object 90 degree in clock-wise direction."
    c = 'espeak -ven+f3 -k5 -s120 --punct="<characters>" "%s" 2>>/dev/null' % a 
    execute_unix(c)
else:
    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    image_path = r'/home/sneha/testimg.jpg'
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    c = 'espeak -ven+f3 -k5 -s100 --punct="<characters>" "%s" 2>>/dev/null' % text 
    execute_unix(c)



# except keyboardinterrupt:
  #  pass
# text='hello'
# k=  'espeak --voices=uk -ven+f3 -k5 -s120 --punct="<characters>" "%s" 2>>/dev/null' % text 
#                                                      execute_unix(k)
    



 
 
 
 
 
 
 
 
 
 
 