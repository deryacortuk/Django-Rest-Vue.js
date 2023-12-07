from django.shortcuts import render
from product.serializers import VideoReadSerializer,VideoWriteSerializer,VideoReviewsSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import VideoModel,VideoReviews
from rest_framework.views import APIView
from django.db.models import Q
from django.http import Http404
from django.views.decorators.clickjacking import xframe_options_exempt

class VideoListAPIView(APIView):
    
    
    # @method_decorator(cache_page(60))
    def get(self, request,fromat=None):               
        products = VideoModel.objects.all()
        serializer = VideoReadSerializer(products,context={"request":request}, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    
    def get_object(self, product_slug):
        try:
            return VideoModel.objects.get(slug=product_slug)
        except VideoModel.DoesNotExist:
            return Http404
    
    def get(self, request, product_slug, fromat=None):
        product = self.get_object(product_slug)
        serialize = VideoReadSerializer(product,context={"request":request})
        return Response(serialize.data)

@api_view(['POST'])
def search_api(request):
    query = request.data.get('query', '')
    if query:
        products = VideoModel.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        serializer = VideoReadSerializer(products,context={"request":request}, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})