from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ReviewSerializer, \
    ProductTagsSerializer, ProductPutSerializer, RegisterSerializer
from .models import Product, Category, Review, Tag

from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

# permission_classes = [permissions.IsAuthenticated]


# @api_view(['GET', 'POST'])
# def product_list_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         data = ProductSerializer(products, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         title = request.data['title']
#         description = request.data.get('description', '')
#         price = request.data['price']
#         category = request.data['category']
#         tags = request.data['tags']
#         product = Product.objects.create(
#             title=title, description=description,
#             price=price, category_id=category
#         )
#         product.tags.set(tags)
#         return Response(data=ProductDetailSerializer(product).data,
#                         status=status.HTTP_201_CREATED)
#

# @api_view(['GET', 'DELETE', 'PUT'])
# def product_detail_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Product Not Found!'})
#     if request.method == 'GET':
#         data = ProductDetailSerializer(product, many=False).data  # many=False стоит по дефолту, его не обяз писать
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(data={'message': 'The product has been deleted.'})
#     elif request.method == 'PUT':
#         serializer = ProductPutSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#
#         serializer = ProductDetailSerializer(product, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "Successfully updated!!!"
#             return Response(data=data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def product_reviews_view(request):
#     products = Product.objects.all()
#     data = ReviewSerializer(products, many=True).data
#     return Response(data=data)


# @api_view(['GET'])
# def products_tags_view(request):
#     products = Product.objects.all()
#     data = ProductTagsSerializer(products, many=True).data
#     return Response(data=data)
#

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from shop_app.serializers import CategorySerializer
from rest_framework.pagination import PageNumberPagination


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = PageNumberPagination


class TagsListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer


class ProductDetailPutDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'


class ProductReviewCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ReviewSerializer


class LoginAPIView(GenericAPIView):
    def post(self, request):
        user = authenticate(**request.data)  # (username:"admin",password: "123")
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'user not found :c'}, status=404)


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


