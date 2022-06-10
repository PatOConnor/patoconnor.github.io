from os import path
from bs4 import BeautifulSoup as bs
def run():
    root_dir = path.dirname(__file__)[:-5]
    templates = root_dir+'/static/templates/'
    fragments = root_dir+'/static/fragments/'
    staticsite = root_dir+'patsite-no-js/'


    with open(templates+'template_home.html') as homepage, \
        open(fragments+'header.html') as header_data, \
        open(fragments+'project-links.html') as project_links_data, \
        open(fragments+'blog-links.html') as blog_links_data, \
        open(fragments+'footer.html') as footer_data:

        tmplt = bs(homepage, 'html.parser')
        tmplt.find("header").append(bs(header_data, 'html.parser'))
        tmplt.find('div', {'id':'project-links'}).append(bs(project_links_data, 'html.parser'))
        tmplt.find('div', {'id':'blog-links'}).append(bs(blog_links_data, 'html.parser'))
        tmplt.find('footer').append(bs(footer_data, 'html.parser'))

        with open(staticsite+'home.html','w') as staticpage:
            staticpage.write(tmplt.prettify())
if __name__=='__main__':
    run()