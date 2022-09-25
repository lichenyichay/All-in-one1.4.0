

def pingmiantuxingjisuanqi(huida: object) -> object:
    """
    :param huida:选择的图形
    :return 0:正常，1：未找到
    """
    while True:
        if huida == "正方形":
            huida1 = input("请输入计算的是面积、边长之和还是折纸盒问题（剪掉的只能是小正方形）：")
            huida2 = float(input("请输入边长："))
            if huida1 == "面积":
                shuchu: float = huida2 ** 2
                print("面积是：" + str(shuchu))
            elif huida1 == "边长之和":
                shuchu = huida2 * 4
                print("边长之和是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida3 = float(input("请输入被剪掉的小正方形的边长："))
                V = (huida2 - 2 * huida3) ** 2
                S = huida2 ** 2 - ((huida3 ** 2) * 4)
                print("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                print("不支持此功能！")
        elif huida == "长方形":
            huida1 = input("请输入计算的是面积、周长还是折纸盒问题（剪掉的只能是小正方形）：")
            huida2 = float(input("请输入长："))
            huida3 = float(input("请输入宽："))
            if huida1 == "面积":
                shuchu = huida2 * huida3
                print("面积是：" + str(shuchu))
            elif huida1 == "周长":
                shuchu = (huida2 + huida3) * 2
                print("周长是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida4 = float(input("请输入被剪掉的小正方形的边长："))
                V = (huida2 - (2 * huida4)) * (huida3 - (2 * huida4))
                S = huida2 * huida3 - (huida4 ** 2 * 4)
                print("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                print("不支持此功能！")
        elif huida == "平行四边形":
            huida1 = int(
                input("请输入要计算的是面积、周长还是折纸盒问题（剪掉的必须是平行四边形，且平行四边形的四条边长度均相等）"))
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            huida4 = float(input("请输入斜边的长度："))
            if huida1 == "面积":
                shuchu = huida2 * huida3
                print("面积是：" + str(shuchu))
            elif huida1 == "周长":
                shuchu = (huida2 + huida4) * 2
                print("周长是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida5 = float(input("请输入被剪掉的平行四边形的边长："))
                S = huida2 * huida3 - (huida4 ** 2) * 4
                V = huida5 * ((huida4 - 2 * huida5) * (huida2 - 2 * huida5))
                print(f"体积是：{str(V)},表面积是：{str(S)}")
            else:
                print("不支持此功能！")
        elif huida == "菱形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = huida2 * huida3
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                shuchu = huida2 * 4
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "三角形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = huida2 * huida3 / 2
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                huida4 = float(input("请输入其中1条腰长："))
                huida5 = float(input("请输入另1条腰长："))
                shuchu = huida2 + huida4 + huida5
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "梯形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入上底："))
            huida3 = float(input("请输入下底："))
            huida4 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = (huida2 + huida3) * huida4 / 2
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                huida5 = float(input("请输入其中1条腰长："))
                huida6 = float(input("请输入另1条腰长："))
                shuchu = huida2 + huida3 + huida5 + huida6
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "圆形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入半径："))
            if huida1 == "面积":
                shuchu = 3.14 * (huida2 ** 2)
                print(f"面积是：{shuchu}")
            elif huida1 == "周长":
                shuchu = 2 * 3.14 * huida2
                print(f"周长是：{shuchu}")
            else:
                print("不支持此功能！")
        else:
            # print("暂不支持此图形的计算！！！")
            # print("退出中......")
            # time.sleep(2)
            return 1
            break

    return 0
# pingmiantuxingjisuanqi("Hello")
