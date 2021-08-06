# 入口函数
#  执行导包的时候也会执行一次方法
from pythoncode.gift.set_gift import send_gift
from pythoncode.gift.show_gift import show_gift
# 访问所有的内置变量
# print(locals())
# --name = --main__ 的时候执行这个
# 当前模块等于__maib__，其他模块不等于
if __name__ == '__main__':
    send_gift()
    show_gift()
