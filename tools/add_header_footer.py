#uses the beautiful soup DOM to add the header and footer to a page
from bs4 import BeautifulSoup as bs
from os import path

def run(page_soup:bs)->bs:
    root_dir = path.dirname(__file__)[:-5]
    fragments = root_dir+'/static/fragments/'
    with open(fragments+'header.html') as header_data, \
         open(fragments+'footer.html') as footer_data:
        page_soup.find("header").append(bs(header_data, 'html.parser'))
        page_soup.find('footer').append(bs(footer_data, 'html.parser'))
    return page_soup

