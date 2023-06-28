from django.contrib import admin
from . models import Product, Customer, Cart, payment, OrderPlaced, Wishlist
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','product', 'quantity']

@admin.register(payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']
    
@admin.register(OrderPlaced)
class OrderPlacedMOdelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']
    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']