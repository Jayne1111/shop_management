#!/usr/bin/python3
# -*- coding: utf-8 -*-

import user_reg_login
import sys
import pymysql


conn = pymysql.connect("127.0.0.1", "fxj", "123456", "fxjdb")
# 获取一个游标对象(Cursor类)，用于执行SQL语句
cur = conn.cursor()

# 仓库
bar = dict()
# 商品清单
shangpin_list = []
# 商品数量
shangpin_numbers = []

# def goods_list():
#     '''
#     显示商品信息列表
#     '''

    # # 执行任意支持的SQL语句
    # cur.execute("select * from goods")
    # # 通过游标获取执行结果
    # rows = cur.fetchall()
#     print("-" * 70)
#     print("%13s%40s%10s%10s" % ("ID","条码", "商品名称", "单价","数量")) 


#     # 记录商品的价格
#     sum = 0
#     # 遍历代表购物清单的list列表
#     for i,item in list(shangpin_list,start=1):
#         # 转换id为索引加1
#         pid = i
#         # 获取该购物项的第1个元素：商品条码
#         pcode = item[0]
#         # 获取商品条码读取商品，再获取商品的名称
#         pname = bar[pcode][1]
#         # 获取商品条码读取商品，再获取商品的单价
#         price = bar[pcode][2]
#         # 获取该购物项的第2个元素：商品数量
#         pnumber = item[1]
        
#         # 小计
#         amount = price * pnumber
#         # 总计
#         sum = sum + amount

#         line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
#             (pid, pcode, pname, price, pnumber, amount)
#         print(line)
#     print("-" * 70)
#     print("                          总计: " , sum)
# print("=" * 70)

# 初始化商品
def start_shangpin():
    # 遍历商品生成仓库字典
    for i in range(len(shangpin_numbers)):
        start_shangpin[shangpin_numbers[i][0]] = shangpin_numbers[i]

# 显示超市的商品清单，就是遍历代表仓库的dict字典
def show_goods(): 
    # 执行任意支持的SQL语句
    cur.execute("select * from goods")
    # 通过游标获取执行结果
    rows = cur.fetchall()

    print("%13s%40s%10s%10s" % ("条码", "商品名称", "单价","数量"))     
    
    # 遍历仓库所有的value值显示商品清单
    for s in bar.values():
        s = tuple(s)
        print("%15s%40s%12s%12s" % s)

# 显示商品清单，就是遍历代表购物清单的list列表
def goods_list():
    # 执行任意支持的SQL语句
    cur.execute("select * from goods where pcode=%s", goods_pcode)
    # 通过游标获取执行结果
    rows = cur.fetchall()

    print("=" * 70)


    if not shangpin_list:
        print("还未选购商品！")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 70)
        
        # 记录商品的价格
        sum = 0
        # 遍历代表购物清单的list列表
        for i,item in list(shangpin_list,start=1):
            # 转换id为索引加1
            pid = i
            # 获取该购物项的第1个元素：商品条码
            pcode = item[0]
            # 获取商品条码读取商品，再获取商品的名称
            pname = bar[pcode][1]
            # 获取商品条码读取商品，再获取商品的单价
            price = bar[pcode][2]
            # 获取该购物项的第2个元素：商品数量
            pnumber = item[1]
            
            # 小计
            amount = price * pnumber
            # 总计
            sum = sum + amount

            line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
                (pid, pcode, pname, price, pnumber, amount)
            print( line )
        print("-" * 100)
        print("                          总计: " , sum)
    print("=" * 100)


def sys_root():
    show_goods()
    print("欢迎进入万万达购物超市")
    print("=" * 100)
    while True:
        print('''购物车操作指令：
        添加商品(a)   修改(m)   删除(d)   结算(p)   后台管理(r)
        ''')
        n = input("请输入操作序号>>")
        if n == "a":
            goods_pcode = int(input("请输入商品条码："))
            goods_name = int(input("请输入商品名称："))
            goods_pnumber = int(input("请输入商品数量："))
        elif n == "m":
            goods_ID = int(input("请输入需要修改的商品ID："))
            goods_pnumber = int(input("请输入新的购买数量："))
        elif n == "d":
            goods_del = int(input("请输入要删除的商品ID："))
        elif n == "p":
            print("欢迎下次再来！")
            # conn.close()
            break
        elif n == "r":
            goods_list()
            print('''欢迎进入超市后台管理平台，后台操作指令：
            添加商品(a)  修改商品(m)  下架商品(d)  退出(q)
            ''')
            n = input("请输入操作序号>>")
            if n == "a":
                goods_pcode = int(input("请输入商品条码："))
                goods_name = int(input("请输入商品名称："))
                goods_price = int(input("请输入商品价格："))
                goods_pnumber = int(input("请输入商品数量："))
                if user_reg_login.goods_info(goods_pcode,goods_name,goods_price,goods_pnumber):
                    print("商品添加成功！")
                else:
                    print("商品添加失败！")

            if n == "m":
                goods_pcode = int(input("请输入商品条码："))
                goods_name = int(input("请输入修改后的商品名称："))
                goods_price = int(input("请输入修改后的商品价格："))
                goods_pnumber = int(input("请输入修改后的商品数量："))
                if user_reg_login.mod_goods_info(goods_pcode,goods_name,goods_price,goods_pnumber):
                    print("商品修改成功！")
                else:
                    print("商品修改失败")
            if n == "d":
                good_pcode = int(input("请输入要下架的商品条码："))
                if user_reg_login.del_goods_info(goods_pcode):
                    print("商品成功下架！")
                else:
                    print("商品下架失败！")
        else:
            print("请输入正确的操作指令！")
            
start_shangpin()
show_goods()


while True:
    goods_list()
    sys_root()
    
   

def user_login():
    '''
    用户登录
    '''
    uname = input("请输入用户名：")
    passwd = input("请输入密码：")
    if user_reg_login.check_uname_passwd(uname,passwd):
        print("登录失败")
    else:
        print("登录成功")
        sys.root()
        sys.exit(1)


def user_reg():
    '''
    用户注册
    '''
    uname = input("请输入用户名：")
    passwd = input("请输入密码：")
    phone = input("请输入手机号：")
    email = input("请输入邮箱：")
    if not user_reg_login.user_reg(uname,passwd,phone,email):
        print("注册失败")
    else:
        print("用户%s注册成功！" % uname)
        

print(
    '''
    欢迎登录本系统：
    1. 登录
    2. 注册
    3. 退出
    '''
)

n = int(input("请输入操作序号>>"))
if n == 1:
    user_login()
elif n == 2:
    user_reg()
elif n == 3:
    print("感谢你的使用，欢迎下次登录！")
    sys.exit(1)

