import os
import datetime
from datetime import tzinfo
# from datetime import timezone
import math
from picamera import PiCamera
from time import sleep
import time


# Enter the path where the raspberry pi will store its file
RASPI_PATH = "/home/pi"

INTERVAL = 5 # the time interval (in seconds) between pictures
SESSION_LENGTH = 1100# the duration of the script

camera = PiCamera()
camera.start_preview()
# Have the camera take pictures at the specified interval until the session is over

#this creates a folder everytime we start the camera so we can have a collection per run- the folder is named after the start date and time
# datetime.timezone.tzname("EDT")
now = datetime.datetime.now()
str_now = now.strftime("%m-%d-%Y-%H:%M:%S")

os.mkdir('{}/{}'.format(RASPI_PATH, str_now))

FOLDERCREATED = '{}/{}'.format(RASPI_PATH, str_now)

#inside the () is the number of photos taken
for i in range(SESSION_LENGTH/INTERVAL):
	time.sleep(INTERVAL)
	#this captures an image and saves into the FOLDERCREATED, the images are named image(i).jpg
	camera.capture('{}/image{}.jpg'.format(FOLDERCREATED, i))

camera.stop_preview()

