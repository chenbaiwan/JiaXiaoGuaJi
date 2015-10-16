#!/usr/bin/python
#coding=utf-8

import time
import requests

s = requests.session()
id_number = ''
password = ''

def restart():
    count = 0
    logout = s.post("http://www.jppt.com.cn/gzpt/train/logOut")
    print logout.text
    
    login = s.post("http://www.jppt.com.cn/gzpt/index/login", {'loginType':'1', 'sfzmhm':id_number, 'password':password})
    print login.text
    
    startTrain = s.post('http://www.jppt.com.cn/gzpt/train/startTrain')
    print startTrain.text
    print u'开始挂机'
    
    while True:
        time.sleep(60)
        guaji()
        #每小时重新登录一次
        count = count + 1
        if count >= 60:
            break;

def guaji():
    calculateOnLoad = s.post('http://www.jppt.com.cn/gzpt/train/calculateOnLoad')
    print calculateOnLoad.text

    autoSave = s.post('http://www.jppt.com.cn/gzpt/train/autoSave')
    print autoSave.text
    print u'存个档压压惊'

def main():
    while True:
        restart()

if __name__ == '__main__':
        file_object = open('account.txt')
        content = file_object.readlines()
        id_number = content[0].strip('\n')
        password = content[1]
        main()
