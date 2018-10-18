import requests, os

os.mkdir("lessons")
file_number = 1

while file_number < 27:
    print("正在下载: 文件{}".format(file_number))
    res = requests.get('https://www.hulaoshi.tech/res/lesson_{}.7z'.format(file_number))
    try:
        res.raise_for_status()
    except Exception as err:
        print("哦豁！出错了！错误是：{}".format(err))

    playFile = open('lessons/{}.7z'.format(file_number), 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    playFile.close()
    print("文件{}下载完毕".format(file_number))
    file_number += 1
