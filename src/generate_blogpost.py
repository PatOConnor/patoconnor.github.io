from os import path
from bs4 import BeautifulSoup
from sys import argv
from datetime import date

current_date = str(date.today())
title = argv[1]
page_link = argv[2]
dirname = path.dirname(__file__)

with open(dirname+'\\blogpost_template.html') as blog_template:
    tmplt = BeautifulSoup(blog_template, 'html.parser')
with open(dirname[:-3]+'\\blog\\'+page_link) as post_data: 
    new_post = BeautifulSoup(post_data, 'html.parser')
print(tmplt.prettify())
title_tag = tmplt.find("title")
blog_title_div = tmplt.find(id="blogpost-title")
blog_text_div = tmplt.find(id="blogpost-text")

title_tag.append(title)
blog_title_div.append(title)
blog_text_div.append(new_post)

with open(dirname[:-3]+'\\pages\\'+current_date+'.html', 'w') as f:
    f.write(tmplt.prettify())