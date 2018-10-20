soup对象有个比较实用的方法 .get()
我们可以让它返回一个标签的属性的值

代码:
--------------------------------------------------------------------------------
import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file, features="html.parser")
span_elems = example_soup.select('span')[0] #由于网页中只有一个span，这里我就直接把它的索引设定上去了
id = span_elems.get('id')
print(id)  # 应该打印出 'author'
