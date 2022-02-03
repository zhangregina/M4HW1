from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(Category):

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='product_category')
    tags = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.product.title


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username and self.password

