from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    
    context = {
        "object_list":qs
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
        return redirect(article_object.get_absolute_url())
        #title = form.cleaned_data.get()
        #content = request.POST.get("content")
        #article_object = Article.objects.create(title=title, content=content)
        #print(title,content)
        #context['title'] = title
        #context['content'] = content
        #context['object'] = article_object
        #context['created'] = True
    
    return render(request, "articles/create.html", context=context)

def article_detail(request,slug=None):
    article_obj = None
    
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).last()
        except:
            raise Http404
        
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)