from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.
def menu(request):
    category = Category.objects.all()
    context={
        "category":category,

    }
    return render(request,"kiosk/menu.html",context)
