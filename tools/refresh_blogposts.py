# goes through files in /static/posts and checks if there is a 
# corresponding file in nojs/pages/blog
# if there is no corresponding file, make one.
import generate_blogpost
from os import path, listdir

def run():
    dirname = path.dirname(__file__)[:-5]
    rawdir = dirname+'/static/posts/'
    posts_dirs = ['/patsite-no-js/',]
    post_contents = listdir(rawdir)
    for dir in posts_dirs:
        dir_contents = listdir(dirname+dir)
        #subtract sets to get unmade posts
        unmade_posts = list(set(post_contents).difference(set(dir_contents)))
        for post in unmade_posts:
            generate_blogpost.run(post)

if __name__=='__main__':
    run()

