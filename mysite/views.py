from django.shortcuts import render, redirect
from article.models import Category, BlogArticle
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models import Count

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

def api(request):
    template_name = "landingpage/api.html"
    
    context = {
        "title" : "Api",
    }
    
    return render(request, template_name, context)

def get_article_by_category(request, category_id):
    template_name = "landingpage/index.html"
    category = Category.objects.all()
    selected_category = Category.objects.get(name=category_id)
    article = BlogArticle.objects.filter(category=selected_category)
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

    current_path = request.path

    # Bersihkan slash di awal/akhir dan pecah path menjadi beberapa bagian
    path_components = current_path.strip('/').split('/')

    breadcrumbs = []

    url_so_far = ''
    for component in path_components:
        url_so_far += f'/{component}'
        breadcrumbs.append({
            'name': component.replace('-', ' ').capitalize(), # Ganti '-' dengan spasi dan buat huruf kapital
            'url': url_so_far
        })
    
    if Group.objects.get(name='Operator') in request.user.groups.all():
        articles = BlogArticle.objects.all()
        print('operator')
    else:
        articles = BlogArticle.objects.filter(created_by=request.user)
        print(request.user.groups.all())
    
    categories = Category.objects.all()
    users = User.objects.all()
    user_list = User.objects.annotate(total_article=Count('blogarticle')).filter(
    total_article__gt=0)

    template_name = "dashboard/index.html"
    context = {
        "title" : "Dashboard",
        "articles": articles,
        "categories": categories,
        "users": users,
        "user_list": user_list,
        'breadcrumbs': breadcrumbs
    }
    
    return render(request, template_name, context)

def gallery(request):
    template_name = "gallery.html"
    context = {
        "title" : "Galeri"
    }
    
    return render(request, template_name, context)