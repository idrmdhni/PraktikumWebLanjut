from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from article.models import Category, BlogArticle
from article.forms import CategoryForms, ArticleForms

# Create your views here.

# Admin
# Kategori
@login_required(login_url='/auth-login')
def admin_category_list(request):
    template_name = "dashboard/admin/category_list.html"
    categories = Category.objects.all()
    context = {
        'title' : 'Daftar Kategori',
        'categories' : categories
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_add_category(request):
    template_name = "dashboard/admin/category_form.html"
    if request.method == "POST":
        forms = CategoryForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil menambah kategori")
            return redirect(admin_category_list)

    forms = CategoryForms()
    context = {
        'title' : 'Tambah Kategori',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_edit_category(request, category_id):
    template_name = "dashboard/admin/category_form.html"
    category_name =  Category.objects.get(id = category_id)

    if request.method == "POST":
        forms = CategoryForms(request.POST, instance=category_name)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil memperbarui kategori")
            return redirect(admin_category_list)

    forms = CategoryForms(instance=category_name)
    context = {
        'title' : 'Edit Kategori',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_delete_category(request, category_id):
    try:
        Category.objects.get(id=category_id).delete()
        messages.success(request, "Berhasil menghapus kategori")
    except:
        messages.error(request, "Gagal menghapus kategori")

    return redirect(admin_category_list)

# Artikel
@login_required(login_url='/auth-login')
def admin_article_list(request):
    template_name = "dashboard/admin/article_list.html"
    articles = BlogArticle.objects.all()
    context = {
        'title' : 'Daftar Artikel',
        'articles' : articles
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_add_article(request):
    template_name = "dashboard/admin/article_form.html"
    if request.method == "POST":
        forms = ArticleForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil menambah artikel")
            return redirect(admin_article_list)

    forms = ArticleForms()
    context = {
        'title' : 'Tambah Artikel',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_edit_article(request, article_id):
    template_name = "dashboard/admin/article_form.html"
    article_name =  BlogArticle.objects.get(id = article_id)

    if request.method == "POST":
        forms = ArticleForms(request.POST, request.FILES, instance=article_name)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil memperbarui artikel")
            return redirect(admin_article_list)

    forms = ArticleForms(instance=article_name)
    context = {
        'title' : 'Edit Artikel',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_delete_article(request, article_id):
    try:
        BlogArticle.objects.get(id = article_id).delete()
        messages.success(request, "Berhasil menghapus artikel")
    except:
        messages.error(request, "Gagal menghapus artikel")

    return redirect(admin_article_list)
