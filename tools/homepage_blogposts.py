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
        f.write("""<h3><a href="./pages/projects/allposts.html">Blog</a></h3>\n
                <hr>\n<ul>""")
        for post in reversed(blogposts):
            postname = post[1+post.rfind('-'):]
            f.write(f"""<li><a href="./pages/blog/{post}">{postname}</a></li>\n""")
        f.write("</ul>")

if __name__=='__main__':
    run()

