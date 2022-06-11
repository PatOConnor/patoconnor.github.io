from os import path
from bs4 import BeautifulSoup
import add_header_footer
from sys import argv

def run(page_link):
    # delim_end = page_link.rfind('.')
    # post_title = page_link[:delim_end]

    dirname = path.dirname(__file__)
    template_dir = dirname[:-5]+'static/templates'
    projects_dir = dirname[:-5]+'static/projects/'

    with open(template_dir+'\\template_projectpost.html') as blog_template:
        tmplt = BeautifulSoup(blog_template, 'html.parser')
    with open(projects_dir+page_link) as post_data: 
        new_post = BeautifulSoup(post_data, 'html.parser')

    tmplt = add_header_footer.run(tmplt)
    tmplt.find('div', {'id':'project-info'}).append(new_post)

    with open(dirname[:-5]+'patsite-no-js/pages/projects/'+page_link, 'w') as f:
        f.write(tmplt.prettify())

if __name__=='__main__':
    page_link = argv[1]
    run()