有时候，我们手头有一个列表或者字符串，但是我们并不想将它们作为一个整体使用，我们只需要它们其中的一段，或者一个切片(slice)。

问题：
    假设用户输入了这样一个URL的字符串："https://www.google.com"
    你想从中提取网站的名称 "google"，怎么办？

例子：
    URL = "https://www.google.com"
    url_name = URL[12:-4]
    print(url_name)

解读：
    slice的基本格式为： object[start:stop]
    简单的来说，使用两个索引，中间以'冒号'隔开，则可以取一个对象的切片。
    'start' 代表切片从哪个索引开始。
    'stop' 代表切片到哪个索引结束。'注意，stop的索引不会成为切片的一部分'!

    # 一些例子，可以自己在REPL中练习
    "apple"[0:3] 会返回 "app"
    "apple"[:3] 会返回 "app" #这是一种简写，省略了start就意味着切片会从0开始

    "apple"[2:5] 会返回 "ple"
    "apple"[2:-1] 会返回 "pl" #跟索引一样，-1代表最后一位
    "apple"[2:] 会返回 "ple" #这是一种简写，省略了stop就意味着切片会延伸到最后

    "apple"[:] 会返回 "apple"
