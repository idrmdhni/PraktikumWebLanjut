from rest_framework import serializers
from article.models import BlogArticle

class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ['id', 'category', 'title', 'content', 'image', 'status', 'created_at', "created_by"]
        # fields = '__all__' # Bisa juga seperti itu