#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
这是一个通讯录增删改查的练习
通讯录以文件形式保存，具体保存格式：
    ID  Name    Passwd      Email           Phone
eg: 1   jack    123         123@126.com     010-88888888
'''
#----------------引入tab自动补全--------------
# python startup file
import sys
import readline
import rlcompleter
import atexit
import os
# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)

del os, histfile, readline, rlcompleter
#----------------tab end--------------

import os


#用户登录
def login():
    name = raw_input('Please input your name:').strip()
    try:
        fd = file('data.txt','r')
    except:
        exit('\n\tThe contact data is not found!')
    #一个循环，每次到文件中读取一行，如果有和输入的name匹配，就进入密码验证，如果密码正确，返回字符串'good'
    while True:
        line = fd.readline()
        if(line == ''):
            break
        if(name == line.split()[1]):
            passwd  = raw_input('Please input your password:').strip()
            if( passwd == line.split()[2]):
                return 'good'
            break 
    fd.close() 

#查询子系统
def Search():
    while True:
        fd = file('data.txt','r')
        cmd = raw_input('Please input a name : ').strip()
        #判断是否回到主菜单
        if(cmd == 'HELP'):
            return

        flag = True   #设置一个标示符，默认为True，如果有匹配内容，就改为False，为后面的输出信息做准备
        while True:
            line = fd.readline()
            if(line == ''):     #如果line为空，表示文件已经读完，退出循环
                break 
            elif(cmd in line.split()):
                flag = False 
                print 'ID:',line.split()[0],'   Name:',line.split()[1],'    Email:',line.split()[3],\
                '   Phone:',line.split()[4]

        if( flag ):     #如果一直没有匹配结果，则flag为True，所以输出信息
            print "There isn't information what you want"

        fd.close()

#删除子系统
def Delate():
    while True:
        fd = file('data.txt','r')
        cmd = raw_input('Please input a name : ').strip()
        #判断是否回到主菜单
        if(cmd == 'HELP'):
            return

        flag = True   #设置一个标示符，默认为True，如果有匹配内容，就改为False，为后面的输出信息做准备
        temp = file('temp','a')
        while True:
            line = fd.readline()
            if(line == ''):     #如果line为空，表示文件已经读完，退出循环
                break 
            elif(cmd in line.split()):
                flag = False 
                print 'ID:',line.split()[0],'   Name:',line.split()[1],'    Email:',line.split()[3],\
                '   Phone:',line.split()[4]
                Yes = raw_input('Are you sure delate this item?(y/n):')

                if(Yes == 'y' or Yes == 'Y'):
                    continue
                else:
                    temp.write(line)
                    print 'Nothing to do!'
            else:
                temp.write(line) 
        temp.close()
        fd.close()
        os.remove('data.txt')
        os.rename('temp','data.txt')

        if( flag ):     #如果一直没有匹配结果，则flag为True，所以输出信息
            print "There isn't information what you want to delate"


#插入子系统
def Insert():
    while True:
        print 'Please input user informations'
        Id      = raw_input('Input id :').strip()
        if(Id == 'HELP'):
            return
        name    = raw_input('Input name :').strip()
        if(name == 'HELP'):
            return
        passwd  = raw_input('Input passwd :').strip()
        if(passwd == 'HELP'):
            return
        email   = raw_input('Input email :').strip()
        if(email == 'HELP'):
            return
        phone   = raw_input('Input phone :').strip()
        if(phone == 'HELP'):
            return

        item = [Id,name,passwd,email,phone]
        item_str = '   '.join(item)

        print 'you will insert this item:\n\n\t',item
        Yes = raw_input('\n\tAre you sure(y/n):')
        if ( Yes == 'y'):
            fd = file('data.txt','a')
            fd.write(item_str +'\n')
            fd.close()
            print 'Insert a item successful ^_^\n-----------------------------------'

#开始执行
#res = login()
#if ( res != 'good' ):
    exit('\n\tyour name or password is wrong!') 

print '''
        Welcome to the cantacts system
        There are some commands for use the system
        S   :   search
        D   :   Delate
        U   :   Update
        I   :   Insert
        HELP:   It is use to back mainmenu(It's here)
        quit:   quit the system
      '''

#进入主循环执行
while True:
    command = raw_input('Please input a command : ').strip()
    if(command == 'S'):
        #进入查询子系统
        Search() 
    elif(command == 'D'):
        #进入删除子体统
        Delate()
    elif(command == 'U'):
        #进入更新子系统
        print 'U'
    elif(command == 'I'):
        #进入插入子系统
        Insert()
    elif(command == 'quit'):
        #退出系统
        exit('Thanks for you ^_^ Bye!')
