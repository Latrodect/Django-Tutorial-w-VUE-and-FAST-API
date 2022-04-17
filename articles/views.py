from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")

    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    
    context = {
        "object":article_obj
    }
    return render(request, "articles/search.html", context=context)

@login_required
def create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        article_object = form.save() #only work in model form important!!
        context['form'] = ArticleForm()
        #title = form.cleaned_data.get()
        #content = request.POST.get("content")
        #article_object = Article.objects.create(title=title, content=content)
        #print(title,content)
        #context['title'] = title
        #context['content'] = content
        context['object'] = article_object
        context['created'] = True
    
    return render(request, "articles/create.html", context=context)

def article_detail(request,id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)