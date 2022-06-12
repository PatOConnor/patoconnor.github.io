# TODO modify blog post injector to inject legal blurb
from os import path
from bs4 import BeautifulSoup
import add_header_footer

def run():
    dirname = path.dirname(__file__)
    template_dir = dirname[:-5]+'static/templates'
    page = dirname[:-5]+'static/fragments/allprojects.html'

    with open(template_dir+'\\template_index.html') as blog_template:
        tmplt = BeautifulSoup(blog_template, 'html.parser')
    with open(page) as post_data: 
        new_post = BeautifulSoup(post_data, 'html.parser')
        print(new_post.prettify())
    #print(tmplt.prettify())
    content_div = tmplt.find('ul')
    content_div.append(new_post)
    #that quick fix requires the header to be added after
    tmplt = add_header_footer.run(tmplt)

    with open(dirname[:-5]+'patsite-no-js/pages/allprojects.html', 'w') as f:
        f.write(tmplt.prettify())

if __name__=='__main__':
    run()