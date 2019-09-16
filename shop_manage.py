# 定义仓库
repository = dict()
# 定义购物清单对象
shop_list = []
# 定义仓库里商品数量
shangpin = [["1000001", "你好世界", 88.0, 10],
["1000002", "python讲义", 69.0, 12],
["1000003", "奥利奥", 29.0, 188],
["1000004", "算法结构", 88.0, 56],
["1000005", "巧克力", 108.0, 100],
["1000006", "世界起源", 77.0, 122]]
# 定义一个函数来初始化商品
def init_repository():
    # 遍历商品生成仓库dict字典
    for i in range(len(shangpin)) :
        repository[shangpin[i][0]] = shangpin[i]
#显示超市的商品清单，就是遍历代表仓库的dict字典
def show_goods():
    print("欢迎来到万万达")
    print('万万达的商品清单:')
    print("%13s%40s%10s%10s" % ("条码", "商品名称", "单价","数量"))
    # 遍历repository的所有value来显示商品清单
    for s in repository.values():
        s = tuple(s)
        print("%15s%40s%12s%12s" % s)
# 显示购物清单，就是遍历代表购物清单的list列表
def show_list():
    print("=" * 100)
    # 如果清单不为空的时候，输出清单的内容
    if not shop_list:
        print("还未购买商品")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        # 记录总计的价钱
        sum = 0
        # 遍历代表购物清单的list列表
        for i, item in enumerate(shop_list,start=1):
            # 转换id为索引加1
            id = i 
            # 获取该购物项的第1个元素：商品条码
            code = item[0]
            # 获取商品条码读取商品，再获取商品的名称
            name = repository[code][1]
            # 获取商品条码读取商品，再获取商品的单价
            price = repository[code][2]
            # 获取该购物项的第2个元素：商品数量
            number = item[1]
            # 小计
            amount = price * number
            # 计算总计
            sum = sum + amount
            line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
                (id, code, name, price, number, amount)
            print( line )
        print("-" * 100)
        print("                          总计: " , sum)
    print("=" * 100)
# 添加购买商品，就是向代表用户购物清单的list列表中添加一项。
def add():
    # 等待输入条码
    code = input("请输入商品的条码:\n")
    # 没有找到对应的商品，条码错误
    if code not in repository:
        print("条码错误，请重新输入")
        return        
    # 根据条码找商品
    goods = repository[code]
    # 等待输入数量
    number = input("请输入购买数量:\n")
    # 把商品和购买数量封装成list后加入购物清单
    shop_list.append([code, int(number)])
# 修改购买商品的数量，就是修改代表用户购物清单的list列表的元素
def edit():
    id = input("请输入要修改的购物明细项的ID:\n")
    # id减1得到购物明细项的索引
    index = int(id) - 1
    # 根据索引获取某个购物明细项
    item = shop_list[index]
    # 提示输入新的购买数量
    number = input("请输入新的购买数量:\n")
    # 修改item里面的number
    item[1] = int(number)
# 删除购买的商品明细项，就是删除代表用户购物清单的list列表的一个元素。
def delete():
    id = input("请输入要删除的购物明细项的ID: ")
    index = int(id) - 1
    # 直接根据索引从清单里面删除掉购物明细项
    del shop_list[index]
def payment():
    # 先打印清单
    show_list()
    print('\n' * 3)
    print("欢迎下次光临")
    # 退出程序
    import os
    os._exit(0) 
# 后台添加商品函数
def adds():
    # 获取要添加的商品信息
    a = input("请输入商品条码:")
    b = input('请输入商品名称:')
    c = input('请输入商品单价:')
    d = input('请输入商品数量:')
    # 添加到商品列表
    shangpin.append([a,b,c,d])
    # 重新打印商品清单
    init_repository()
    show_goods()
# 后天修改商品属性函数
def edits():
    a = input("请输入商品条码:")
    # 获取此商品条码的新的值
    if a in repository.keys():
       e = input("请输入修改后商品名字:")
       f = input("请输入修改后商品单价:")
       g = input("请输入修改后商品数量:")
       repository.update({a:[a,e,f,g]})
       print(repository[a])
       show_goods()
    else:
       print('输入条码有误')
def deletes():
    h = input('请输入您要下架商品条码:')
    # 直接根据条码从仓库里面删除掉此商品
    repository.pop(h)
    show_goods()
# 重新打印商品清单
def show_good():
    show_goods()
# 后台支持的操作
cmd_dicts = {'a': adds, 'e': edits, 'd': deletes, 's': show_good, 'q': quit}
def root():
    # 先打印清单
    show_goods()
    print("欢迎进入超市货品管理平台")
    print("=" * 100)
    while True:
        cmds = input("后台操作指令: \n" +
            "    添加商品(a)  修改商品(e)  删除商品(d)  全部商品(s)  退出(q)\n") 
        if cmds == 'q' :
            return
        elif cmds not in cmd_dicts:
            print("好好玩，行吗！")
        else:
            cmd_dicts[cmds]()
# 用户所支持的操作
cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's': show_goods, 'r': root }
# 初始仓库并展示
init_repository()
show_goods()
# 显示命令提示
def show_command():
    # 等待命令
    cmd = input("用户操作指令: \n" +
        "    添加(a)  修改(e)  删除(d)  结算(p)  超市商品(s)  后台管理(r)\n")
    # 如果用户输入的字符没有对应的命令   
    if cmd not in cmd_dict:
        print("不要玩，好不好！")
    else:
        cmd_dict[cmd]()
# 显示清单和操作命令提示
while True:
    show_list()
    show_command()