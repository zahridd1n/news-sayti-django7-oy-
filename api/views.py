from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializer


@api_view(['GET'])
def home_page(request):
    """Asosiy sahifa uchun api"""
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    posts = models.Post.objects.all()

    categorys_serializer = serializer.CategoryListSerializer(categorys, many=True)
    regions_serializer = serializer.RegionListSerializer(regions, many=True)
    posts_serializer = serializer.PostListSerializer(posts, many=True)

    return Response(
        {
            'categorys': categorys_serializer.data,
            'regions': regions_serializer.data,
            'posts': posts_serializer.data,
        }
    )


@api_view(['GET'])
def post_in_category(request, id):
    """tanlangan kategoryaga qarab postlarni filterlab beruvchi  funksiya"""
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    try:
        category = models.Category.objects.get(id=id)
        posts = models.Post.objects.filter(category=category)

        categorys_serializer = serializer.CategoryListSerializer(categorys, many=True)
        regions_serializer = serializer.RegionListSerializer(regions, many=True)
        posts_serializer = serializer.PostListSerializer(posts, many=True)

        return Response(
            {
                'categorys': categorys_serializer.data,
                'regions': regions_serializer.data,
                'posts': posts_serializer.data,
            })
    except models.Category.DoesNotExist:
        return Response(
            {
                'message': 'Category not found'
            }
        )


@api_view(['GET'])
def post_in_region(request, id):
    """tanlangan kategoryaga qarab postlarni filterlab beruvchi  funksiya"""
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    try:
        region = models.Region.objects.get(id=id)
        posts = models.Post.objects.filter(region=region)

        categorys_serializer = serializer.CategoryListSerializer(categorys, many=True)
        regions_serializer = serializer.RegionListSerializer(regions, many=True)
        posts_serializer = serializer.PostListSerializer(posts, many=True)

        return Response(
            {
                'categorys': categorys_serializer.data,
                'regions': regions_serializer.data,
                'posts': posts_serializer.data,
            })
    except models.Region.DoesNotExist:
        return Response(
            {
                'message': 'Region not found'
            }
        )


@api_view(['GET', 'POST'])
def post_detail(request, id):
    """postning ichiga kirgandagi chiqadigan malumotlar"""
    try:
        posts = models.Post.objects.get(id=id)
        serializer_data = serializer.PostDetailSerializer(posts)
        return Response(serializer_data.data)
    except models.Post.DoesNotExist:
        return Response(
            {
                'message': 'Post not found'
            }
        )


@api_view(['POST'])
def comment_post(request, id):
    """postga comment yozish"""
    try:
        post = models.Post.objects.get(id=id)
        if request.method == 'POST':
            text = request.data.get('text')
            models.Comment.objects.create(
                post=post,
                text=text
            )
            return Response(
                {
                    'message': 'Comment created'
                }
            )
    except:
        return Response(
            {
                'message': 'Comment creation failed'
            }
        )


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
