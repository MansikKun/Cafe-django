from django.db import models



#Customer
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

#Order
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField("order date")
    total_price = models.IntegerField()
    
#Category
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)

#Menu
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    menu_name = models.CharField(max_length=200)
    price = models.IntegerField()

#OrderMenu(연결 테이블)
class OrderMenu(models.Model):
    order_menu_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    items_price = models.IntegerField()


#Logs
class Logs(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_type = models.CharField(max_length=200)
    timestamp = models.DateTimeField()