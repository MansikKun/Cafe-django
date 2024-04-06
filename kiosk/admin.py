from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','phone_number')
    search_fields=('customer_name','phone_number')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','order_date','total_price')
    search_fields=('order_date','total_price')
@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','category_name')
@admin.register(Menu)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','menu_name','category','price','description','quantity')

@admin.register(OrderMenu)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','order','menu','order_quantity')

