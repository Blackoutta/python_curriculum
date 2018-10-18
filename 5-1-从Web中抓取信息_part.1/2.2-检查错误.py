如果在刚才的脚本中，我们输入了错误的地址，比如：
--------------------------------------------------------------------------------
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/hahahahahahhahaha/pg1112.txt')
--------------------------------------------------------------------------------
地址虽然会404，但程序却不会终止，这样很容易后续程序崩溃。
所以我们要防患于未然，如果 requests.get()出现任何问题，我们要马上终止程序并显示错误提示
这里我们只需要用一个简单的方法来完成： requests.raise_for_status()
--------------------------------------------------------------------------------
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/hahahahahahhahaha/pg1112.txt')
res.raise_for_status()
--------------------------------------------------------------------------------


如果你觉得这个错误提示太吓人，你可以用 try except 来自定义一下：
--------------------------------------------------------------------------------
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/sdfsf/pg1111.txt')
try:
    res.raise_for_status()
except Exception as err:
    print("哦豁！出错了！错误是：{}".format(err))
--------------------------------------------------------------------------------
