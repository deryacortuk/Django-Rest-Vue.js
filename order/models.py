from django.db import models
from cart.models import Cart
import uuid
from product.models import VideoModel
from django.conf import settings
from account.models import User


STATUS_CHOICES = (
 ('paid','Paid'),('refunded','refunded')
)  



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")       
    stripe_id = models.CharField(max_length=250, blank=True)    
    paid = models.BooleanField(default=True)        
    status = models.CharField(choices=STATUS_CHOICES, default='paid',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    class Meta:
        ordering = ('-created_at',)
        
    
    def __str__(self):
        return str(self.id)
    
   
    
    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        if '__test__' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        else:
            path = '/'
        return f"https://dashoard.stripe.com{path}payments/{self.stripe_id}"
    

    
 
    


class OrderItem(models.Model):
    order= models.ForeignKey(Order,related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(VideoModel, related_name="items",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    def total(self):
        return round(self.price * self.quantity,2)