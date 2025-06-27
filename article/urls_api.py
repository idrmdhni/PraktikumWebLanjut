from django.urls import path

from article.api import (
    api_blog_article_list,
    api_blog_article_add,
    api_blog_article_update,
    api_blog_article_delete
)

urlpatterns = [
    # Api
    path("article/list", api_blog_article_list),
    path("article/add", api_blog_article_add),
    path("article/update/<int:article_id>", api_blog_article_update),
    path("article/delete/<int:article_id>", api_blog_article_delete),
]