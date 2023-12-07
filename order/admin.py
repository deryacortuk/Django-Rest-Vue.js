from django.contrib import admin

from order.models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):        
    model = OrderItem
    raw_id_fields = ['product']
    


@admin.register(Order)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user","status","created_at"]    
    inlines = [OrderItemAdmin]