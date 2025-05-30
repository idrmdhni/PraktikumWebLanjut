from django.urls import path

from article.views import (
    admin_category_list,
    admin_add_category,
    admin_edit_category,
    admin_delete_category,

    admin_article_list,
    admin_add_article,
    admin_edit_article,
    admin_delete_article,
)

urlpatterns = [
    path("category/list", admin_category_list, name="admin_category_list"),
    path("category/add", admin_add_category, name="admin_add_category"),
    path("category/edit/<int:category_id>", admin_edit_category, name="admin_edit_category"),
    path("category/delete/<int:category_id>", admin_delete_category, name="admin_delete_category"),

    path("article/list", admin_article_list, name="admin_article_list"),
    path("article/add", admin_add_article, name="admin_add_article"),
    path("article/edit/<int:article_id>", admin_edit_article, name="admin_edit_article"),
    path("article/delete/<int:article_id>", admin_delete_article, name="admin_delete_article"),
]