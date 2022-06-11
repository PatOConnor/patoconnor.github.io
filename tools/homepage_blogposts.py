#gets list of five most recent blogposts and saves
#HTML snippet it to /static/fragments
from os import listdir, path
POSTS_TO_GRAB = 5
def run():
    #filenames are in YYYY-MM-DD so slicing from end yields most recent
    dirname = path.dirname(__file__)[:-5]
    blogposts = listdir(dirname+'static/posts')[-POSTS_TO_GRAB:]
    
    with open(dirname+'/static/fragments/blog-links.html', 'w+') as f:
        #add link to div
        f.write("""<h3><a href="./pages/allposts.html">Blog</a></h3>\n
                \n<ul class="naked-list">""")
        for post in reversed(blogposts):
            postdate = post[:post.rfind('-')]
            postname = post[1+post.rfind('-'):post.rfind('.')]
            f.write(f"""<li class="list-link"><a href="./pages/blog/{post}">{postdate}   {postname}</a></li>\n""")
        f.write("</ul>")

if __name__=='__main__':
    run()

