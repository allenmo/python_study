#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
import os
import commands

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

readyLED = 11
inprocessLED = 13
passLED = 15
failLED = 37
startButton = 7

GPIO.setup([readyLED, inprocessLED, passLED, failLED], GPIO.OUT, initial=GPIO.HIGH)
time.sleep(0.3)
GPIO.output(readyLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(inprocessLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(passLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(failLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(failLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(passLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(inprocessLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(readyLED, GPIO.HIGH)
time.sleep(0.3)
for i in range(0,6):
    GPIO.output(readyLED, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(readyLED, GPIO.HIGH)
    time.sleep(0.1)
GPIO.output(readyLED, GPIO.LOW)

def button_pressed_callback(channel):
    print "Start Button pressed!"
    GPIO.output(inprocessLED, GPIO.LOW)
    GPIO.output(passLED, GPIO.HIGH)
    GPIO.output(failLED, GPIO.HIGH)
    subprocess.call('/home/pi/jlink/jlink/1.sh', shell=True)
    #subprocess.Popen('./1.sh', shell=True)
    #subprocess.Popen('./1.sh', stdout=subprocess.PIPE, shell=True)
    GPIO.output(inprocessLED, GPIO.HIGH)
    GPIO.output(passLED, GPIO.LOW)
    GPIO.output(failLED, GPIO.HIGH)


GPIO.setup(startButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(startButton, GPIO.RISING, callback=button_pressed_callback, bouncetime=400)

while True:
    #print "in loop"
    time.sleep(0.5)
