# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:38
# @FILE:math_cal_py.py
# @Software:IDLE 3.9.6
import math
'''
函数名：math_cal
调用形式：s = math_cal(mode,float1,float2)
:param mode 模式 1~19 模式不在此选择范围内会抛出异常
:param float1 float2 float型参数，根据模式的需求，如参数有空余，则空余参数添0即可，例：mode = 3:math_cal(3,5.2,0);
例2：mode = 4:math_cal(4,0,0);例3：mode = 1:math_cal(1,5.92,-8)
:return 结果
'''
def math_cal(mode,float1,float2):
    if mode == 1:
        return math.copysign(float1,float2)
    elif mode == 2:
        return math.cos(float1)
    elif mode == 3:
        return math.degrees(float1)
    elif mode == 4:
        return math.e
    elif mode == 5:
        return math.pi
    elif mode == 6:
        return math.tan(float1)
    elif mode == 7:
        return math.sqrt(float1)
    elif mode == 8:
        return math.sin(float1)
    elif mode == 9:
        return math.radians(float1)
    elif mode == 10:
        return math.pow(float1,float2)
    elif mode == 11:
        return math.modf(float1)
    elif mode == 12:
        return math.log(float1,float2)
    elif mode == 13:
        return math.ldexp(float1,float2)
    elif mode == 14:
        return not math.isnan(float1)
    elif mode == 15:
        return not math.isinf(float1)
    elif mode == 16:
        return math.factorial(int(float1))
    elif mode == 17:
        return math.fabs(float1)
    elif mode == 18:
        return math.exp1(float1)
    elif mode == 19:
        return math.exp(float1)
    else:
        raise TypeError("TypeError:类型错误！")
