from django.contrib import admin
from django.urls import path, include

# Media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import *
from mysite.authentication import login, register, logout
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("article/<int:id>", article_detail, name="article_detail"),
    path("article_not_found", article_not_found, name="article_not_found"),
    path("dashboard/", dashboard, name="dashboard"),
    path("dashboard/", include("article.urls")),
    path("dashboard/article_list", article_list, name="article_list"),
    path("contact", contact, name="contact"),
    path("gallery", gallery, name="gallery"),


    ################ Authentication ################
    path("auth-login", login, name="login"),
    path("auth-register", register, name="register"),
    path("auth-logout", logout, name="logout")
]

# Media
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# CKEditor
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
