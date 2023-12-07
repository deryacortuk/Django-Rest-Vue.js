from rest_framework import serializers
from order.models import Order, OrderItem
from django.utils.translation import gettext_lazy as _

from product.serializers import VideoReadSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    #product = VideoReadSerializer()
    class Meta:
        model = OrderItem
        fields = ("id","order","product","quantity","price")

class OrderSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(source="user.get_full_name",read_only=True)    
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id","stripe_id","items","first_name","last_name","email","address","zip_code","phone","status","paid","created_at","updated_at","total_price")
    
    def create(self, validated_data):
       
        items_data = validated_data.pop('items') 
        
        order = Order.objects.create(**validated_data)

       
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order