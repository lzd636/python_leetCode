# -*-coding:utf8 -*-

'''
时间复杂度：
找出数组中相加和为target的两个元素位置
input: number = [2,5,7,15],target = 9
output: index1 = 1 ,index2 = 2
'''

import time

number = [2,5,7,4,15]
target = int(raw_input("请输入目标和值："))
print type(target)
a = [[x,y] for x in number for y in number if x!=y and x + y == target ]
print type(a)
print a
for i in a:
    a = i[0] + i[1]
    if a == target:
        print i[0],i[1]
    # print "index1 = %d ,index2 = %d ",% (i[0],i[1])

