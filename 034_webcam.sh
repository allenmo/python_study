#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
fswebcam -r 640x480 --no-banner ~/webcam/$DATE.jpg
#fswebcam -r 1024x768 --no-banner ~/webcam/$DATE.jpg
#fswebcam -r 1920x1080 --no-banner ~/webcam/$DATE.jpg
#fswebcam -r 2560x1440 --no-banner ~/webcam/$DATE.jpg

