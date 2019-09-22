#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

import user_reg_login

# import pymysql


# conn = pymysql.connect("192.168.10.171","fxj","123456","fxjdb"
# cursor = conn.cursor()

# 仓库
bar = dict()
# 商品清单
shangpin_list = []
# 商品数量
shangpin_numbers = []

# 初始化商品
def start_shangpin():
    # 遍历商品生成仓库字典
    for i in range(len(shangpin_numbers)):
        start_shangpin[shangpin_numbers[i][0]] = shangpin_numbers[i]

# 显示超市的商品清单，就是遍历代表仓库的dict字典
def show_goods():   
    # cursor.execute("select * from goods")
    # rows = cursor.fetchall()
    print("%13s%40s%10s%10s" % ("条码", "商品名称", "单价","数量"))     
    
    # 遍历仓库所有的value值显示商品清单
    for s in bar.values():
        s = tuple(s)
        print("%15s%40s%12s%12s" % s)

# 显示商品清单，就是遍历代表购物清单的list列表
def show_list():
    print("=" * 100)
    if not shangpin_list:
        print("还未选购商品！")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        
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


# 添加购买商品，就是向代表用户购物清单的list列表中添加一项。
def add_goods():
    # cursor.execute("select from ")
    # rows = cursor.fetchall()
    pcode = input("请输入商品条形码:\n")
    # 判断条形码是否输入正确
    if pcode not in bar:
        print("条形码错误，请重新输入")
        return

        # 根据条形码找商品
        goods = bar[pcode]

        pnumber = input("请输入商品数量:\n")
        # 把商品和购买数量加入购物清单中
        show_list.append([pcode],int[pnumber])


# 修改购买商品的数量，就是修改代表用户购物清单的list列表的元素
def mod_goods():
    pid = input("请输入要修改的商品ID:\n")
    # id减1得到购物明细项的索引
    index = int(pid) - 1
    # 根据索引获取某个购物明细
    item = show_list[index]

    pnumber = input("请输入新的商品购买数量:\n")
    # 修改item中的pnumber
    item[1] = int(pnumber)


# 删除购买商品的数量，就是修改代表用户购物清单的list列表的元素
def del_goods():
    pid = input("请输入要删除的商品ID:\n")
    index = int(pid) - 1

    del show_list[index]


# 打印要支付的商品清单
def paylist():
    show_list()
    print("\n" * 3)
    print("欢迎下次光临！")
    sys.exit(1)
    

# 后台添加商品
def back_add():
    a = input("请输入商品条码:")
    b = input('请输入商品名称:')
    c = input('请输入商品单价:')
    d = input('请输入商品数量:')
    # 添加到商品列表
    show_list.append([a,b,c,d])
    # 重新打印商品清单
    start_shangpin()
    show_goods

# 后台修改商品
def back_mod():
    a = input("请输入商品条码:")

    # 获取商品条形码新的值
    if a in bar.keys():
        e = input("请输入修改后的商品名称:")
        f = input("请输入修改后的商品单价:")
        g = input("请输入修改后的商品数量:")
        
        bar.update({a:[a,e,f,g]})
        print(bar[a])
        show_goods()
    else:
        print("输入的条形码有误!")

# 后台要删除的商品
def back_del():
    h = input("请输入你要下架的商品")
    bar.pop(h)
    show_goods()

# 重新打印商品清单
def back_goods():
    show_goods()

# 后台可以进行的操作
back_dicts = {'a': back_add,'e':back_mod,'f':back_del,'s':back_goods,'q':quit}


def sys_root():
    show_goods()
    print("欢迎进入万万达购物超市")
    print("=" * 100)
    while True:
        back_sys = print("后台操作指令:\n" + "添加商品(a)  修改商品(e)  删除商品(d)  全部商品(s)  退出(q)\n")
        if back_sys == 'q':
            return
        elif back_sys not in back_dicts:
            print("操作有误，请重新操作！")
        else:
            back_dicts[back_sys]()
for_dicts = {'a': add_goods, 'e': mod_goods, 'd': del_goods, 'p': paylist, 's': show_goods, 'r': sys_root }

        
start_shangpin()
show_goods()

def show_command():
    for_sys = input("用户操作指令:\n"+ "添加(a)  修改(e)  删除(d)  结算(p)  超市商品(s)  后台管理(r)\n")
    if for_sys not in for_dicts:
        print("操作有误，请重新操作！")
    else:
        for_dicts[for_sys]()

while True:
    show_list()
    show_command()
   


def user_reg():
    '''
    函数内容：用户注册
    '''
    user_name = input("请输入用户名：")
    user_passwd = input("请输入密码：")
    user_phone = input("请输入手机号：")
    user_email = input("请输入邮箱：")

    if not user_reg_login.user_reg(user_name,user_passwd,user_phone,user_email):
        print("注册失败！")
    else:
        print("用户%s注册成功！" % user_name)


def user_login():
    '''
    用户登录
    '''
    user_name = input("请输入用户名：")
    user_passwd = input("请输入密码：")
    
    if user_reg_login.check_uname_pwd(user_name,user_passwd):
        print("登录失败！")
    else:
        print("登录成功！")
        sys_root()
        sys.exit(1)

print(
    '''
    欢迎使用本系统
    1.登录
    2.注册
    0.退出
    '''
)

num = int(input("请输入操作序号>"))
if num == 1:
    user_login()
elif num == 2:
    user_reg()
elif num == 0:
    print("感谢你的使用，下次再见！")
    sys.exit(1)



# def system_main():

#     goods_list()

#     while True:
#         print('''购物车操作指令：
#         添加商品(a)   修改(m)   删除(d)   结算(p)   后台管理(r)
#         '''
#         )
#         n = input("请输入操作序号>>")
#         if n == "a":
#             goods_pcode = int(input("请输入商品条码："))
#             goods_pnumber = int(input("请输入商品数量："))
#         elif n == "m":
#             goods_ID = int(input("请输入需要修改的商品ID："))
#             goods_pnumber = int(input("请输入新的购买数量："))
#         elif n == "d":
#             goods_del = int(input("请输入要删除的商品ID："))
#         elif n == "p":
#             print("欢迎下次再来！")
#             # conn.close()
#             break
#         elif n == "r":
#             goods_list()
#             print('''欢迎进入超市后台管理平台，后台操作指令：
#             添加商品(a)  修改商品(m)  下架商品(d)  退出(q)
#             ''')
#             n = input("请输入操作序号>>")
#             if n == "a":
#                 goods_pcode = int(input("请输入商品条码："))
#                 goods_name = int(input("请输入商品名称："))
#                 goods_price = int(input("请输入商品价格："))
#                 goods_pnumber = int(input("请输入商品数量："))
#                 if user_reg_login.goods_info(goods_pcode,goods_name,goods_price,goods_pnumber):
#                     print("商品添加成功！")
#                 else:
#                     print("商品添加失败！")

#             if n == "m":
#                 goods_pcode = int(input("请输入商品条码："))
#                 goods_name = int(input("请输入修改后的商品名称："))
#                 goods_price = int(input("请输入修改后的商品价格："))
#                 goods_pnumber = int(input("请输入修改后的商品数量："))
#                 if user_reg_login.mod_goods_info(goods_pcode,goods_name,goods_price,goods_pnumber):
#                     print("商品修改成功！")
#                 else:
#                     print("商品修改失败")
#             if n == "d":
#                 good_pcode = int(input("请输入要下架的商品条码："))
#                 if user_reg_login.del_goods_info(goods_pcode):
#                     print("商品成功下架！")
#                 else:
#                     print("商品下架失败！")
#         else:
#             print("请输入正确的操作指令！")