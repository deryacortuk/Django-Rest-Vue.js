from django.urls import path
from order import views

app_name="order"
urlpatterns = [
 
    path('list/', views.MyListAPIView.as_view(), name='order_list'),
]