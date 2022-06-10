#goes through and updates all pages. Should run once a 
import make_homepage, make_blog_index, make_projects_index, \
       refresh_blogposts, homepage_blogposts

#create webpages for individual posts if not present
refresh_blogposts.run()

#create inner HTML of recent projects for homepage, saves to /static/fragments
homepage_blogposts.run()

#create index of projects based on contents of projects and posts folders
make_projects_index.run()
make_blog_index.run()

#update homepage
make_homepage.run()