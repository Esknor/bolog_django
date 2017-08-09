from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^1/', views.basic_one, name = 'basic_one' ),
	#url(r'^2/', views.basic_two, name = 'basic_two' ),
	url(r'^$', views.articles, name = 'articles'),
	url(r'^article/(?P<article_id>\d+)/$', views.article, name = 'article' ),
	url(r'^article/addlike/(?P<article_id>\d+)/$', views.addlike, name = 'addlike' ),
	url(r'^article/addcomment/(?P<article_id>\d+)/$', views.addcomment, name = 'addcomment' ),
	#url(r'^/auth/logout/$', view),
]
