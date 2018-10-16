#! python3
# pw.py - 一个密码保管箱程序
import sys
import pyperclip


if len(sys.argv) < 2:
    print('使用方法: python pw.py [账号名] - 这可以让你从保险箱中取出相应账号的密码并复制到剪贴板上')
    sys.exit()

account = sys.argv[1]


PASSWORDS = {'gmail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             '163mail': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'wow': '123456'
}

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("账号: {}的密码已经复制到剪贴板。".format(account))
else:
    print("无法找到账号: {}".format(account))
