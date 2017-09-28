#!/usr/bin/env python

"""
    ledRGB.py

	경 로 : model/sensor/ledRGB.py
    목 적 : 3색 LED 테스트 코드
    설 명 :
    주 의 :
    단 계 :
    이 슈 :
    일 자 : 2017.09.25
    작 성 : SuperMoon
"""

# 0. 내장 모듈 처리
import RPi.GPIO as GPIO		# gpio
import time					# time
import os, sys  			# system

# 1. 경로 처리
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path + "/../../model")
sys.path.append(path + "/../../util")

# 2. LC 제작 모듈 import
import util					# 기능 속성
import Define				# 정의 속성

# 3. 변수 설정
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]

"""
    * [Function : setupLedRGB]
    *   
    * @DESC   : 3색 LED 구성하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def setupLedRGB(data):
	global pins													# 핀 배열
	global p_R, p_G, p_B										# 핀 객체

	pins = {
		'pin_R': Define.getGpioPin()[data['gpio'][0]['pin']],	# 전역 변수 가져오기
		'pin_G': Define.getGpioPin()[data['gpio'][1]['pin']],	# 전역 변수 가져오기
		'pin_B': Define.getGpioPin()[data['gpio'][2]['pin']]	# 전역 변수 가져오기
	}

	GPIO.setmode(GPIO.BOARD)       			# Numbers GPIOs by physical location
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   	# Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) 	# Set pins to high(+3.3V) to off led

	p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 1999)
	p_B = GPIO.PWM(pins['pin_B'], 5000)

	p_R.start(100)      # Initial duty Cycle = 0 (leds off)
	p_G.start(100)
	p_B.start(100)

"""
    * [Function : loopLedRGB]
    *   
    * @DESC   : 3색 LED 동작하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def loopLedRGB(Serial):

	# 1. 성공 메세지 리턴
	Serial.SendCmd(str({'param': -1}))

	# 2. 센서 프로세스 진행
	while True:
		for col in colors:
			time.sleep(1)
			setLedRGBColor(col)

		# TODO temp
		print(Serial.lock)

		# GPIO.cleanup()

"""
    * [Function : playLedRGB]
    *   
    * @DESC   : 3색 LED 실행하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def playLedRGB (Serial, data):
	print('playLedRGB')

	try :

		setupLedRGB(data)  			# 3색 LED 설정
		loopLedRGB(Serial)  		# 3색 LED 반복 진행

	except KeyboardInterrupt:

		destroyLedRGB()				# 3색 LED 파괴

"""
    * [Function : setLedColor]
    *   
    * @DESC   : 3색 LED 색상 설정하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def setLedRGBColor(col):   # For example : col = 0x112233
	R_val = (col & 0xff0000) >> 16
	G_val = (col & 0x00ff00) >> 8
	B_val = (col & 0x0000ff) >> 0

	R_val = mapLedRGB(R_val, 0, 255, 0, 100)
	G_val = mapLedRGB(G_val, 0, 255, 0, 100)
	B_val = mapLedRGB(B_val, 0, 255, 0, 100)

	p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(100-G_val)
	p_B.ChangeDutyCycle(100-B_val)

"""
    * [Function : setLedColor]
    *   
    * @DESC   : 3색 LED 색상 설정하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def mapLedRGB(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

"""
    * [Function : destroyLedRGB]
    *   
    * @DESC   : 3색 LED 실행하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def destroyLedRGB():
	p_R.stop()
	p_G.stop()
	p_B.stop()
	offLedRGB()
	GPIO.cleanup()

"""
    * [Function : offLedRGB]
    *   
    * @DESC   : 3색 LED 동작 종료 하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def offLedRGB ():
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds