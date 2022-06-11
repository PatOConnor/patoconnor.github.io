import make_projectpost
from os import path, listdir

def run():
    dirname = path.dirname(__file__)[:-5]
    rawdir = dirname+'/static/projects/'
    posts = listdir(rawdir)
    for post in posts:
        make_projectpost.run(post)

if __name__=='__main__':
    run()
