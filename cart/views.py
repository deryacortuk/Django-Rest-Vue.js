from django.shortcuts import redirect, get_object_or_404,render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from cart.serializers import CartItemSerializer, CartSerializer
from cart.models import Cart, CartItem
from product.models import VideoModel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
import json
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseBadRequest, JsonResponse

 
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_cart(request,id):
   
    if request.method =="POST":
        product_obj = get_object_or_404(VideoModel, pk=id)
        cart_obj, _ = Cart.objects.get_existing_or_new(request)        
        
        cart_item_obj, created = CartItem.objects.get_or_create(product=product_obj,cart=cart_obj)
     
        cart_item_obj.save()
        serializer = CartSerializer(cart_obj, context={"request":request})
        return Response(serializer.data)
        
    



class CartListAPIView(ListAPIView):
    
    
    def get(self, request, format=None):
        
        user = request.user        
        cart_list = Cart.objects.filter(user=user, used=False)       
        
        serializer = CartSerializer(cart_list, many=True)        
       
        return Response(serializer.data)
    


@login_required
def delete_item(request,id):
    if request.method == "POST":
        cartitem = CartItem.objects.get(id=id)
        cartitem.cart.user = request.user
        cartitem.delete()
        return JsonResponse(data={"success":"Product was deleted."})
    else:
        return HttpResponseBadRequest("Invalid request.")

        
            