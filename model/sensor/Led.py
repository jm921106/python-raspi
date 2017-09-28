"""
    Led.py

    목 적 : Led 클래스
    설 명 :
    단 계 :
    문 제 :
    일 자 : 2017.07.26
    작 성 : SuperMoon
    참 조 :
"""

# embedded
import RPi.GPIO as gpio  # gpio
import os, sys, time     # embedded

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path + "/../")

from GPIO import GPIO

class Led (GPIO) :

    def __init__(self, packet) :
        GPIO.__init__(self, packet)

    def on (self):
        # test
        print ('on')
        gpio.output(self.arrPin[0], True)

    def off (self):
        # test
        print ('off')
        gpio.output(self.arrPin[0], False)