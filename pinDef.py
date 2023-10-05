# This file defines pins on raspberry pi and their usages

import RPi.GPIO as GPIO
# Inputs
Mode_Button = 17 # GPIO pin that swaps from manual to auto mode
Kick_Button = 27 # GPIO pin that triggers the kick
KP_Button = 23 # GPIO pin that sets the kick power low, medium, or high (counts presses)
Aim_Pot = 22 # GPIO pin that reads the potentiometer for aim

# Peripherals
Led_Pin = 18 # GPIO pin that controls the LED

# Servos

aim_Servo = 12 # GPIO pin that controls the aim servo
kick_Servo = 13 # GPIO pin that controls the kick servo

# GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(Mode_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Kick_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KP_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Aim_Pot, GPIO.IN)