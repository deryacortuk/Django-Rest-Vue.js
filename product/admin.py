from django.contrib import admin
from product.models import VideoModel, VideoReviews

@admin.register(VideoModel)
class VideoProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'quantity','category')
    list_filter = ('available', 'category')
    search_fields = ('title', 'category')
    ordering = ('title',)
    

    
@admin.register(VideoReviews)
class VideoReviewsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_id', 'rating', 'created_at', )
    list_filter = ('product_id', 'user_id')
    search_fields = ('product_id', 'rating')
    ordering = ('created_at',)
    
