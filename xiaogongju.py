# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:07
# @FILE:xiaogongju.py
# @Software:IDLE 3.9.6
import random

'''
函数名：randomint
调用形式：a = randomint(maxint,minint,mode)
:param maxint 随机数最大值
:param minint 随机数最小值
:param mode 模式 bin（二进制）/oct（八进制）/int（十进制）/hex（十六进制） 不在选择范围内则抛出异常
:return 随机数
作用：取不同进制的随机数
'''
def randomint(maxint,minint,mode):
    b = random.randint(minint,maxint)
    if mode == "bin":
        return bin(b)
    elif mode == "oct":
        return oct(b)
    elif mode == "int":
        return b
    elif mode == "hex":
        return hex(b)
    else:
        raise TypeError("TypeError:模式错误！")

'''
函数名：daorxiao
调用形式：daorxiao(mode)
:param mode 模式 datoxiao（大写转小写）/xiaotoda（小写转大写） 不在选择范围内则抛出异常
:return 0
作用：大小写转换
'''
def daorxiao(mode):
    zifugeshu = int(input("请输入字符个数"))
    if mode == "datoxiao":
        if zifugeshu > 1:
            for i in range(zifugeshu):
                zifu = input("请输入第" + str(i + 1) + "个字符")
                # zifu1 = ord(zifu)
                zifu1 = ord(zifu) + 32
                zifu1 = chr(zifu1)
                zongzifu = []
                zongzifu.append(zifu1)
            print("转换结果：",end = '')
            for j in zongzifu:
                print(j)
        else:
            zifu = input("请输入字符：")
            zifu1 = ord(zifu)
            zifu1 = zifu1 + 32
            zifu1 = chr(zifu1)
            print("转换结果：" + zifu1)
        return 0
    elif mode == "xiaotoda":
        if zifugeshu > 1:
            for i in range(zifugeshu):
                zifu = input("请输入第" + str(i + 1) + "个字符")
                # zifu1 = ord(zifu)
                zifu1 = ord(zifu) - 32
                zifu1 = chr(zifu1)
                zongzifu = []
                zongzifu.append(zifu1)
            print("转换结果：",end = '')
            for j in zongzifu:
                print(j)
        else:
            zifu = input("请输入字符：")
            zifu1 = ord(zifu)
            zifu1 = zifu1 - 32
            zifu1 = chr(zifu1)
            print("转换结果：" + zifu1)
        return 0
    else:
        raise Exception("Error:模式错误!")

'''
函数名：twonumbers_TheBiggestCommonfactor
调用形式：a = twonumbers_TheBiggestCommonfactor(num1,num2)
:param num1 第一个数
:param num2 第二个数
:return num1和num2的最大公因数
作用：求最大公因数
'''
def twonumbers_TheBiggestCommonfactor(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return max(lst)

'''
函数名：twonumbers_TheMinimumCommonmultiple
调用形式：a = twonumbers_TheMinimumCommonmultiple(num1,num2)
:param num1 第一个数
:param num2 第二个数
:return num1和num2的最小公倍数
作用：求最小公倍数
'''
def twonumbers_TheMinimumCommonmultiple(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return num1 * num2 // max(lst)
