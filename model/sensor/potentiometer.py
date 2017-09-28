#!/usr/bin/env python

"""
    potentionmeter.py

	경 로 : model/sensor/potentionmeter.py
    목 적 : 가변 저항 센서 코드
    설 명 :
    주 의 :
    단 계 :
    이 슈 :
    일 자 : 2017.09.25
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
import PCF8591 as ADC		#
import util					# 기능 속성
import Define				# 정의 속성

GPIO.setmode(GPIO.BCM)

"""
    * [Function : setPotentiometer]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def setPotentiometer ():
	ADC.setup(0x48)

"""
    * [Function : loopPotentiometer]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def loopPotentiometer (Serial, data):

	# 1. 성공 메세지 리턴
	Serial.SendCmd(str({'param': -1}))

	# 2. 변수 속성
	preValue 	= 0
	analog		= data['analog'][0]['index']

	# 3. 센서 프로세스 진행
	while True :
		time.sleep(1)

		# TODO temp
		print ('Value:', ADC.read(analog))

		value = ADC.read(analog)				# 측정 값
		gap = preValue - value					# 변한 값이 +- 5 이상 충분히 변동이 있어야 한다.
		print(abs(gap))
		if (abs(gap) > 5) :						# 값이 변함 감지 !
			preValue = value					# preVale에 변동된 값 입력
			Serial.SendCmd(str({'param': -1}))	# 변동 사항 전달

"""
    * [Function : playPotentiometer]
    *   
    * @DESC   : 
    * @INPUT  : 
    * @OUTPUT : 
"""
def playPotentiometer (Serial, data):
	try:

		setPotentiometer()				# setup
		loopPotentiometer(Serial, data)	# loop

	except KeyboardInterrupt:
		pass
