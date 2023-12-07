from django.shortcuts import get_object_or_404
from order.models import Order, OrderItem
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from cart.models import Cart, CartItem
from order.tasks import order_created
from django.urls import reverse
import logging
from django.http import Http404
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from order.serializers import OrderSerializer
from django.utils import timezone

logger = logging.getLogger(__name__)




# class MyListAPIView(APIView):        
#     # @method_decorator(cache_page(60))
#     def get(self, request,fromat=None):               
#         user = request.user.id 
#         print(request.user.id)
#         current_time = timezone.now()
#         time_difference_threshold = timezone.timedelta(days=90)
#         products = Order.objects.filter(user=user,created_at__lt=current_time - time_difference_threshold)
#         serializer = OrderSerializer(products,context={"request":request}, many=True)
#         return Response(serializer.data)
class MyListAPIView(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #4permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, context={"request":request},many=True)
        return Response(serializer.data)