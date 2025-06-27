from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from article.models import BlogArticle
from article.serializer import BlogArticleSerializer

@api_view(['GET'])
def api_blog_article_list(request):
    article = BlogArticle.objects.all()
    serializer = BlogArticleSerializer(article, many = True)
    content = {
        'message' : 'success',
        'record' : article.count(),
        'rows' : serializer.data
    }
    return Response(content, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_blog_article_add(request):
    data = request.data.copy()

    serializer = BlogArticleSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message' : 'The article has been added successfully',
                'data' : serializer.data
            },
            status = status.HTTP_201_CREATED
        )
    else:
        return Response(
            {
                'message' : 'Article failed to be added',
                'errors' : serializer.errors
            },
            status = status.HTTP_400_BAD_REQUEST
        )

@api_view(['PUT'])
def api_blog_article_update(request, article_id):
    article = get_object_or_404(BlogArticle, id = article_id)
    data = request.data.copy()

    serializer = BlogArticleSerializer(instance = article, data = data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message' : 'The article has been updated successfully',
                'data' : serializer.data
            },
            status = status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'message' : 'Article failed to be updated',
                'errors' : serializer.errors
            },
            status = status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['DELETE'])
def api_blog_article_delete(request, article_id):
    try:
        article = get_object_or_404(BlogArticle, id=article_id)
        article.delete()
        return Response(
            {
                'message' : 'The article has been deleted successfully',
            },
            status = status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'message' : 'Article failed to be deleted',
            },
            status = status.HTTP_400_BAD_REQUEST
        )
