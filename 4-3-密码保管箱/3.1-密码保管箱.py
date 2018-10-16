#! python3
# pw.py - 一个密码保管箱程序
import sys
import pyperclip

# 如果没有输入命令行参数，则为用户显示使用方法
if len(sys.argv) < 2:
    print('使用方法: python pw.py [账号名] - 这可以让你从保险箱中取出相应账号的密码并复制到剪贴板上')
    sys.exit()

# 将文件名后面的第一个命令行参数设为变量
account = sys.argv[1]


PASSWORDS = {'gmail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             '163mail': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'wow': '123456'
}

# TODO: 写一个判断式，如果 account 是 PASSWORDS这个字典中的键的话，用pypyerclip.copy()将其值复制到剪贴板
# TODO: 否则打印： 无法找到该账号
