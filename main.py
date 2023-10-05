
import cv2
import time
from pinDef import *

# Define GPIO pinds for button input

# Mode_Button = 17 # GPIO pin that swaps from manual to auto mode
# Led_Pin = 18 # GPIO pin that controls the LED

# # GPIO settings 
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(Mode_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(Led_Pin, GPIO.OUT)

# States 
AUTO_MODE = 0
MANUAL_MODE = 1
mode = AUTO_MODE

def toggle_mode(channel):
    global mode
    if mode == AUTO_MODE:
        mode = MANUAL_MODE 
    else:
        mode = AUTO_MODE

# Event handler for button press
GPIO.add_event_detect(Mode_Button, GPIO.FALLING, callback=toggle_mode, bouncetime=300)


try:
    while True:
        if mode == MANUAL_MODE:
            GPIO.output(Led_Pin, GPIO.HIGH) # Turn on the LED
        else:
            GPIO.output(Led_Pin, GPIO.LOW) # Turn off the LED
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() #clean up GPIO on CTRL+C exit
