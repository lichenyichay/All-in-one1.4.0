# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/25 9:03
# @FILE:erfenchazhao_py.py
# @Software:IDLE 3.9.6

import time

'''
函数名：erfenchazhao
调用形式：a = erfenchazhao(yuanlst,shengxulst,target)
:param yuanlst 原序列
:param shengxulst 升序列表（原序列改编）
:param target 查找值
:return 查找结果（索引，用时，次数）
作用：查找列表中的值
'''
def erfenchazhao(yuanlst,shengxulst,target):
    start_time = time.time()
    start = 0
    count = 0
    end = len(shengxulst)-1
    if target not in shengxulst:
        end_time = time.time()
        return "列表中未查找到目标值"+str(target)+"，共用时"+str(end_time-start_time)+"s，查找次数：0，索引：无"
    while True:
        count += 1
        mid = (start+end)//2
        if target < shengxulst[mid]:
            end = mid-1
            continue
        elif target > shengxulst[mid]:
            start = mid + 1
            continue
        else:
            end_time = time.time()
            return "列表中已查找到目标值"+str(target)+"，共用时"+str(end_time-start_time)+"s，查找次数："+ str(count) +"，原列表中索引："+str(yuanlst.index(target))