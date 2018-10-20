import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file, features="html.parser")
span_elems = example_soup.select('span')[0] #由于网页中只有一个span，这里我就直接把它的索引设定上去了
id = span_elems.get('id')  # 应该返回 'author'
print(id)
