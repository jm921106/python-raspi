#!/usr/bin/env python

"""
    Queue.py

    경 로 : model/Queue.py
    목 적 :
    설 명 :
    주 의 :
    단 계 :
    이 슈 :
    일 자 : 2017.09.26
    작 성 : SuperMoon
"""

class Queue :

    def __init__(self):
        self.arrQueue   = []        # 큐 배열
        self.lock       = False     # 큐 사용 여부