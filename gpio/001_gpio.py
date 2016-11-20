import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
print hex(mode), mode

GPIO.setwarnings(False)

print GPIO.RPI_INFO
print GPIO.RPI_INFO['P1_REVISION']
print GPIO.RPI_REVISION
print GPIO.VERSION

# GPIO 11 pin of BOARD, output
channel = 11
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
for i in range(0,10):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.3)

# GPIO 7 pin of BOARD, input
inChannel = 7
GPIO.setup(inChannel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for i in range(0,30):
    print GPIO.input(inChannel)
    time.sleep(0.3) 

waitChannel = GPIO.wait_for_edge(inChannel, GPIO.RISING, timeout=5000)
if waitChannel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel ', waitChannel)

def button_pressed_callback(channel):
    print "button pressed"

GPIO.remove_event_detect(inChannel)
GPIO.add_event_detect(inChannel, GPIO.RISING, callback = button_pressed_callback, bouncetime=200)

while True:
    print "in loop"
    time.sleep(2)
