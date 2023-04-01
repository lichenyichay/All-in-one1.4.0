# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2023/3/28 20:20
# @FILE:Allinone.py
# @version:2.4.0
# @Software: IntelliJ IDEA
import os,math,time,random

from module.book import *
from module.calculator import *
from module.erfenchazhao_py import *
from module.math_cal_py import *
from module.student_py import *
from module.tuxing_cal import *
from module.xiaogongju import *

def allinone(fuwu,mode,*args):
    """
    :param 需要服务的功能
    :return: 0：正常，1：不正常，其他返回值表示功能的结果
    功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）
    """
    global zongzifu
    try:
        i = -1
        i = i + 1
        if fuwu == "大小写互换":
            gongneng1 = mode
            if gongneng1 == "1":
                for i in args:
                    zifu = i
                    zifu1 = chr(ord(zifu) + 32)
                return("转换结果：",zifu1)
            elif gongneng1 == "2":
                for i in args:
                    zifu = i
                    zifu1 = chr(ord(zifu) - 32)
                return("转换结果：",zifu1)
        elif fuwu == "抽取随机数":
            c = args[0]
            d = args[1]
            while True:
                try:
                    e = args[2]
                    return randomint(d,c,e)
                except Exception as e:
                    return repr(e)
        elif fuwu == "求最小公倍数":
            num1 = args[0]
            num2 = args[1]
            for i1 in range(max(num1, num2), num1 * num2 + 1):
                if i1 % num1 == 0 and i1 % num2 == 0:
                    return f"最小公倍数是：{i1}"
                    break
        elif fuwu == "求最大公因数":
            num1 = args[0]
            num2 = args[1]
            return twonumbers_TheBiggestCommonfactor(num1,num2)
        # elif fuwu == "快速排列":
        #     kuaisupailie()
        elif fuwu == "图形计算器":
            while True:
                huida = args[0]
                try:
                    if tuxing(huida) != 1:
                        if tuxing(huida) != 2:
                            return tuxing(huida)
                        else:
                            return "不支持此图形的计算！"
                    else:
                        return "不支持该功能！"
                except ValueError:
                    return ("输入无效！")
                    break
        elif fuwu == "小学学生信息管理系统":
            student()
        elif fuwu == "二分查找":
            while True:
                d = input("请输入是否运行（运行输yes，否则输no）：")
                if d == "yes":
                    a = args
                    b = sorted(a)
                    c = args[-1]
                    diaoyong = binarysearch(a, b, c)
                    return(diaoyong)
                    sleep(5)
                elif d == "no":
                    return 0
                    break
                else:
                    return ("指令无效！")
        elif fuwu == "求余":
            while True:
                try:     
                    w1 = args[0]
                    w2 = args[1]
                    w3 = w1 % w2
                    return w3
                    break
                except Exception as e:
                    raise Exception(repr(e))
        elif fuwu == "向下取整":
            while True:
                try:
                    w1 = args[0]
                    return int(w1)
                    break
                except Exception as e:
                    raise Exception(repr(e))
        elif fuwu == "向上取整":
            while True:
                try:
                    w1 = args[0]
                    return (int(w1)+1)
                    break
                except Exception as e:
                    raise Exception(repr(e))
        elif fuwu == "多个数求和":
            try:
                b = args
                b = tuple(b)
                b = math.fsum(b)
                return (b)
            except Exception as e:
                raise Exception(repr(e))
        elif fuwu == "多个数求差":
            try:
                b = 0
                e = args
                c = len(args)
                b = e[0]
                for i in range(c-1):
                    b -= e[1+i]
                return (b)
            except Exception as e:
                raise Exception(repr(e))
        elif fuwu == "多个数求积":
            try:
                b = 0
                e = args
                c = len(args)
                b = e[0]
                for i in range(c-1):
                    b *= e[1+i]
                return(b)
            except Exception as e:
                print(repr(e))
        elif fuwu == "判断闰年":
                while True:
                    try:
                        year = args[0]
                        if (year % 4) == 0:
                            if (year % 100) == 0:
                                if (year % 400) == 0:
                                    return("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
                                else:
                                    return("{0} 不是闰年".format(year))
                            else:
                                return("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
                        else:
                            return("{0} 不是闰年".format(year))
                        break
                    except Exception as e:
                        raise Exception(repr(e))
        elif fuwu == "判断是否为质数":
            while True:
                try:
                    # 用户输入数字
                    num = args[0]
                    # 质数大于 1
                    if num > 1:
                        # 查看因子
                        for i in range(2,num):
                            if (num % i) == 0:
                                return(num,"不是质数")
                                break
                        else:
                            return(num,"是质数")
                               
                    # 如果输入的数字小于或等于 1，不是质数
                    else:
                        return(num,"不是质数")
                    break
                except Exception as e:
                    print(repr(e))
        elif fuwu == "整数、小数计算-乘":
            if mode == "0":
                eee = args[0]
                aaa = args[1]
                qqq = eee * aaa
                return("等于",qqq)
            else:
                eee = args[0]
                aaa = args[1]
                qqq = eee / aaa
                return("等于",qqq)
        elif fuwu == "分数计算-加":
            try:
                qw = args[0]
                sd =args[1]
                ad = args[2]
                df = args[3]
                sva = (sd/qw)+(df/ad)
                return("等于",sva)
            except Exception as e:
                raise Exception(e)
        elif fuwu == "分数计算-减":
            try:
                qw = args[0]
                sd =args[1]
                ad = args[2]
                df = args[3]
                sva = (sd/qw)-(df/ad)
                return("等于",sva)
            except Exception as e:
                raise Exception(e)
        elif fuwu == "分数计算-乘":
            try:
                qw = args[0]
                sd =args[1]
                ad = args[2]
                df = args[3]
                sva = (sd/qw)*(df/ad)
                return("等于",sva)
            except Exception as e:
                raise Exception(e)
        elif fuwu == "分数计算-除":
            try:
                qw = args[0]
                sd =args[1]
                ad = args[2]
                df = args[3]
                sva = (sd/qw)/(df/ad)
                return("等于",sva)
            except Exception as e:
                raise Exception(e)
        elif fuwu == "比大小":
            pass
        elif fuwu == "年龄计算":
            pass
        elif fuwu == "开平方":
            pass
        elif fuwu == "华氏度摄氏度转换":
            pass
        elif fuwu == "混合运算-（+-）":
            pass
        elif fuwu == "混合运算-（+*）":
            pass
        elif fuwu == "混合运算-（+/）":
            pass
        elif fuwu == "混合运算-（-+）":
            pass
        elif fuwu == "混合运算-（-*）":
            pass
        elif fuwu == "混合运算-（-/）":
            pass
        elif fuwu == "混合运算-（*+）":
            pass
        elif fuwu == "混合运算-（*-）":
            pass
        elif fuwu == "混合运算-（*/）":
            pass
        elif fuwu == "混合运算-（/+）":
            pass
        elif fuwu == "混合运算-（/-）":
            pass
        elif fuwu == "混合运算-（/*）":
            pass
        elif fuwu == "混合运算-（//）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->USD（美元）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->JPY（日元）":
            pass
        elif fuwu == "货币转换-USD（美元）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-USD（美元）->JPY（日元）":
            pass
        elif fuwu == "货币转换-JPY（日元）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-JPY（日元）->USD（美元）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->MOP（澳门元）":
            pass
        elif fuwu == "货币转换-MOP（澳门元）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->HKD（港元）":
            pass
        elif fuwu == "货币转换-HKD（港元）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->TWD（台币）":
            pass
        elif fuwu == "货币转换-TWD（台币）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->GBP（英镑）":
            pass
        elif fuwu == "货币转换-GBP（英镑）->CNY（人民币）":
            pass
        elif fuwu == "货币转换-CNY（人民币）->EUR（欧元）":
            pass
        elif fuwu == "货币转换-EUR（欧元）->CNY（人民币）":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "":
            pass
        elif fuwu == "quit" or fuwu == "exit":
            return 0
        else:
            jieshulist = ["功能无效！", "无法实现服务！", "暂时还在开发！"]
            b = random.choice(jieshulist)
            return b
        return 0
    except KeyboardInterrupt:
        return 0


# print(__doc__)

import Allinone
##print(help(Allinone))
print(allinone("大小写互换","2",("a")))
