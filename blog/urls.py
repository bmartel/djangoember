from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('blog.views',
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    url(r"^post/(\d+)$", views.post, name="post"),
    url(r"^add_comment/(\d+)/$", "add_comment"),
)