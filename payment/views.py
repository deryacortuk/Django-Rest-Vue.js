from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.conf import settings
from order.models import Order
import stripe
from decimal import Decimal
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponseBadRequest, JsonResponse
from order.serializers import OrderSerializer
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_checkout_session(request):
    #order_id = request.data.get('order_id')
    #order = get_object_or_404(Order, id=order_id)
    
    success_url = request.build_absolute_uri(reverse('payment:done'))
    cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
    
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        
        # line_items = []
        # for item in serializer.validated_data["items"]:
        #     line_items.append({
        #     'price_data': {
        #         'unit_amount': int(item.price * Decimal('100')),
        #         'currency': 'usd',
        #         'product_data': {
        #             'name': item.product.title,
        #         },
        #     },
        #     'quantity': item.quantity,
        # })

    #     session_data = {
    #     'payment_method_types': ['card'],
    #     'line_items': line_items,
    #     'mode': 'payment',
    #     'client_reference_id': serializer.id,
    #     'success_url': success_url,
    #     'cancel_url': cancel_url,
    # }
        #session = stripe.checkout.Session.create(**session_data)
        total_price = sum(
            item.get('quantity') * item.get('product').price 
            for item in serializer.validated_data['items']
        )
        try:
            
            charge = stripe.Charge.create(
                amount=int(total_price * 100),
                currency='usd',
                description='Online Education Payment',
                source=serializer.validated_data['stripe_id']
            )

            serializer.save(user=request.user, total_price=total_price)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def payment_done(request):
    
    return Response(status=status.HTTP_200_OK)

def payment_canceled(request):
   
    return Response(status=status.HTTP_400_BAD_REQUEST)