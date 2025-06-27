from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages

from article.models import Category, BlogArticle
from article.forms import CategoryForms, ArticleForms

# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True
    
def breadcrumbs(request):
    current_path = request.path

    # Bersihkan slash di awal/akhir dan pecah path menjadi beberapa bagian
    path_components = current_path.strip('/').split('/')

    breadcrumbs = []

    url_so_far = ''
    for component in path_components:
        url_so_far += f'/{component}'
        breadcrumbs.append({
            'name': component.replace('_', ' ').title(), # Ganti '-' dengan spasi dan buat huruf kapital
            'url': url_so_far
        })
    
    return breadcrumbs

# User
# Artikel
def article_list(request):
    template_name = "dashboard/user/article_list.html"
    articles = BlogArticle.objects.filter(created_by=request.user)

    context = {
        'title' : 'Daftar Artikel',
        'articles' : articles,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def add_article(request):
    template_name = "dashboard/admin/article_form.html"
    if request.method == "POST":
        forms = ArticleForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil menambah artikel")
            return redirect(article_list)

    forms = ArticleForms()
    context = {
        'title' : 'Tambah Artikel',
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def edit_article(request, article_id):
    template_name = "dashboard/admin/article_form.html"
    try:
        article_name =  BlogArticle.objects.get(id = article_id, created_by=request.user)
    except:
        messages.warning(request, "Halaman tidak ditemukan!")
        return redirect("/dashboard")

    if request.method == "POST":
        forms = ArticleForms(request.POST, request.FILES, instance=article_name)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "Berhasil memperbarui artikel")
            return redirect(article_list)

    forms = ArticleForms(instance=article_name)
    context = {
        'title' : 'Edit Artikel',
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def delete_article(request, article_id):
    try:
        BlogArticle.objects.get(id = article_id, created_by=request.user).delete()
        messages.success(request, "Berhasil menghapus artikel")
    except:
        messages.error(request, "Gagal menghapus artikel")

    return redirect(article_list)


# Admin
# Kategori
@login_required(login_url='/')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_category_list(request):
    template_name = "dashboard/admin/category_list.html"
    categories = Category.objects.all()
    context = {
        'title' : 'Daftar Kategori',
        'categories' : categories,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')

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
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
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
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_delete_category(request, category_id):
    try:
        Category.objects.get(id=category_id).delete()
        messages.success(request, "Berhasil menghapus kategori")
    except:
        messages.error(request, "Gagal menghapus kategori")

    return redirect(admin_category_list)

# Artikel
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_article_list(request):
    template_name = "dashboard/admin/article_list.html"
    articles = BlogArticle.objects.all()
    context = {
        'title' : 'Daftar Artikel',
        'articles' : articles,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
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
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
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
        'forms' : forms,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_delete_article(request, article_id):
    try:
        BlogArticle.objects.get(id = article_id).delete()
        messages.success(request, "Berhasil menghapus artikel")
    except:
        messages.error(request, "Gagal menghapus artikel")

    return redirect(admin_article_list)


# Managemen user oleh operator
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    users = User.objects.all()
    context = {
        'title' : 'Daftar User',
        'users' : users,
        'breadcrumbs': breadcrumbs(request)
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/dashboard')
def admin_management_user_delete(request, user_id):
    try:
        User.objects.get(id = user_id).delete()
        messages.success(request, "Berhasil menghapus akun")
    except:
        messages.error(request, "Gagal menghapus akun")

    return redirect(admin_management_user_list)

@login_required(login_url='/auth-login/')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = 'dashboard/admin/user_edit.html'
    user = get_object_or_404(User, pk=user_id) # Ambil objek user berdasarkan ID, atau 404 jika tidak ditemukan
    all_groups = Group.objects.all()
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff = request.POST.get("is_staff")
        groups_checked = request.POST.getlist('groups')

        if is_staff == None:
            is_staff = False
        else:
            is_staff = True
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f"berhasil update user {user.username}")
        return redirect(admin_management_user_list) # Redirect ke halaman daftar user setelah berhasil

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user,
        'breadcrumbs': breadcrumbs(request)
    }

    return render(request, template_name, context)