from django.urls import path
from . import views

app_name = "kiosk"

urlpatterns = [
    path("", views.menu,name='menu'),
    path('kiosk/add_ordermenu/<int:menu_id>/', views.add_ordermenu, name='add_ordermenu'),
    path('kiosk/remove_ordermenu/<int:menu_id>/', views.remove_ordermenu, name='remove_ordermenu'),
]