from time import *
from threading import Thread


def kuaisupailie():
    """
    :return: 0:正常，1：不正常
    """
    try:
        input_ = []
        answer = []
        jobs = []

        def fast_arrangement(num: int):
            """
            :type num:int
            """
            sleep(num / 10000)
            answer.append(num)

        times = int(input("你要输入几个数："))
        for i in range(times):
            num = int(input("请输入数字:"))
            input_.append(num)

        for i in range(len(input_)):
            t = Thread(target=fast_arrangement, args=(input_[i],))
            jobs.append(t)
            t.start()

        for job in jobs:
            job.join()

        print(answer)
        return 0
    except Exception as e:
        print("错误信息：" + repr(e))
        return 1
    print("--------------------")


__doc__ = """
:param 无
:return 0:正常，1:不正常
"""
print(__doc__)
