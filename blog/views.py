# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
	articles = models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})
	#return HttpResponse('<html>helloWorld</html>') 
def article_page(request,id):
 	article = models.Article.objects.get(pk=id)
 	return render(request,'blog/article_page.html',{'article':article})
def edit_page(request):
 	return render(request,'blog/edit_page.html')
def edit_action(request):
	title = request.POST.get('title','TITLE')
	content = request.POST.get('content','CONTENT')
	models.Article.objects.create(title=title,content=content)
	articles = models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles}) 