import time


def student():
    """
    :param 无
    :return: 0:正常,1:不正常
    """
    try:
        print("这里是xx小学学生信息管理系统")
        stu = {"老八": "老八,岁数不明,男,厕所深处 爱好:在厕所干饭"}
        print("你可以查到所有学员的个人信息,但也请不要向外泄露")
        while True:
            print("以下是现有学员名单：")
            for k in stu:
                print(k)
            ans = input("查询学员信息请按1,删除学员信息请按2,新增学员信息请按3,退出请按0：")
            if ans == "1":
                try:
                    a = input("请输入学员姓名：")
                    print(f"{a}的相关信息是：{stu[a]}")
                    time.sleep(5)
                    print("--------------------")
                except KeyError:
                    print("无此学生")
                    time.sleep(5)
                    print("--------------------")
            elif ans == "2":
                a = input("请输入要删除的学员姓名：")
                del stu[a]
                print(a, "的相关信息已经删除")
                time.sleep(5)
                print("--------------------")
            elif ans == "3":
                a = input("请输入要添加的学员姓名：")
                b = input("请输入新增的学员信息：")
                stu[a] = b
                print(a, "的相关信息已添加")
                time.sleep(5)
                print("--------------------")
            elif ans == "0":
                print("感谢你的使用！再见")
                break
            else:
                print("无此功能")
                time.sleep(5)
        print("--------------------")
        return 0
    except Exception:
        return 1
