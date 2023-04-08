# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/25 9:02
# @FILE:student_py.py
# @Software:IDLE 3.9.6
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
        ans = input("请输入功能：")
        if ans == "查询学生信息":
            try:
                a = input("请输入学员姓名：")
                return f"{a}的相关信息是：{stu[a]}"
            except:
                return "无此学生"
        elif ans == "删除学生信息":
            a = input("请输入要删除的学员姓名：")
            del stu[a]
            return f"{a}的相关信息已经删除"
        elif ans == "添加学生信息":
            a = input("请输入要添加的学员姓名：")
            b = input("请输入新增的学员信息：")
            stu[a] = b
            return (f"{a}的相关信息已添加")
        elif ans == "4":
            break
        else:
            return ("无此功能")
    return 0
