from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse
from account.models import User
from django.utils.text import slugify
from random import randint
from product.validator import file_size

class VideoModel(models.Model):
    CATEGORY_CHOICES = (
        ('anatomi', 'Anatomi'),
        ('biokimya', 'Biyokimya'),
        ('farmakoloji', 'Farmakoloji'),
        
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, db_index=True)     
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    duration = models.CharField(max_length=50, blank=True, null=True, default='3 Month')
    video_file = models.FileField(upload_to='videos/',validators=[file_size])
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title

    class Meta:
        
        indexes = [
            models.Index(fields=['slug', 'available']),  
        ]

    # def get_absolute_url(self):
    #     return reverse('product:video_detail', args=[self.slug])
    def get_absolute_url(self):
        return f'/{self.slug}/'


    
class VideoReviews(models.Model):
    
    product_id=models.ForeignKey(VideoModel,on_delete=models.CASCADE)    
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)    
    rating=models.CharField(default="0",max_length=255,null=True, blank=True)
    review=models.TextField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created_at",)
        
    def __str__(self):
        return str(self.product_id)
    
