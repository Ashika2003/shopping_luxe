from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/',views.buy_now, name='buy_now'),
    path('profile/',views.profile, name='profile'),
    path('address/', views.address,  name='address'),
    path('orders/', views.orders,  name='orders'),
    path('changepassword/', views.change_password,  name='changepassword'),
    path('login/', views.login,  name='login'),
    path('registeration/', views.costumerregister,  name='customerregistration'),
    path('checkout/', views.checkout,  name='checkout'),
    path('mobile/', views.mobile,  name='mobile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)