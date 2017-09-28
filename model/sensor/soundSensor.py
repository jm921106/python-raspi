#!/usr/bin/env python

"""
    soundSensor.py

	경 로 : model/sensor/soundSensor.py
    목 적 : 소리 인식 센서 코드
    설 명 :
    주 의 :
    단 계 :
    이 슈 :
    일 자 : 2017.09.26
    작 성 : SuperMoon
"""

# 0. 내장 모듈 처리
import os, sys  			# system
import RPi.GPIO as GPIO		#
import time					#

# 1. 경로 처리
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path + "/../../model")
sys.path.append(path + "/../../util")

# 2. LC 제작 모듈
import PCF8591 as ADC		# 아날로그 센서
import util					# 기능 속성
import Define				# 정의 속성

GPIO.setmode(GPIO.BCM)

"""
    * [Function : setupSoundSensor]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def setupSoundSensor():
	ADC.setup(0x48)

"""
    * [Function : loopSoundSensor]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def loopSoundSensor(Serial, data):

	# 1. 성공 메세지 리턴
	Serial.SendCmd(str({'param': -1}))

	# 2. 변수 속성
	analog		= data['analog'][0]['index']

	# 3. 센서 프로세스 진행
	while True:
		time.sleep(1)

		# TODO temp
		print ('Value:', ADC.read(analog))

		value = ADC.read(analog)
		if value:
			if value < 50 :
				print ("Voice detected!")

"""
    * [Function : playSoundSensor]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def playSoundSensor(Serial, data):
	try:

		setupSoundSensor()
		loopSoundSensor(Serial, data)

	except KeyboardInterrupt:

		pass	
