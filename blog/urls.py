from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$',views.index,name='main_page'),
	url(r'^(?P<id>[0-9]+)$',views.article_page,name='article_page'),
	url(r'^edit/$',views.edit_page,name='edit_page'),
	url(r'^edit_action/$',views.edit_action,name='edit_action'),
] 
 