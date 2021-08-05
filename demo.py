# a = 1
#
#
# # 变量的类型根据值来展示
# def demo1():
#     # 告诉解释器。现在要使用外面的全局a
#     global a
#     # 变量会就近取之，变量可改变
#     a = 2
#     print(a)
#     print(id(a))
#     return a
#
#
# # 输出的为none，函数不return的话默认返回none
# print(demo1())
#
#
# # id 变量的存储位置
# # print(id(a))
# # print(a)
#
#
# # python支持嵌套函数，闭包函数
# def outer():
#     def inner():
#         print('i am inner')
#     return inner()
#
#
# outer()
