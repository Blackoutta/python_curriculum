import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file, features="html.parser")
p_elems = example_soup.select('p')

for i in p_elems:
    print(i.getText())
