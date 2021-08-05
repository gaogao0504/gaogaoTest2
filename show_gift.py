# from pythoncode.gift import have_gift
import gift


def show_gift():
    # 方法可以使用外部变量
    if gift.have_gift == True:
        print('收到礼物啦，好开心。')
    else:
        print('等待礼物中')