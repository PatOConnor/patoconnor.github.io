#goes through and updates all pages. Should run once a 
import make_homepage, make_blog_index, make_legal, make_allprojects,\
       refresh_blogposts, refresh_projects, homepage_blogposts

refresh_blogposts.run()
refresh_projects.run()

#create inner HTML of recent projects for homepage, saves to /static/fragments
homepage_blogposts.run()

#create index page for blog based on data
make_blog_index.run()

#make TOS/ Software License page
make_legal.run()

make_allprojects.run()

#update homepage
make_homepage.run()