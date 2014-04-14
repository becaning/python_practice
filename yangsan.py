#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
杨辉三角
'''
total = int(raw_input('input a number: '))

l = [1,[1,1]]
for i in range(1,total):
    num = len(l[i])
    temp=[]
    for j in range(1,num):
        temp.append(l[i][j-1] + l[i][j]) 

    temp.append(1)
    temp.reverse()
    temp.append(1)
    l.append(temp)

for i in range(total):
    print l[i]
