PI = 3.14


def litituxingjisuanqi(huida):
    while True:
        if huida == "长方体":
            huida1 = input("请输入计算的是体积、表面积、棱长总和、容积还是染色问题（包含底面，且长宽高均为整数）：")
            huida2 = float(input("请输入长："))
            huida3: float = float(input("请输入宽："))
            huida4 = float(input("请输入高："))
            if huida1 == "体积":
                shuchu = huida3 * huida3 * huida4
                print("体积是：" + str(shuchu))
            elif huida1 == "表面积":
                shuchu = (huida3 * huida3 + huida3 * huida4 + huida3 * huida4) * 2
                print("表面积是：" + str(shuchu))
            elif huida1 == "染色问题":
                huida2 = int(huida2)
                huida3 = int(huida3)
                huida4 = int(huida4)
                if huida4 == 1:
                    print("4个面染色的小正方体有4个。")
                    print("3个面染色的小正方体有" + str((huida2 - 2) * 2 + (huida3 - 2) * 2) + "个。")
                    print("2个面染色的小正方体有" + str((huida2 - 2) * (huida3 - 2)) + "个。")
                else:
                    print("3个面染色的小正方体有8个。")
                    print("2个面染色的小正方体有" + str(((huida2 - 2) + (huida3 - 2) + (huida4 - 2)) * 4) + "个。")
                    print("1个面染色的小正方体有" + str(((huida2 - 2) * (huida3 - 2) + (huida2 - 2) * (huida4 - 2) + (
                            huida3 - 2) * (huida4 - 2)) * 2) + "个。")
                    print("0个面染色的小正方体有" + str((huida2 - 2) * (huida3 - 2) * (huida4 - 2)) + "个")
            elif huida1 == "棱长总和":
                shuchu = (huida3 + huida3 + huida4) * 4
                print("棱长总和是：" + str(shuchu))
            elif huida1 == "容积":
                shuchu = huida3 * huida3 * huida4
                print("容积是：" + str(shuchu))
            else:
                print("不支持此功能")
        elif huida == "正方体":
            huida1 = input("请输入计算的是体积、表面积、棱长总和、容积还是染色问题（包含底面，且长宽高均为整数）：")
            huida3 = float(input("请输入棱长："))
            if huida1 == "体积":
                shuchu = huida3 ** 3
                print("体积是：" + str(shuchu))
            elif huida1 == "表面积":
                shuchu = huida3 ** 2 * 6
                print("表面积是" + str(shuchu))
            elif huida1 == "棱长总和":
                shuchu = huida3 * 12
                print("棱长总和" + str(shuchu))
            elif huida1 == "容积":
                shuchu = huida3 ** 3
                print("容积是：" + str(shuchu))
            elif huida1 == "染色问题":
                huida3 = int(huida3)
                if huida3 == 1:
                    print("6个面染色的小正方体有1个")
                else:
                    print("3个面染色的小正方体有8个。")
                    print("2个面染色的小正方体有" + str((huida3 - 2) * 12) + "个。")
                    print("1个面染色的小正方体有" + str((huida3 - 2) ** 2 * 6) + "个。")
                    print("0个面染色的小正方体有" + str((huida3 - 2) ** 3) + "个。")
            else:
                print("不支持此功能")
        elif huida == "圆柱":
            huida1 = input("请输入计算的是体积、表面积、容积还是侧面积：")
            huida2 = float(input("请输入半径："))
            huida3 = float(input("请输入高："))
            if huida1 == "体积":
                shuchu = PI * (huida2 ** 2) * huida3
                print("体积是：" + str(shuchu))
            elif huida1 == "表面积":
                shuchu = huida3 ** 2 * 6
                print("表面积是" + str(shuchu))
            elif huida1 == "侧面积":
                shuchu = 2 * PI * huida3
                print("侧面积是" + str(shuchu))
            elif huida1 == "容积":
                shuchu = PI * (huida2 ** 2) * huida3
                print("容积是：" + str(shuchu))
        else:
            # print("暂不支持此图形的计算！！！")
            # print("退出中......")
            # time.sleep(2)
            return 1
            break
    return 0
