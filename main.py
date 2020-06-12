#!/usr/bin/env pybricks-micropython
import time
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
obstacle_sensor = InfraredSensor(Port.S4)
strike_motor = Motor(Port.D, Direction.CLOCKWISE)
move_motor = Motor(Port.C, Direction.CLOCKWISE)
turning_motor = Motor(Port.B, Direction.CLOCKWISE)

while(True):
    print(obstacle_sensor.distance())
    while(obstacle_sensor.distance() > 15):
        move_motor.run(360)
    move_motor.run_time(-360, 1400)
    for i in range(3):
        turning_motor.run_time(400, 500)
        turning_motor.run_time(-400, 500)
            # motor_c.run_time(220, 1100)  
    strike_motor.run_time(220, 1100)  
    brick.sound.file("snakehiss2.wav")
    strike_motor.run_time(-220, 1100)
            # motor_c.run_time(-220, 1100)
            # brick.sound.file("snakehiss2.wav")
    move_motor.run_time(-360, 4000)
    turning_motor.run_time(360, 2000)
    move_motor.run_time(360, 4000)
    turning_motor.run_time(-360, 2000)