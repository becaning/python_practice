#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
杨辉三角
'''
total = int(raw_input('input a number: '))

if( total > 2):
    print '1' 
l = [1]
for i in range(0,total):
    num = len(l)
    temp=[]
    for j in range(1,num):
        temp.append(l[j-1] + l[j]) 

    temp.append(1)
    temp.insert(0,1)
    l = temp
    temp = map(str, temp)
    s = ' '.join(temp)
    lon = len(s)/2
#    for j in range(total - lon):
#        print '  ',
    print s 
