from django.urls import path, include
from .import views
from django.contrib.auth import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('master', views.master, name='master'),
    path('signup', views.signup, name='signup'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('accounts/', include('django.contrib.auth.urls')),

    #Cart Urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail', views.cart_detail, name='cart_detail'),

    # CheckOut Page
    path('checkout', views.checkout, name='checkout'),

    # Order Page
    path('order', views.order, name='order'),

    # Product Page
    path('product', views.product, name='product'),
    path('product_detail', views.product_detail, name='product_detail'),

    # Search Page
    path('search', views.search, name='search')



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

