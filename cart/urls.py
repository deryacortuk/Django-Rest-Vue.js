from django.urls import path
from cart.views import add_cart,delete_item, CartListAPIView

app_name = "cart"

urlpatterns = [
    path("add/<id>", add_cart, name="add_cart"),
    path("checkout/", CartListAPIView.as_view(),name="cart_list"),
    path("delete/<id>/",delete_item, name="delete_product"),
    
    
]
