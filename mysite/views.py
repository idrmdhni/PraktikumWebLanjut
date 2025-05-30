from django.shortcuts import render, redirect
from article.models import Category, BlogArticle

def index(request):
    template_name = "landingpage/index.html"
    category = Category.objects.all()
    article = BlogArticle.objects.all()
    context = {
        "title" : "Beranda",
        "category" : category,
        "article" : article
    }
    
    return render(request, template_name, context)

def article_detail(request, id):
    template_name = "landingpage/detail.html"
    try:
        article = BlogArticle.objects.get(id=id)
    except:
        return redirect(article_not_found)
    
    another_article = BlogArticle.objects.all().exclude(id=id)

    context = {
        "article" : article,
        "another_article" : another_article
    }
    
    return render(request, template_name, context)

def article_not_found(request):
    template_name = "article_not_found.html"
    return render(request, template_name)

def contact(request):
    template_name = "contact.html"
    context = {
        "title" : "Kontak"
    }
    
    return render(request, template_name, context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/")
    template_name = "dashboard/index.html"
    context = {
        "title" : "Dashboard"
    }
    
    return render(request, template_name, context)

def article_list(request):
    template_name = "dashboard/article_list.html"
    context = {
        "title" : "Daftar Artikel"
    }
    
    return render(request, template_name, context)

def gallery(request):
    template_name = "gallery.html"
    context = {
        "title" : "Galeri"
    }
    
    return render(request, template_name, context)