from os import path
from bs4 import BeautifulSoup
from sys import argv

def run(page_link):
    hyphen = page_link.rfind('-')
    dot = page_link.rfind('.')
    post_title = page_link[1+hyphen:dot]

    dirname = path.dirname(__file__)
    template_dir = dirname[:-5]+'static/templates'
    blogpost_dir = dirname[:-5]+'static/posts/'

    with open(template_dir+'\\template_blogpost.html') as blog_template:
        tmplt = BeautifulSoup(blog_template, 'html.parser')
    with open(blogpost_dir+page_link) as post_data: 
        new_post = BeautifulSoup(post_data, 'html.parser')
    #print(tmplt.prettify())
    title_tag = tmplt.find("title")
    blog_title_div = tmplt.find(id="blogpost-title")
    blog_text_div = tmplt.find(id="blogpost-text")
    
    title_tag.append(post_title)
    blog_title_div.append(post_title)
    blog_text_div.append(new_post)

    with open(dirname[:-5]+'patsite-no-js/pages/blog/'+page_link, 'w') as f:
        f.write(tmplt.prettify())

if __name__=='__main__':
    page_link = argv[1]
    run()