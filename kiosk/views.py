from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


# Create your views here.
def menu(request):
    category = Category.objects.all()
    context={
        "category":category,

    }
    return render(request,"kiosk/menu.html",context)
def order(request):
    order = Order.objects.all()
    context={
        "order":order,

    }
    return render(request,"kiosk/order.html",context)

def add_ordermenu(request,menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    customer = Customer.objects.first()#로그인 화면 추가시 수정예정
    order, created = Order.objects.get_or_create(
        customer=customer, 
        order_date__date=timezone.now().date(),
        defaults={'total_price': 0}
    )
    
    # 주문 메뉴를 가져오거나 새로 생성합니다.
    order_menu, created = OrderMenu.objects.get_or_create(
        order=order, 
        menu=menu,
        defaults={'order_quantity': 0, 'items_price': 0}
    )
    
    # 주문 수량을 1 증가시키고, 항목 가격을 업데이트합니다.
    order_menu.order_quantity += 1
    order_menu.items_price = menu.price * order_menu.order_quantity
    order_menu.save()
    
    # 주문의 총 가격을 업데이트합니다.
    order.total_price += menu.price
    order.save()
    
    return HttpResponseRedirect(reverse('kiosk:menu'))
def remove_ordermenu(request,menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    customer = Customer.objects.first()#로그인 화면 추가시 수정예정
    order = Order.objects.filter(
        customer=customer, 
        order_date__date=timezone.now().date()
    ).first()
    
    if order:
        # 주문 메뉴 객체를 가져옵니다.
        order_menu = OrderMenu.objects.filter(order=order, menu=menu).first()
        
        if order_menu:
            # 주문 수량을 1 감소시킵니다.
            order_menu.order_quantity -= 1
            
            if order_menu.order_quantity <= 0:
                # 주문 수량이 0 이하이면 객체를 삭제합니다.
                order_menu.delete()
            else:
                # 아니면, 항목 가격을 업데이트하고 저장합니다.
                order_menu.items_price = menu.price * order_menu.order_quantity
                order_menu.save()
                
            # 주문의 총 가격을 업데이트합니다.
            order.total_price -= menu.price
            if order.total_price < 0:
                order.total_price = 0
            order.save()
    
    return HttpResponseRedirect(reverse('kiosk:menu'))