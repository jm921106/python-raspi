
"""
    util.py

    목 적 : Project에 필요한 기능단위의 함수를 모아 놓은 스크립트
    설 명 : Python 프로젝트에서 필요한 기능단위의 함수들을 정리해 놓은 스크립트 (자료형 및 수식 관련)
    단 계 : 진행중
    문 제 :
    일 자 : 2017.07.26
    작 성 : SuperMoon
"""


# byte to str converter
def bytesToStr (arrByte) :
    result = ""
    for i in arrByte:
        result += str(i) + "_"
    return result[:len(result)-1]

# string to byte converter
def strToBytes (str) :
    result = bytearray()
    arrStr = str.split('_')
    for i in arrStr:
        result.append(int(i))
    return result

# electron packet str convert
def convertStr(str) :
    rtn = str.replace('"', "%q%")
    rtn = rtn.replace(' ', "%s%")
    return rtn

# electron packet str rollback
def rollbackStr(str) :
    rtn = str.replace("%q%", '"')
    rtn = rtn.replace("%s%", ' ')
    return rtn

