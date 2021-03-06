from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from blog.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from blog.forms import *
from django.core.context_processors import csrf
from django.contrib import auth

def basic_one(request):
	vova = "Vova"
	vera = "Vera"
	html = "<html><body>"+ vova + " love " + vera +"</body></html>" 
	return HttpResponse(html)

	
def basic_two(request):
	vova = "Vova"
	vera = "Vera"
	return render_to_response('basic_two.html', {'vova':vova, 'vera':vera})


def articles(request):
	articles = Article.objects.all()
	username = auth.get_user(request).username
	return render_to_response('articles.html', {'articles': articles, 'username': username})

def article(request, article_id):
	comment_form = CommentForm
	args = {}
	args.update(csrf(request))
	args['article'] = Article.objects.get(id = article_id)
	args['comments'] = Comments.objects.filter(comments_article_id = article_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('article.html', args)

def addlike(request, article_id):
	try:
		if article_id in request.COOKIES:
			redirect('/')
		else:
			article = Article.objects.get(id = article_id)
			article.article_likes += 1
			article.save()
			response = redirect('/')
			response.set_cookie(article_id, "test")
			return response
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')

def addcomment(request, article_id):
	if request.POST and ('pause' not in request.session):
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comments_article = Article.objects.get(id=article_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] = True
	return redirect('/')
	
	
	
