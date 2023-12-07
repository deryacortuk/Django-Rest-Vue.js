from django.urls import path
from product.views import  VideoListAPIView,search_api,ProductDetail
app_name = "product"

urlpatterns = [
  path("video/<slug:product_slug>/",ProductDetail.as_view(),name="video_detail"),
  path("videos/",VideoListAPIView.as_view(),name="videos"),
    path('search/', search_api),
]
