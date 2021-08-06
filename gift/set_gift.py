"""
实现发礼物
1、默认值（have_gift= False）没有礼物
2、定义一个发礼物的方法
3、定义一个显摆礼物的方法
4、实现发完礼物之后，能展示礼物
"""
# have_gift = False
from pythoncode.gift import gift


def send_gift():
    # global have_gift
    gift.have_gift = True
    print('发礼物啦')


# def show_gift():
#     # 方法可以使用外部变量
#     if have_gift == True:
#         print('收到礼物啦，好开心。')
#     else:
#         print('等待礼物中')


# # 入口函数
# if __name__ == '__main__':
#     send_gift()
#     show_gift()
