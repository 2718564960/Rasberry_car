# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class BasicMove():
    PWMA = 18
    AIN1 = 22
    AIN2 = 27
    PWMB = 23
    BIN1 = 25
    BIN2 = 24
    GPIO.setwarnings(False)

    def start(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.AIN2, GPIO.OUT)
        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.BIN1, GPIO.OUT)
        GPIO.setup(self.BIN2, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        self.L_Motor = GPIO.PWM(self.PWMA, 100)
        self.R_Motor = GPIO.PWM(self.PWMB, 100)
        self.R_Motor.start(0)
        self.L_Motor.start(0)

    def t_up(self, speed):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.AIN2, False)  # AIN2
        GPIO.output(BasicMove.AIN1, True)  # AIN1
        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.BIN2, False)  # BIN2
        GPIO.output(BasicMove.BIN1, True)  # BIN1


    def t_stop(self):
        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(BasicMove.AIN2, False)  # AIN2
        GPIO.output(BasicMove.AIN1, False)  # AIN1
        self.R_Motor.ChangeDutyCycle(0)
        GPIO.output(BasicMove.BIN2, False)  # BIN2
        GPIO.output(BasicMove.BIN1, False)  # BIN1

    def t_down(self, speed):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.AIN2, True)  # AIN2
        GPIO.output(BasicMove.AIN1, False)  # AIN1
        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.BIN2, True)  # BIN2
        GPIO.output(BasicMove.BIN1, False)  # BIN1

    def t_left(self, speed):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.AIN2, True)  # AIN2
        GPIO.output(BasicMove.AIN1, False)  # AIN1
        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.BIN2, False)  # BIN2
        GPIO.output(BasicMove.BIN1, True)  # BIN1

    def t_right(self, speed):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.AIN2, False)  # AIN2
        GPIO.output(BasicMove.AIN1, True)  # AIN1
        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BasicMove.BIN2, True)  # BIN2
        GPIO.output(BasicMove.BIN1, False)  # BIN1
        
    def exit():
        GPIO.cleanup()

