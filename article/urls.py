from django.urls import path

from article.views import (
   article_list,
   add_article,
   edit_article,
   delete_article,

    admin_category_list,
    admin_add_category,
    admin_edit_category,
    admin_delete_category,

    admin_article_list,
    admin_add_article,
    admin_edit_article,
    admin_delete_article,

    admin_management_user_list,
    admin_management_user_edit,
    admin_management_user_delete,
)

urlpatterns = [
    # User
    path("article", article_list, name="article_list"),
    path("article/add", add_article, name="add_article"),
    path("article/edit/<int:article_id>", edit_article, name="edit_article"),
    path("article/delete/<int:article_id>", delete_article, name="delete_article"),

    # Admin
    path("operator/category", admin_category_list, name="admin_category_list"),
    path("operator/category/add", admin_add_category, name="admin_add_category"),
    path("operator/category/edit/<int:category_id>", admin_edit_category, name="admin_edit_category"),
    path("operator/category/delete/<int:category_id>", admin_delete_category, name="admin_delete_category"),

    path("operator/article", admin_article_list, name="admin_article_list"),
    path("operator/article/add", admin_add_article, name="admin_add_article"),
    path("operator/article/edit/<int:article_id>", admin_edit_article, name="admin_edit_article"),
    path("operator/article/delete/<int:article_id>", admin_delete_article, name="admin_delete_article"),

    path("operator/management_user", admin_management_user_list, name="admin_management_user_list"),
    path("operator/management_user/edit/<int:user_id>", admin_management_user_edit, name="admin_management_user_edit"),
    path("operator/management_user/delete/<int:user_id>", admin_management_user_delete, name="admin_management_user_delete"),
]