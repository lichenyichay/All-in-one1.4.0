# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/9/24 8:36
# @FILE:Allinone.py
# @version:1.4.2
# @Software: IntelliJ IDEA
import os,math,time,random

from src.module.book import *
from src.module.calculator import *
from src.module.erfenchazhao_py import *
from src.module.math_cal_py import *
from src.module.student_py import *
from src.module.tuxing_cal import *
from src.module.xiaogongju import *

global zongzifu


def allinone(fuwu):
    """
    :param 需要服务的功能
    :return: 0：正常，1：不正常
    功能：大小写互换、抽取随机数、求最小公倍数、图形计算器、小学学生信息管理系统、二分查找
    """
    global zongzifu
    try:
        i = -1
        while True:
            i = i + 1
            # a = input("请输入你要什么服务：（输入quit或exit退出）")
            if fuwu == "大小写互换":
                gongneng1 = input("请输入服务：（可选项：大写转小写，小写转大写）")
                if gongneng1 == "大写转小写":
                    zifugeshu = int(input("请输入字符个数"))
                    if zifugeshu > 1:
                        for i in range(zifugeshu):
                            zifu = input("请输入第" + str(i + 1) + "个字符")
                            # zifu1 = ord(zifu)
                            zifu1 = ord(zifu) + 32
                            zifu1 = chr(zifu1)
                            zongzifu = [zifu1]
                        print("转换结果：", end='')
                        for j in zongzifu:
                            print(j)
                    else:
                        zifu = input("请输入字符：")
                        zifu1 = ord(zifu)
                        zifu1 = zifu1 + 32
                        zifu1 = chr(zifu1)
                        print("转换结果：" + zifu1)
                elif gongneng1 == "小写转大写":
                    zifugeshu = int(input("请输入字符个数"))
                    if zifugeshu > 1:
                        for i in range(zifugeshu):
                            zifu = input("请输入第" + str(i + 1) + "个字符")
                            zifu1 = ord(zifu)
                            zifu1 = zifu1 - 32
                            zifu1 = chr(zifu1)
                            zongzifu = [zifu1]
                        print("转换结果：")
                        for j in zongzifu:
                            print(j)
                    else:
                        zifu = input("请输入字符：")
                        zifu1 = ord(zifu)
                        zifu1 = zifu1 - 32
                        zifu1 = chr(zifu1)
                        print("转换结果：" + zifu1)
                    print("--------------------")
            elif fuwu == "抽取随机数":
                c = int(input("请输入最小值："))
                d = int(input("请输入最大值："))
                while True:
                    try:
                        e = input("请输入模式（二进制：bin;八进制：oct,十进制：int，十六进制：hex）：")
                        return randomint(d,c,e)
                    except Exception as e:
                        return repr(e)
            elif fuwu == "求最小公倍数":
                num1 = int(input("请输入数字："))
                num2 = int(input("请输入数字："))
                for i1 in range(max(num1, num2), num1 * num2 + 1):
                    if i1 % num1 == 0 and i1 % num2 == 0:
                        return f"最小公倍数是：{i1}"
                        break
                print("--------------------")
            elif fuwu == "求最大公因数":
                num1 = int(input("请输入数字："))
                num2 = int(input("请输入数字："))
                return twonumbers_TheBiggestCommonfactor(num1,num2)
            # elif fuwu == "快速排列":
            #     kuaisupailie()
            elif fuwu == "图形计算器":
                while True:
                    huida = input("请输入你要计算的对象：")
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
                print("--------------------")
            elif fuwu == "小学学生信息管理系统":
                student()
            elif fuwu == "二分查找":
                while True:
                    d = input("请输入是否运行（运行输yes，否则输no）：")
                    if d == "yes":
                        a = []
                        while True:
                            i2 = input("请输入列表中的数据（-1代表结束）：")
                            if i2 == "-1":
                                break
                            else:
                                a.append(i2)
                        b = sorted(a)
                        c = input("请输入查找值：")
                        diaoyong = binarysearch(a, b, c)
                        print(diaoyong)
                        sleep(5)
                        print("--------------------")
                    elif d == "no":
                        print("程序结束运行！")
                        break
                    else:
                        print("指令无效！")
            elif fuwu == "quit" or "exit":
                print("感谢您的使用，再见！")
                break
            else:
                jieshulist = ["功能无效！", "无法实现服务！", "暂时还在开发！"]
                b = random.choice(jieshulist)
                print(b)
                break
        return 0
    except KeyboardInterrupt:
        print("\n感谢您的使用，再见！")
        return 1


# print(__doc__)
if __name__ == "__main__":
    import Allinone
    print(help(Allinone))
