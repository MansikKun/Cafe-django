from django.db import models



#Customer
class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    def __str__(self):
        return self.customer_name
#Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(verbose_name="order date")
    total_price = models.IntegerField()
    def __str__(self):
        return self.total_price
#Category
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
#Menu
class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus')
    menu_name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, help_text="simple description")
    quantity = models.IntegerField()
    def __str__(self):
        return self.menu_name    
    
#OrderMenu(연결 테이블)
class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_menus')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_orders')
    order_quantity = models.IntegerField()
    items_price = models.IntegerField()
    def __str__(self):
        return self.order_quantity

