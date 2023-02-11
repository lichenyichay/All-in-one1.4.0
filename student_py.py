# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/25 9:02
# @FILE:student_py.py
# @Software:IDLE 3.9.6

from menu import *
import time
'''
函数名：student
调用形式：student()
作用：小学学生信息管理系统
'''
def student():
    print("这里是xx小学学生信息管理系统")
    stu = { "老八"  : "老八,岁数不明,男,厕所深处 爱好:在厕所干饭"}
    print("你可以查到所有学员的个人信息,但也请不要向外泄露")
    while True:
        print("以下是现有学员名单：")
        for k in stu:
            print(k)
        student_menu()
        ans = input("请输入序号：")
        if ans == "1":
            try:
                a = input("请输入学员姓名：")
                print(f"{a}的相关信息是：{stu[a]}")
                time.sleep(1)
            except:
                print("无此学生")
                time.sleep(1)
        elif ans == "2":
            a = input("请输入要删除的学员姓名：")
            del stu[a]
            print(a,"的相关信息已经删除")
            time.sleep(1)
        elif ans == "3":
            a = input("请输入要添加的学员姓名：")
            b = input("请输入新增的学员信息：")
            stu[a] = b
            print(a,"的相关信息已添加")
            time.sleep(1)
        elif ans == "4":
            break
        else:
            print("无此功能")
            time.sleep(1)