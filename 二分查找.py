import time


def binarysearch(yuanlst, shengxulst, target):
    start = 0
    start_time = time.time()
    count = 0
    end = len(shengxulst) - 1
    if target not in shengxulst:
        end_time = time.time()
        return "列表中未查找到目标值" + str(target) + "，共用时" + str(end_time - start_time) + "s，查找次数：0，索引：无"
    while True:
        count += 1
        mid = (start + end) // 2
        if target < shengxulst[mid]:
            end = mid - 1
            continue
        elif target > shengxulst[mid]:
            start = mid + 1
            continue
        else:
            end_time = time.time()
            return "列表中已查找到目标值" + str(target) + "，共用时" + str(end_time - start_time) + "s，查找次数：" + str(
                count) + "，原列表中索引：" + str(yuanlst.index(target))
