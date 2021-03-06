from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from blog import views


urlpatterns = [
    path('', views.HomePost.as_view(), name='home_posts'),
    path('posts/<pk_post>/', views.PostDetail.as_view(), name='post_detail'),
    path('product/<pk_product>/', views.ProductDetail.as_view(), name='product_detail'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:category_pk>/', views.CategoryDetail.as_view(), name='category_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)