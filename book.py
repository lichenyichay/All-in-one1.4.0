import os,time,csv,shutil
book = {}   # 书名字典，格式：书名:本数
jiebook = {} # 借书清单

def jieshu(name,count):          #借书
    if name in book.keys():
        if book[name] < 0:
            del book[name]
        if name not in jiebook.keys():
            book[name] -= count
            jiebook.update({name:1})
            if book[name] < 0:
                del book[name]
            print("借书成功！")
            return 0
        else:
            print("请先还书后再借阅，操作失败！")
            return 1
    else:
        print("书目不存在，操作失败！")
        return 1
def huanshu(name,count):          #还书
    if name in book.keys():
        if name in jiebook.keys():
            book[name] += count
            jiebook[name] -= count
            if book[name] < 0:
                del book[name]
            if jiebook[name] < 0:
                del jiebook[name]
            print("还书成功！")
            return 0
        else:
            print("未查询到借阅记录，无法还书，操作失败！")
            return 1
    else:
        print("书目不存在！")
        return 1
def jiashu(name,count):          #在库存内加书
    if name in book.keys():
        book[name] += count
    else:
        book[name] = count
    print("操作成功！")
    return 0
def jianshu(name,count):       #在库存内减书
    if name in book.keys():
        book[name] -= count
        if book[name] < 0:
            del book[name]
        print("操作成功！")
        return 0
    else:
        print("书目不存在，操作失败！")
        return 1
def jiebooksavetocsv(mode):
    try:
        with open("D:\\图书管理系统\\借书清单.csv",mode,encoding="UTF-8",newline="") as f:
            csv_writer = csv.writer(f)
            for i in jiebook:
                csv_writer.writerow([i,jiebook[i]])
    except:
        with open("D:\\图书管理系统\\借书清单.csv","w",encoding="UTF-8",newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["书名","本数"])
            for i in jiebook:
                csv_writer.writerow([i,jiebook[i]])
def booksavetocsv(mode):
    try:
        with open("D:\\图书管理系统\\图书清单.csv",mode,encoding="UTF-8",newline="") as f:
            csv_writer = csv.writer(f)
            for i in book:
                csv_writer.writerow([i,book[i]])
    except:
        with open("D:\\图书管理系统\\图书清单.csv","w",encoding="UTF-8",newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["书名","本数"])
            for i in book: 
                csv_writer.writerow([i,book[i]])
def printjiebook():
    print("------借书清单------")
    print("书名          本数")
    for i in jiebook:
        print(i,"        ",jiebook[i])
    jiebooksavetocsv("w")
    return 0
def bookquery(name):
    a = {}
    for i in book.keys():
        if name in i:
            a[i] = book[i]
    if len(a) != 0:
        print("------查询结果------")
        print("书名          本数")
        for i in a:
            print(i,"        ",a[i])
    else:
        print("查询失败！")
        return 1
    return 0
def printbook():
    print("------库存清单------")
    print("书名          本数")
    for i in book:
        print(i,"        ",book[i])
    booksavetocsv("w")
    return 0
def startmenu():
    print("------处理原数据------")
    print("1、初始化（删除）")
    print("2、保留")
    return 0
