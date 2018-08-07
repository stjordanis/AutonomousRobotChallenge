# import curses and GPIO
from gpioServo import MotorControls
motor = MotorControls()

with open("key_strokes.txt",'r') as keys:
    key_strokes = keys.readlines()

key_strokes = [x.strip() for x in key_strokes]
for x in key_strokes:
    if x == '1,0,0,0':
        motor.forward()
    elif x == '0,1,0,0':
        motor.stop()
    elif x == '0,0,1,0':
        motor.turn1()
    elif x == '0,0,0,1':
        motor.turn2()

