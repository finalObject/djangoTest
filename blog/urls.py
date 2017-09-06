from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$',views.index),
	url(r'^(?P<id>[0-9]+)$',views.article_page,name='article_page'),
	url(r'^edit$',views.edit_page,name='edit_page')
] 
 