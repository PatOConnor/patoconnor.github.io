from audioop import add
from os import path, listdir
from bs4 import BeautifulSoup
import add_header_footer
def run():
    dirname = path.dirname(__file__)
    index_dir = dirname[:-5]+'patsite-no-js/pages/'
    template_dir = dirname[:-5]+'static/templates'
    filename = 'allposts.html'
    blogposts = listdir(index_dir+'/blog')
    with open(template_dir+'/template_index.html') as f:
        tmplt = BeautifulSoup(f, 'html.parser')

    tmplt = add_header_footer.run(tmplt)

    posts_list = tmplt.find('ul', {'id':'content-list'})
    for post_link in reversed(blogposts):
        new_item = tmplt.new_tag('li')
        new_item['class'] = 'list-link'

        new_link = tmplt.new_tag('a')
        #set href to post link in full
        new_link['href'] = './blog/'+post_link
        #set title to the chunk at the end between final - and file extension
        new_link.append(post_link[1+post_link.rfind('-'):post_link.rfind('.')])
        #put it together
        new_item.append(new_link)
        posts_list.append(new_item)
    with open(index_dir+filename, 'w+') as f:
        f.write(tmplt.prettify())

if __name__=='__main__':
    run()
