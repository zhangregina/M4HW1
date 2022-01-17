from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ReviewSerializer, \
    ProductTagsSerializer
from .models import Product, Category, Review


@api_view(['GET', 'POST'])
def product_list_view(request):
    # if request.method == 'GET':
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


# elif request.method == 'POST':
#     title = request.data['title']
#     description = request.data.get('description','')
#     price = request.data['price']
#     category = request.data['category']
#     tags = request.data['tags']
#     product = Product.objects.create(
#         title=title, description=description,
#         price=price
#     )
#     return Response()
#
#     body = request.data
#     print(body)
#     return Response()


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie Not Found!'})
    data = ProductDetailSerializer(product, many=False).data  # many=False стоит по дефолту, его не обяз писать
    return Response(data=data)


@api_view(['GET'])
def product_reviews_view(request):
    products = Product.objects.all()
    data = ReviewSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def products_tags_view(request):
    products = Product.objects.all()
    data = ProductTagsSerializer(products, many=True).data
    return Response(data=data)
