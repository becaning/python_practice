#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
杨辉三角
'''
total = int(raw_input('input a number: ')) - 1

if( total > 0):
    print '1' 
    print '1 1'
else:
    exit('请输入大于1的整数')
l = [1,1]
for i in range(1,total):
    num = len(l)
    temp=[]
    for j in range(1,num):
        temp.append(l[j-1] + l[j]) 

    temp.append(1)
    temp.insert(0,1)
    l = temp
    temp = map(str, temp)
    s = ' '.join(temp)
    print s 
