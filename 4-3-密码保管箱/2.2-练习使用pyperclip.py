pyperclip有两个方法：
    pyperclip.copy()
    将脚本中的文本复制到'系统剪贴板'

    pyperclip.paste()
    将'系统剪贴板'中的文本粘贴到脚本中

--------------------------------------------------------------------------------
pyperclip.copy() 例子：
import pyperclip

text = "hello world"
pyperclip.copy(text)
# hello world应该会进入你的剪贴板

--------------------------------------------------------------------------------

pyperclip.paste() 例子：
import pyperclip

print("你刚才复制了: {}!".format(pyperclip.paste()))
# 你上一次复制的东西会被打印出来
