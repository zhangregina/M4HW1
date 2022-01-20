from rest_framework import serializers
from .models import Product, Category, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = 'id title'.split()  # ['id', 'name']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews']


class ProductTagsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title tags'.split()

    def get_tags(self, product):
        active_tags = product.tags.filter(is_active=True)
        data = CategorySerializer(active_tags, many=True).data
        return data


class ProductPutSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=30)
    description = serializers.CharField(default=None)
    price = serializers.IntegerField(required=True)
    category = serializers.IntegerField(required=True)
    tags = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate_title(self, title):
        products = Product.objects.filter(title=title)
        if products:
            raise ValidationError('This product already exists!!')
        return title

