"""shop_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shop_app import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductListCreateAPIView.as_view()),
    # path('api/v1/products/<int:id>/', views.product_detail_view),
    path('api/v1/products/reviews/', views.ProductReviewCreateAPIView.as_view()),
    # path('api/v1/products/tags/', views.products_tags_view),
    path('api/v1/login/', views.LoginAPIView.as_view()),
    path('api/v1/register/', views.RegisterAPIView.as_view()),

    path('api/v1/categories/', views.CategoriesListCreateAPIView.as_view()),
    path('api/v1/tags/', views.TagsListCreateAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductDetailPutDeleteAPIView.as_view()),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

