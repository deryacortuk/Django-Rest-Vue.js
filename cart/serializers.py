from rest_framework import serializers
from rest_framework.fields import Field
from cart.models import Cart, CartItem
from product.models import VideoModel
from django.utils.translation import gettext_lazy as _
import json


class CartProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VideoModel
        fields = ["title","slug","price","quantity"]
        read_only_fields = fields
        
    

class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer()
    
    class Meta:
        model = CartItem
        get_cost = Field(source="get_cost")
        fields = ["id","product","quantity","get_cost"]

        
class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(read_only=True, many=True)
    user = serializers.HiddenField(default =serializers.CurrentUserDefault())
    
    class Meta:
        model = Cart
        total = Field(source='total')               
        total_cart_products = Field(source="total_cart_products")
        fields = ["id","user","total","total_cart_products","products"]
        
    def to_representation(self, instance):
        representation = super(CartSerializer, self).to_representation(instance)
        products = representation.pop("products")
        test = json.dumps(products)              
        
        representation["products"] = json.loads(test)

        return representation