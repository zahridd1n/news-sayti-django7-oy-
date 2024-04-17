from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializer


@api_view(['GET'])
def category_list(request):
    data = models.Category.objects.all()
    serializer_datas = serializer.CategoryListSerializer(data, many=True)
    return Response(serializer_datas.data)


@api_view(['GET'])
def category_detail(request, id):
    data = models.Category.objects.get(id=id)
    serializer_data = serializer.CategoryDetailSerializer(data)
    return Response(serializer_data.data)


@api_view(['GET'])
def post_list(request):
    news = models.Post.objects.all()
    serializer_datas = serializer.PostListSerializer(news, many=True)
    return Response(serializer_datas.data)


@api_view(['GET', 'POST'])
def post_detail(request, id):
    posts = models.Post.objects.get(id=id)
    serializer_data = serializer.PostDetailSerializer(posts)
    return Response(serializer_data.data)


@api_view(['GET'])
def region_list(request):
    regions = models.Region.objects.all()
    serializer_data = serializer.RegionListSerializer(regions, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def region_detail(request, id):
    region = models.Region.objects.get(id=id)
    serializer_data = serializer.RegionDetailSerializer(region)
    return Response(serializer_data.data)