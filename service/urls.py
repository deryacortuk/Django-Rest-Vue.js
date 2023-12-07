
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include("account.urls",namespace="account")),
    path('api/v1/product/', include('product.urls',namespace="product")),
    path('api/v1/order/', include('order.urls',namespace="order")),
    path('api/v1/payment/', include('payment.urls',namespace="payment")),
    path('api/v1/cart/', include('cart.urls',namespace="cart")),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
