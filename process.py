#!/usr/bin/env python

"""
    process.py

    목 적 : Serial Process [수정없음]
    설 명 : Serial 통신은 받는 스크립트 (변동 없이 무한 반복)
    주 의 : 수정 불가 !
    단 계 :
    이 슈 :
        추가적인 소스코드 수정이 들어가선 안됨
        버그 없이 최소화된 소스코드로 배포
        외부 모듈 사용을 최소화
    일 자 : 2017.07.26
    작 성 : SuperMoon
"""

print ('Raspberry PI Serial Process ON :)')

# 1. 내장 모듈 호출
import os, sys          # 1.1 system
import ast              # 1.2 str > dict
import threading        # 1.3 threading
import RPi.GPIO as GPIO	# 1.4 GPIO

# 2. 절대 경로 삽입
path = os.path.abspath(os.path.dirname(__file__))   #
sys.path.append(path + "/util")                     #
sys.path.append(path + "/model")                    #
sys.path.append(path + "/model/sensor")             #

# 3. LC 제작 모듈 호출
from RS232 import RS232 # 3.1 시리얼 통신 모듈
import util             # 3.2 유틸 모듈

# 4. 센서 모듈 호출
import ledRGB           # 4.1 3색 LED
import potentiometer    # 4.2 가변 저항
import soundSensor      # 4.3 소리 센서
import photoResistor    # 4.4 조도 센서

# 5. 변수 정의
processStatus = True    # 5.1
Serial = RS232(115200)  # 5.2 시리얼 객체 생성

"""
    * [Function : showProcessList]
    *   
    * @DESC   : 프로세스 목록 보기
    * @INPUT  : 
    * @OUTPUT : 
"""
def showProcessList() :

    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    print ('==================프로세스 목록====================')

    for pid in pids:
        try:
            print (open(os.path.join('/proc', pid, 'cmdline'), 'rb').read())
        except IOError:  # proc has already terminated
            continue

    print ('==================프로세스 목록====================')

"""
    * [Function : getThreadCount]
    *   
    * @DESC   : Thread 갯수 확인하기
    * @INPUT  : 
    * @OUTPUT : 
"""
def getThreadCount () :
    return threading.active_count()

"""
    * [Function : closeAllThread]
    *   
    * @DESC   : 모든 Thread 종료 시키기
    * @INPUT  : 
    * @OUTPUT : 
"""
def closeAllThread() :

    pass


"""
    * [Listener : Serial Listener]
    *   
    * @DESC   : 시리얼 통신 수신 리스너
    * @INPUT  : 
    * @OUTPUT : 
"""
while processStatus:
    try :
        data = Serial.Receive()  # 시리얼 수신 데이터

        if data != None:

            # [TODO] Data type except process
            strPacket = data.decode("utf-8")  # serial 전송 데이터 디코드
            dictPacket = ast.literal_eval(strPacket)  # serial 문자 데이터 > 가공 데이터

            # TODO temp
            print (getThreadCount())

            # 1. 연결 체크 [check]
            if dictPacket['url'] == 'check':
                print ('url [check]')
                Serial.SendCmd(str({'param': -1}))

                # TODO temp
                if(Serial.lock == True) :
                    Serial.lock = False
                else :
                    Serial.lock = True

                print(Serial.lock)

            # 2. 시스템 명령 접근 [cmd]
            elif dictPacket['url'] == 'cmd':
                print ('url [cmd]')
                os.system(dictPacket['cmd'])

            # 3. 2색 LED [ledDual]
            elif dictPacket['url'] == 'ledDual':
                print ('url [ledDual]')
                pass

            # 4. 3색 LED [ledRGB]
            elif dictPacket['url'] == 'ledRGB':
                print ('url [ledRGB]')

                # Thread 존재한다면 종료 후 다시 실행
                # if 'ledRGB' in queue.arrQueue.keys():
                #     pass
                #
                #     # TODO Thread 종료 메소드
                #     # dictThread['ledRGB'] .terminate() or .stop()

                newProcess = threading.Thread(target=ledRGB.playLedRGB,
                                              args=(Serial, dictPacket['args']))
                newProcess.setName('ledRGB')        # Thread 이름 설정      (종료시 접근하기 위해)
                # dictThread['ledRGB'] = newProcess   # Thread 리스트에 추가   (종료시 접근하기 위해)
                newProcess.start()

            # TODO 5. 가변 저항 [potentiometer]
            elif dictPacket['url'] == 'potentiometer':
                print ('url [potentiometer]')

                # Thread 존재한다면 종료 후 다시 실행
                # if 'potentiometer' in dictThread.keys():
                #     pass
                #
                #     # TODO Thread 종료 메소드
                #     # dictThread['ledRGB'] .terminate() or .stop()

                newProcess = threading.Thread(target=potentiometer.playPotentiometer,
                                              args=(Serial, dictPacket['args']))
                newProcess.setName('potentiometer')        # Thread 이름 설정      (종료시 접근하기 위해)
                # dictThread['potentiometer'] = newProcess   # Thread 리스트에 추가   (종료시 접근하기 위해)
                newProcess.start()

            # TODO 6. 소리 센서 [soundSensor]
            elif dictPacket['url'] == 'soundSensor':
                print ('url [soundSensor]')

                # Thread 존재한다면 종료 후 다시 실행
                # if 'soundSensor' in dictThread.keys():
                #     pass
                #
                #     # TODO Thread 종료 메소드
                #     # dictThread['ledRGB'] .terminate() or .stop()

                newProcess = threading.Thread(target=soundSensor.playSoundSensor,
                                              args=(Serial, dictPacket['args']))
                newProcess.setName('soundSensor')           # Thread 이름 설정      (종료시 접근하기 위해)
                # dictThread['soundSensor'] = newProcess    # Thread 리스트에 추가   (종료시 접근하기 위해)
                newProcess.start()

            # TODO 7. 조도 센서 [photoResistor]
            elif dictPacket['url'] == 'photoResistor':
                print ('url [photoResistor]')

                # Thread 존재한다면 종료 후 다시 실행
                # if 'soundSensor' in dictThread.keys():
                #     pass
                #
                #     # TODO Thread 종료 메소드
                #     # dictThread['ledRGB'] .terminate() or .stop()

                newProcess = threading.Thread(target=photoResistor.playPhotoResistor,
                                              args=(Serial, dictPacket['args']))
                newProcess.setName('photoResistor')       # Thread 이름 설정      (종료시 접근하기 위해)
                # dictThread['photoResistor'] = newProcess  # Thread 리스트에 추가   (종료시 접근하기 위해)
                newProcess.start()

            # TODO 8. Error 처리 (404)
            else:
                pass
    except e:
        print(e)