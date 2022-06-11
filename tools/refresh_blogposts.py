# goes through files in /static/posts and checks if there is a 
# corresponding file in nojs/pages/blog
# if there is no corresponding file, make one.
import make_blogpost
from os import path, listdir

def run():
    dirname = path.dirname(__file__)[:-5]
    rawdir = dirname+'/static/posts/'
    posts = listdir(rawdir)
    for post in posts:
        make_blogpost.run(post)

if __name__=='__main__':
    run()

